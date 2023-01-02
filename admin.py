from flask import *
from database import *
import uuid

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
    q="select * from vendor where vendor_status='active'"
    data['ven']=select(q)
    # print(data['ven'])
    if 'submit' in request.form:
       
        ven_id=request.form['ven_id']
        raw=request.form['raw']
        quant=request.form['quant']
      
        q="insert into rawmaterials values (null,'%s','%s','%s')"%(ven_id,raw,quant)
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
            quant=request.form['quant']

            q="update rawmaterials set raw_mat='%s', quantity='%s' where raw_mat_id='%s' "%(raw,quant,rawid)
            update(q)
            return redirect(url_for("admin.adminmanagerawmaterials"))
    return render_template('adminmanagerawmaterials.html',data=data) 



@admin.route('/adminmanagecourier',methods=['get','post'])
def adminmanagecourier():
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
            return redirect(url_for("admin.adminmanagecourier"))

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
        return redirect(url_for("admin.adminmanagecourier"))
    if action == "inactive":
        q="update login set status='inactive' where username='%s' "%(uname)
        update(q)
        q="update courier set courier_status='inactive' where courier_id='%s' "%(corid)
        update(q)
        return redirect(url_for("admin.adminmanagecourier"))

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
            return redirect(url_for("admin.adminmanagecourier"))
    return render_template('adminmanagecourier.html',data=data) 




@admin.route('/adminmanagecaterogy',methods=['get','post'])
def adminmanagecaterogy():
    data={}
    if 'submit' in request.form:
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into category values (null,'%s','%s','inactive')"%(name,desc)
        insert(q)
        return redirect(url_for("admin.adminmanagecaterogy"))

    data={}
    q="select * from category"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        cat_id=request.args['cat_id']

      
    else:
        action=None

    if action == "active":
        q="update category set status='active' where category_id='%s' "%(cat_id)
        update(q) 
        return redirect(url_for("admin.adminmanagecaterogy"))
    if action == "inactive":
        q="update category set status='inactive' where category_id='%s' "%(cat_id)
        update(q)
        return redirect(url_for("admin.adminmanagecaterogy"))

    if action == "update":
        q="select * from category where category_id='%s'"%(cat_id)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update category set category_name='%s', category_desc='%s' where category_id='%s' "%(name,desc,cat_id)
            update(q)
            return redirect(url_for("admin.adminmanagecaterogy"))
    return render_template('adminmanagecaterogy.html',data=data) 



@admin.route('/adminmanagesubcategory',methods=['get','post'])
def adminmanagesubcategory():
    data={}

    q="select * from category where status='active' "
    data['cat']=select(q)
    if 'submit' in request.form:
        catid=request.form['catid']
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into subcategory values (null,'%s','%s','%s','inactive')"%(catid,name,desc)
        insert(q)
        return redirect(url_for("admin.adminmanagesubcategory"))


    q="select * from subcategory"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        subid=request.args['subid']

      
    else:
        action=None

    if action == "active":
        q="update subcategory set status='active' where subcategory_id='%s' "%(subid)
        update(q) 
        return redirect(url_for("admin.adminmanagesubcategory"))
    if action == "inactive":
        q="update subcategory set status='inactive' where subcategory_id='%s' "%(subid)
        update(q)
        return redirect(url_for("admin.adminmanagesubcategory"))

    if action == "update":
        q="select * from subcategory where subcategory_id='%s'"%(subid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update subcategory set subcategory_name='%s', subcategory_desc='%s' where subcategory_id='%s' "%(name,desc,subid)
            update(q)
            return redirect(url_for("admin.adminmanagesubcategory"))
    return render_template('adminmanagesubcategory.html',data=data) 



@admin.route('/adminmanageitems',methods=['get','post'])
def adminmanageitems():
    data={}

    q="select * from subcategory where status='active'"
    data['sub']=select(q)

    if 'submit' in request.form:
        subid=request.form['subid']
        name=request.form['name']
        desc=request.form['desc']
        price=request.form['price']
        image=request.files['image']
        path="static/uploads/"+str(uuid.uuid4())+image.filename
        image.save(path)
    
        q="insert into product values (null,'%s','%s','%s','%s','%s','inactive')"%(subid,name,desc,path,price)
        insert(q)
        return redirect(url_for("admin.adminmanageitems"))


    q="select * from product"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        pid=request.args['pid']

      
    else:
        action=None

    if action == "active":
        q="update product set status='active' where product_id='%s' "%(pid)
        update(q) 
        return redirect(url_for("admin.adminmanageitems"))
    if action == "inactive":
        q="update product set status='inactive' where product_id='%s' "%(pid)
        update(q)
        return redirect(url_for("admin.adminmanageitems"))

    if action == "update":
        q="select * from product where product_id='%s'"%(pid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']
            price=request.form['price']
            image=request.files['image']
            path="static/uploads/"+str(uuid.uuid4())+image.filename
            image.save(path)
            print(image.filename)
            if image.filename == "":
                q="update product set product_name='%s', product_desc='%s' , product_price='%s' where product_id='%s' "%(name,desc,price,pid)
                update(q)
            else:
                q="update product set product_name='%s', product_desc='%s' , product_image='%s', product_price='%s' where product_id='%s' "%(name,desc,path,price,pid)
                update(q)
            return redirect(url_for("admin.adminmanageitems"))
    return render_template('adminmanageitems.html',data=data) 



@admin.route("/adminmanagepurchase",methods=['get','post'])
def adminmanagepurchase():
    data={}
    q="select * from vendor where vendor_status='active'"
    data['ven']=select(q)
    q="select * from rawmaterials"
    data['raw']=select(q)
    if 'submit' in request.form:
        vid=request.form['vid']
        rid=request.form['rid']
        amount=request.form['amount']

        q="select * from purchasemaster where status='pending'"
        res=select(q)
        if res:
            pmaster_id=res[0]['purchasemaster_id']
        else:
            q="insert into purchasemaster values(null,'%s',0,0,'pending',curdate())"%(vid)
            pmaster_id=insert(q)

        q="select * from purchasechild where raw_mat_id='%s' and purchasemaster_id='%s'"%(rid,pmaster_id)
        val=select(q)
        if val:
            q="update purchasechild set quantity=quantity+(select quantity from rawmaterials where raw_mat_id='%s') where prurchasechild_id='%s'"%(rid,val[0]['prurchasechild_id'])
            update(q)
        else:
            q="insert into purchasechild values(null,'%s','%s','%s',(select quantity from rawmaterials where raw_mat_id='%s'))"%(pmaster_id,rid,amount,rid)
            insert(q)
        q="update rawmaterials set quantity=quantity+(select quantity from rawmaterials where raw_mat_id='%s') where raw_mat_id='%s'"%(rid,rid)
        update(q)
        q="update purchasemaster set staff_id='0', total=total+'%s' where purchasemaster_id='%s'"%(amount,pmaster_id)
        update(q)
        flash("Purchased Sucessfully")
        return redirect(url_for("admin.adminmanagepurchase"))

    q="SELECT * FROM `purchasemaster`, `purchasechild`, `rawmaterials` WHERE `purchasemaster`.`purchasemaster_id`=`purchasechild`.`purchasemaster_id` AND `purchasechild`.`raw_mat_id`=`rawmaterials`.`raw_mat_id` and status='pending'"
    data['res']=select(q)

    if 'btn' in request.form:
    
        q="update purchasemaster set status='purchase completed' where staff_id='0' and status='pending' "
        update(q)
        return redirect(url_for("admin.adminmanagepurchase"))
    return render_template("adminmanagepurchase.html",data=data)


@admin.route('/adminviewbooking')
def adminviewbooking():
    data={}
    q="SELECT * FROM `ordermaster`, `orderdetails`, `customer`, `product` WHERE `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` AND `ordermaster`.`customer_id`=`customer`.`customer_id` AND `orderdetails`.`product_id`=`product`.`product_id`"
    data['res']=select(q)
    return render_template('adminviewbooking.html',data=data)

@admin.route('/adminviewcustomer')
def adminviewcustomer():
    data={}
    cid=request.args['cid']
    q="SELECT * FROM customer where customer_id='%s'"%(cid)
    data['res']=select(q)
    return render_template('adminviewcustomer.html',data=data)

@admin.route('/adminviewpayment')
def adminviewpayment():
    data={}
    omid=request.args['omid']
    q="SELECT * FROM payment where ordermaster_id='%s'"%(omid)
    data['res']=select(q)
    return render_template('adminviewpayment.html',data=data)


@admin.route('/adminviewdeliverystatus')
def adminviewdeliverystatus():
    data={}
    omid=request.args['omid']
    q="SELECT * FROM ordermaster where ordermaster_id='%s'"%(omid)
    data['res']=select(q)
    print(data['res'])
    return render_template('adminviewdeliverystatus.html',data=data)


@admin.route("/adminviewcomplaints",methods=['get','post'])
def adminviewcomplaints():

    
    data={}
    q="select * from customer inner join complaint using (customer_id)"
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
    else:
        action=None

    if action == "reply":
        data['replysec']=True

        if 'submit' in request.form:
            reply=request.form['reply']

            q="update complaint set reply='%s' where complaint_id='%s'"%(reply,cid)
            update(q)
            return redirect(url_for("admin.adminviewcomplaints"))
    return render_template("adminviewcomplaints.html",data=data)




@admin.route('/adminviewpurchasedhistory')
def adminviewpurchasedhistory():
    data={}
    sid=session['sid']
    q="SELECT * FROM `purchasemaster`, `purchasechild`, `rawmaterials`, `vendor` WHERE `purchasemaster`.`purchasemaster_id`=`purchasechild`.`purchasemaster_id` AND `purchasechild`.`raw_mat_id`=`rawmaterials`.`raw_mat_id` AND `purchasemaster`.`vendor_id`=`vendor`.`vendor_id` and purchasemaster.staff_id='0'"
    data['res']=select(q)
    
    return render_template('adminviewpurchasedhistory.html',data=data)