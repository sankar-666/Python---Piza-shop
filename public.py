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
        print(q)
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
            elif utype == "customer":
                q="select * from login where usertype='customer' and status='active'"
                customeract=select(q)
                if customeract:
                    q="select * from customer where username='%s'"%(session['email'])
                    session['cid']=select(q)[0]['customer_id']
                    flash("Login Succeessfully")
                    return redirect(url_for("customer.customerhome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 
            elif utype == "courier":
                q="select * from login where usertype='courier' and status='active'"
                courieract=select(q)
                if courieract:
                    q="select * from courier where username='%s'"%(session['email'])
                    session['cor_id']=select(q)[0]['courier_id']
                    flash("Login Succeessfully")
                    return redirect(url_for("courier.courierhome"))
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



@public.route("/reg",methods=['get','post'])
def reg():
    if 'btn' in request.form:
        email=request.form['email']
        passw=request.form['passw']
        fname=request.form['fname']
        lname=request.form['lname']
        housename=request.form['housename']
        street=request.form['street']
        city=request.form['city']
        district=request.form['district']
        pincode=request.form['pincode']
        phone=request.form['phone']
        dob=request.form['dob']
        gender=request.form['gender']

        q="select * from login where username='%s'"%(email)
        res=select(q)
        if res:
            flash("This email already exist!, try register with new one.")
        else:
            q="insert into login values('%s','%s','customer','active')"%(email,passw)
            insert(q)
            q="insert into customer values (NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','active')"%(email,fname,lname,housename,street,city,district,pincode,phone,dob,gender)
            # print(q)
            insert(q)
            flash("Registration successfull")
            return redirect(url_for("public.login"))
    return render_template("reg.html")