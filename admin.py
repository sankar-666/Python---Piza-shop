from flask import *
from database import *

admin=Blueprint('admin',__name__)


@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')


@admin.route('/adminmanagestaff',methods=['get','post'])
def adminmanagestaff():
    data={}
    if 'submit' in request.form:
        email=request.form['email']
        password=request.form['password']
        fname=request.form['fname']
        lname=request.form['lname']
        desig=request.form['desig']
        street=request.form['street']
        city=request.form['city']
        district=request.form['district']
        state=request.form['state']
        pin=request.form['pin']
        phone=request.form['phone']
        gender=request.form['gender']
        dob=request.form['dob']

        q="insert into login values ('%s','%s','staff','inactive')"%(email,password)
        insert(q)
        q="insert into staff values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',curdate(),'inactive')"%(email,fname,lname,desig,street,city,district,state,pin,phone,gender,dob)
        insert(q)

    data={}
    q="select * from staff"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        logid=request.args['logid']
        stid=request.args['stid']
    else:
        action=None

    if action == "active":
        q=""
    return render_template('adminmanagestaff.html',data=data)