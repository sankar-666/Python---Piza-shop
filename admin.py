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

        q="select * from login where username='%s'"%(email)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else:
            q="insert into login values ('%s','%s','staff','inactive')"%(email,password)
            insert(q)
            q="insert into staff values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',curdate(),'inactive')"%(email,fname,lname,desig,street,city,district,state,pin,phone,gender,dob)
            insert(q)
            return redirect(url_for("admin.adminmanagestaff"))

    data={}
    q="select * from staff"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        uname=request.args['uname']
        stid=request.args['stid']
      
    else:
        action=None

    if action == "active":
        q="update login set status='active' where username='%s' "%(uname)
        update(q)
        q="update staff set staff_status='active' where staff_id='%s' "%(stid)
        update(q)
        return redirect(url_for("admin.adminmanagestaff"))
    if action == "inactive":
        q="update login set status='inactive' where username='%s' "%(uname)
        update(q)
        q="update staff set staff_status='inactive' where staff_id='%s' "%(stid)
        update(q)
        return redirect(url_for("admin.adminmanagestaff"))

    if action == "update":
        q="select * from staff where staff_id='%s'"%(stid)
        val=select(q)
        data['staff']=val

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

            q="update staff set staff_fname='%s', staff_lname='%s', staff_desig='%s', staff_street='%s', staff_city='%s', staff_dist='%s', staff_state='%s', staff_pincode='%s', staff_phone='%s', staff_gender='%s', staff_dob='%s' where staff_id='%s' "%(fname,lname,desig,street,city,district,state,pin,phone,gender,dob,stid)
            update(q)
            return redirect(url_for("admin.adminmanagestaff"))
    return render_template('adminmanagestaff.html',data=data) 



@admin.route('/adminmanagevendor',methods=['get','post'])
def adminmanagevendor():
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
    

       
        q="insert into vendor values (null,'0','%s','%s','%s','%s','%s','%s','%s','%s','inactive')"%(email,name,gonum,street,city,district,pin,phone)
        insert(q)
        return redirect(url_for("admin.adminmanagevendor"))
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
        return redirect(url_for("admin.adminmanagevendor"))
    if action == "inactive":
       
        q="update vendor set vendor_status='inactive' where vendor_id='%s' "%(vid)
        update(q)
        return redirect(url_for("admin.adminmanagevendor"))

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
            return redirect(url_for("admin.adminmanagevendor"))
    return render_template('adminmanagevendor.html',data=data) 



@admin.route('/adminmanagerawmaterials',methods=['get','post'])
def adminmanagerawmaterials():
    data={}
    q="select * from vendor"
    data['ven']=select(q)
    # print(data['ven'])
    if 'submit' in request.form:
       
        ven_id=request.form['ven_id']
        raw=request.form['raw']
      
        q="insert into rawmaterials values (null,'%s','%s')"%(ven_id,raw)
        insert(q)
        return redirect(url_for("admin.adminmanagerawmaterials"))
   
    q="select * from rawmaterials"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        rawid=request.args['rawid']
   
      
    else:
        action=None

    if action == "delete":
      
        q="delete from rawmaterials where raw_mat_id='%s' "%(rawid)
        delete(q)
        return redirect(url_for("admin.adminmanagerawmaterials"))
    

    if action == "update":
        q="select * from rawmaterials where raw_mat_id='%s'"%(rawid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
           
            raw=request.form['raw']

            q="update rawmaterials set raw_mat='%s' where raw_mat_id='%s' "%(raw,rawid)
            update(q)
            return redirect(url_for("admin.adminmanagerawmaterials"))
    return render_template('adminmanagerawmaterials.html',data=data) 