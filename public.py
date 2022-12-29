from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')

@public.route('/login',methods=['post','get'])
def login():

    if 'submit' in request.form:
        email=request.form['email']
        pasw =request.form['password']

        q="select * from login where username='%s' and password='%s'"%(email,pasw)
        res=select(q)


        if res:
            session['email']=res[0]["username"]
            utype=res[0]["usertype"]
            if utype == "admin":
                q="select * from login where usertype='admin' and status='active'"
                adminact=select(q)
                if adminact:
                    flash("Login Succeessfully")
                    return redirect(url_for("admin.adminhome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 
            elif utype == "staff":
                q="select * from login where usertype='staff' and status='active'"
                staffact=select(q)
                if staffact:
                    q="select * from staff where username='%s'"%(session['email'])
                    session['sid']=select(q)[0]['staff_id']
                    flash("Login Succeessfully")
                    return redirect(url_for("staff.staffhome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 
            else:
                flash("failed try again")
                return redirect(url_for("public.login"))
        else:
            flash("invalid Email or Password!")
            return redirect(url_for("public.login"))

    return render_template("login.html")