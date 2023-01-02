from flask import *
from database import *
import uuid

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



@staff.route('/staffmanagecategory',methods=['get','post'])
def staffmanagecategory():
    data={}
    if 'submit' in request.form:
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into category values (null,'%s','%s','inactive')"%(name,desc)
        insert(q)
        return redirect(url_for("staff.staffmanagecategory"))

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
        return redirect(url_for("staff.staffmanagecategory"))
    if action == "inactive":
        q="update category set status='inactive' where category_id='%s' "%(cat_id)
        update(q)
        return redirect(url_for("staff.staffmanagecategory"))

    if action == "update":
        q="select * from category where category_id='%s'"%(cat_id)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update category set category_name='%s', category_desc='%s' where category_id='%s' "%(name,desc,cat_id)
            update(q)
            return redirect(url_for("staff.staffmanagecategory"))
    return render_template('staffmanagecategory.html',data=data) 



@staff.route('/staffmanagesubcategory',methods=['get','post'])
def staffmanagesubcategory():
    data={}

    q="select * from category where status='active' "
    data['cat']=select(q)
    if 'submit' in request.form:
        catid=request.form['catid']
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into subcategory values (null,'%s','%s','%s','inactive')"%(catid,name,desc)
        insert(q)
        return redirect(url_for("staff.staffmanagesubcategory"))


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
        return redirect(url_for("staff.staffmanagesubcategory"))
    if action == "inactive":
        q="update subcategory set status='inactive' where subcategory_id='%s' "%(subid)
        update(q)
        return redirect(url_for("staff.staffmanagesubcategory"))

    if action == "update":
        q="select * from subcategory where subcategory_id='%s'"%(subid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update subcategory set subcategory_name='%s', subcategory_desc='%s' where subcategory_id='%s' "%(name,desc,subid)
            update(q)
            return redirect(url_for("staff.staffmanagesubcategory"))
    return render_template('staffmanagesubcategory.html',data=data) 

@staff.route('/staffmanageitems',methods=['get','post'])
def staffmanageitems():
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
        return redirect(url_for("staff.staffmanageitems"))


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
        return redirect(url_for("staff.staffmanageitems"))
    if action == "inactive":
        q="update product set status='inactive' where product_id='%s' "%(pid)
        update(q)
        return redirect(url_for("staff.staffmanageitems"))

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
            return redirect(url_for("staff.staffmanageitems"))
    return render_template('staffmanageitems.html',data=data) 



@staff.route("/staffmanagepurchase",methods=['get','post'])
def staffmanagepurchase():
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
            q="insert into purchasemaster values(null,'%s','%s',0,'pending',curdate())"%(vid,session['sid'])
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
        q="update purchasemaster set total=total+'%s' where purchasemaster_id='%s'"%(amount,pmaster_id)
        update(q)
        flash("Purchased Sucessfully")
        return redirect(url_for("staff.staffmanagepurchase"))
    return render_template("staffmanagepurchase.html",data=data)


@staff.route('/staffviewbookings')
def staffviewbookings():
    data={}
    q="SELECT * FROM `ordermaster`, `orderdetails`, `customer`, `product` WHERE `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` AND `ordermaster`.`customer_id`=`customer`.`customer_id` AND `orderdetails`.`product_id`=`product`.`product_id`"
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        omid=request.args['omid']  
    else:
        action=None

    if action == "dispatch":
        q="update ordermaster set order_status='Dispatched' where ordermaster_id='%s' "%(omid)
        update(q)
        return redirect(url_for("staff.staffviewbookings"))
    
    return render_template('staffviewbookings.html',data=data)


@staff.route('/staffviewcustomers')
def staffviewcustomers():
    data={}
    cid=request.args['cid']
    q="SELECT * from customer where customer_id='%s'"%(cid)
    data['res']=select(q)


    return render_template('staffviewcustomers.html',data=data)


@staff.route('/staffviewpayment')
def staffviewpayment():
    data={}
    omid=request.args['omid']
    q="select * from payment where type='booking' and ordermaster_id='%s' group by payment_id desc limit 1  "%(omid)
    data['viewpayment']=select(q)


    return render_template('staffviewpayment.html',data=data)


@staff.route('/staffbookingaddraw',methods=['get','post'])
def staffbookingaddraw():
    data={}
    omid=request.args['omid']
    q="select * from rawmaterials"
    data['raw']=select(q)

    if 'rawbtn' in request.form:
        rawid=request.form['rawid']

        q="select * from rawmaterialused where ordermaster_id='%s' " %(omid)
        val=select(q)
        if val:
            flash("Rawmaterial details Already Added!")
            return redirect(url_for("staff.staffviewbookings")) 
        else:
            q="insert into rawmaterialused values(null,'%s','booking','%s',(select quantity from rawmaterials where raw_mat_id='%s'))"%(omid,rawid,rawid)
            # print(q)
            insert(q)
            return redirect(url_for("staff.staffviewbookings")) 


    return render_template('staffbookingaddraw.html',data=data)


@staff.route('/staffviewtoppings',methods=['get','post'])
def staffviewtoppings():
    data={}
    q="SELECT * FROM `customer`, `topping` WHERE `customer`.`customer_id`=`topping`.`customer_id`"
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        tid=request.args['tid']  
    else:
        action=None

    if action == "approve":
        data['approve']=True

        if 'btn' in request.form:
            amount=request.form['amount']
            q="update topping set topping_price='%s', topping_status='Approved by staff' where topping_id='%s'"%(amount,tid)
            update(q)
            return redirect(url_for("staff.staffviewtoppings"))
    
    if action == "viewpayment":

        q="select * from payment where type='topping' and ordermaster_id='%s' group by payment_id desc limit 1  "%(tid)
        data['viewpayment']=select(q)

        if 'dispatch' in request.form:
            q="update topping set topping_status='Dispatched' where topping_id='%s' "%(tid)
            update(q)
            return redirect(url_for("staff.staffviewtoppings"))
    
    if action=='addraw':
        q="select * from rawmaterials"
        data['raw']=select(q)

        if 'rawbtn' in request.form:
            rawid=request.form['rawid']

            q="select * from rawmaterialused where ordermaster_id='%s' " %(tid)
            val=select(q)
            if val:
                flash("Rawmaterial details Already Added!")
                return redirect(url_for("staff.staffviewtoppings")) 
            else:
                q="insert into rawmaterialused values(null,'%s','topping','%s',(select quantity from rawmaterials where raw_mat_id='%s'))"%(tid,rawid,rawid)
                print(q)
                insert(q)
                return redirect(url_for("staff.staffviewtoppings")) 
    return render_template('staffviewtoppings.html',data=data)