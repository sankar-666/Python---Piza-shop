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
                print("admin conforme")
                q="select * from login where usertype='admin' and status='active'"
                adminact=select(q)
                if adminact:
                    flash("Login Succeessfully")
                    return redirect(url_for("admin.adminhome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 

            # elif utype == "stationmaster":
            #     q="select * from stationmaster where login_id='%s'"%(session['loginid'])
            #     val=select(q)
            #     if val:
            #         session['stid']=val[0]['smaster_id']
            #         return redirect(url_for("stationmaster.stationmasterhome"))
               
            
            else:
                flash("failed try again")
                return redirect(url_for("public.login"))


    return render_template("login.html")