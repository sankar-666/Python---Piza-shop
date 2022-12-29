from flask import *
from database import *

staff=Blueprint('staff',__name__)


@staff.route('/staffhome')
def staffhome():
    return render_template('staffhome.html')


@staff.route('/staffmanagevendor',methods=['get','post'])
def staffmanagevendor():
    data={}
    if 'submit' in request.form:
       
        email=request.form['email']
        name=request.form['fname']
        gonum=request.form['gonum']
     
        street=request.form['street']
        city=request.form['city']
        district=request.form['district']
  
        pin=request.form['pin']
        phone=request.form['phone']
    

       
        q="insert into vendor values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','inactive')"%(session['sid'],email,name,gonum,street,city,district,pin,phone)
        insert(q)
        return redirect(url_for("staff.staffmanagevendor"))
    data={}
    q="select * from vendor"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        vid=request.args['vid']
   
      
    else:
        action=None

    if action == "active":
      
        q="update vendor set vendor_status='active' where vendor_id='%s' "%(vid)
        update(q)
        return redirect(url_for("staff.staffmanagevendor"))
    if action == "inactive":
       
        q="update vendor set vendor_status='inactive' where vendor_id='%s' "%(vid)
        update(q)
        return redirect(url_for("staff.staffmanagevendor"))

    if action == "update":
        q="select * from vendor where vendor_id='%s'"%(vid)
        val=select(q)
        data['vendor']=val

        if 'update' in request.form:
           
            name=request.form['fname']
            gonum=request.form['gonum']
        
            street=request.form['street']
            city=request.form['city']
            district=request.form['district']
    
            pin=request.form['pin']
            phone=request.form['phone']

            q="update vendor set vendor_name='%s', vendor_godown_num='%s', vendor_street='%s', vendor_city='%s', vendor_dist='%s', vendor_pincode='%s', vendor_phone='%s' where vendor_id='%s' "%(name,gonum,street,city,district,pin,phone,vid)
            update(q)
            return redirect(url_for("staff.staffmanagevendor"))
    return render_template('staffmanagevendor.html',data=data) 




@staff.route('/staffmanagecourier',methods=['get','post'])
def staffmanagecourier():
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

        q="select * from login where username='%s'"%(email)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else:
            q="insert into login values ('%s','%s','courier','inactive')"%(email,password)
            insert(q)
            q="insert into courier values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',curdate(),'inactive')"%(email,fname,lname,desig,street,city,district,state,pin,phone,gender,dob)
            insert(q)
            return redirect(url_for("staff.staffmanagecourier"))

    data={}
    q="select * from courier"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        uname=request.args['uname']
        corid=request.args['corid']
      
    else:
        action=None

    if action == "active":
        q="update login set status='active' where username='%s' "%(uname)
        update(q)
        q="update courier set courier_status='active' where courier_id='%s' "%(corid)
        update(q)
        return redirect(url_for("staff.staffmanagecourier"))
    if action == "inactive":
        q="update login set status='inactive' where username='%s' "%(uname)
        update(q)
        q="update courier set courier_status='inactive' where courier_id='%s' "%(corid)
        update(q)
        return redirect(url_for("staff.staffmanagecourier"))

    if action == "update":
        q="select * from courier where courier_id='%s'"%(corid)
        val=select(q)
        data['courier']=val

        if 'update' in request.form:
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

            q="update courier set courier_fname='%s', courier_lname='%s', courier_desig='%s', courier_street='%s', courier_city='%s', courier_dist='%s', courier_state='%s', courier_pincode='%s', courier_phone='%s', courier_gender='%s', courier_dob='%s' where courier_id='%s' "%(fname,lname,desig,street,city,district,state,pin,phone,gender,dob,corid)
            update(q)
            return redirect(url_for("staff.staffmanagecourier"))
    return render_template('staffmanagecourier.html',data=data)