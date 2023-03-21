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
        # state=request.form['state']
        pin=request.form['pin']
        phone=request.form['phone']
        gender=request.form['gender']
        dob=request.form['dob']

        q="select * from login where username='%s'"%(email)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else:
            q="insert into login values ('%s','%s','staff','active')"%(email,password)
            insert(q)
            q="insert into staff values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',curdate(),'nil','nil','nil','nil','active')"%(email,fname,lname,desig,street,city,district,pin,phone,gender,dob)
            staffid=insert(q)
            
            if desig=="Delivery Boy":
                return redirect(url_for('admin.adminmanagecourier',staffid=staffid))
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
            # state=request.form['state']
            pin=request.form['pin']
            phone=request.form['phone']
            # gender=request.form['gender']
            dob=request.form['dob']

            q="update staff set staff_fname='%s', staff_lname='%s', staff_desig='%s', staff_street='%s', staff_city='%s', staff_dist='%s', staff_pincode='%s', staff_phone='%s', staff_dob='%s' where staff_id='%s' "%(fname,lname,desig,street,city,district,pin,phone,dob,stid)
            update(q)
            return redirect(url_for("admin.adminmanagestaff"))
    return render_template('adminmanagestaff.html',data=data) 



@admin.route('/adminmanagevendor',methods=['get','post'])
def adminmanagevendor():
    data={}
    if 'submit' in request.form:
       
        # email=request.form['email']
        name=request.form['fname']
        gonum=request.form['gonum']
     
        # street=request.form['street']
        city=request.form['city']
        district=request.form['district']
  
        pin=request.form['pin']
        phone=request.form['phone']
    

       
        q="insert into vendor values (null,'0','%s','%s','%s','%s','%s','%s','active')"%(name,gonum,city,district,pin,phone)
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
        
            # street=request.form['street']
            city=request.form['city']
            district=request.form['district']
    
            pin=request.form['pin']
            phone=request.form['phone']

            q="update vendor set vendor_name='%s', vendor_godown_num='%s', vendor_city='%s', vendor_dist='%s', vendor_pincode='%s', vendor_phone='%s' where vendor_id='%s' "%(name,gonum,city,district,pin,phone,vid)
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
        quant=0
        prof=request.form['prof']
      
        q="insert into rawmaterials values (null,'%s','%s','%s','%s','0')"%(ven_id,raw,quant,prof)
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
            prof=request.form['prof']

            q="update rawmaterials set raw_mat='%s',prof='%s' where raw_mat_id='%s' "%(raw,prof,rawid)
            update(q)
            q="SELECT * FROM purchasechild  WHERE raw_mat_id='%s' GROUP BY price"%(rawid)
            val=select(q)
            q="select labour_cost as l from product where raw_mat_id='%s'"%(rawid)
            print(q)
            lcost=int(select(q)[0]['l'])
            if val:
                for i in val:
                    cp=i['price']
                    print(cp)
                    sp=i['selling_price'] 
                    # sp=int(cp)+(int(cp)*int(pro)/100)
                    # print(sp)
                    nsp=int(cp)+(int(cp)*(int(prof)/100))
                    print(cp)
                    print(sp)
                    print(nsp)
                    q="update purchasechild set selling_price='%s' WHERE selling_price='%s'"%(nsp,sp)
                    update(q)
                    Q="update product set product_price='%s'+'%s' where raw_mat_id='%s'"%(lcost,nsp,rawid)
                    update(Q)
            return redirect(url_for("admin.adminmanagerawmaterials"))
    return render_template('adminmanagerawmaterials.html',data=data) 



@admin.route('/adminmanagecourier',methods=['get','post'])
def adminmanagecourier():
    data={}
    staffid=request.args['staffid']
    if 'submit' in request.form:
        lic_no=request.form['lic_no']
        lic_exp=request.form['lic_exp']
        insu_no=request.form['insu_no']
        insu_exp=request.form['insu_exp']
        
        q="update staff set license_number='%s', license_expiry='%s',insurance_number='%s',insurance_expiry='%s' where staff_id='%s'"%(lic_no,lic_exp,insu_no,insu_exp,staffid)
        update(q)
        return redirect(url_for("admin.adminmanagestaff"))
   

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
            return redirect(url_for("admin.adminmanagestaff"))
    return render_template('adminmanagecourier.html',data=data) 




@admin.route('/adminmanagecategory',methods=['get','post'])
def adminmanagecategory():
    data={}
    if 'submit' in request.form:
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into category values (null,'%s','%s','inactive')"%(name,desc)
        insert(q)
        return redirect(url_for("admin.adminmanagecategory"))

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
        return redirect(url_for("admin.adminmanagecategory"))
    if action == "inactive":
        q="update category set status='inactive' where category_id='%s' "%(cat_id)
        update(q)
        return redirect(url_for("admin.adminmanagecategory"))

    if action == "update":
        q="select * from category where category_id='%s'"%(cat_id)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update category set category_name='%s', category_desc='%s' where category_id='%s' "%(name,desc,cat_id)
            update(q)
            return redirect(url_for("admin.adminmanagecategory"))
    return render_template('adminmanagecategory.html',data=data) 



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
    
    q1="select * from rawmaterials "
    data['raw']=select(q1)
    
    lprice = 150

    if 'submit' in request.form:
        subid=request.form['subid']
        rawid=request.form['rawid']
        name=request.form['name']
        desc=request.form['desc']
        # price=request.form['price']
        image=request.files['image']
        charge=request.form['charge']

        path="static/uploads/"+str(uuid.uuid4())+image.filename
        image.save(path)

        q1="select * from rawmaterials where raw_mat_id='%s'"%(rawid)    
        print(q1)
        cost=select(q1)[0]['r_price']
        final_cost=int(float(cost)) + int(float(charge))
        
        
        q="insert into product values (null,'%s','%s','%s','%s','%s','%s','%s','active')"%(rawid,subid,name,desc,path,final_cost,charge)
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
        rid=val[0]['raw_mat_id']
        data['upd']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']
            lab=request.form['lab']
            image=request.files['image']
            path="static/uploads/"+str(uuid.uuid4())+image.filename
            image.save(path)
            print(image.filename)
            if image.filename == "":   
                q1="select * from rawmaterials inner join purchasechild using(raw_mat_id) where raw_mat_id='%s'"%(rid)    
                print(q1)
                cost=select(q1)[0]['selling_price']
                final_cost=int(float(cost)) + int(float(lab))
                
                q="update product set product_name='%s', product_desc='%s' , product_price='%s', labour_cost='%s' where product_id='%s' "%(name,desc,final_cost,lab,pid)
                update(q)
            else:
                
                q1="select * from rawmaterials inner join purchasechild using(raw_mat_id) where raw_mat_id='%s'"%(rid)    
                print(q1)
                cost=select(q1)[0]['selling_price']
                final_cost=int(float(cost)) + int(float(lab))
                
                q="update product set product_name='%s', product_desc='%s' , product_image='%s', product_price='%s' where product_id='%s' "%(name,desc,path,final_cost,lab,pid)
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
        amount=int(request.form['amount'])
        qty=request.form['qty']
        
        q="select * from rawmaterials where raw_mat_id='%s'"%(rid)
        per=int(select(q)[0]['prof'])

        se = (per/100) * amount
        selling = amount +se
        
        total = int(float(qty))*int(float(amount))
        
        
        q="select quantity from rawmaterials where raw_mat_id='%s'"%(rid)
        qt = select(q)[0]['quantity']
        q="select * from purchasemaster where status='pending' and vendor_id='%s'"%(vid)
        res=select(q)
        if res:
            pmaster_id=res[0]['purchasemaster_id']
        else:
            q="insert into purchasemaster values(null,'%s',0,0,'pending',curdate())"%(vid)
            pmaster_id=insert(q)
            
            

        q="select * from purchasechild where raw_mat_id='%s' and purchasemaster_id='%s'"%(rid,pmaster_id)
        val=select(q)
        if val:
            q="update purchasechild set quantity=quantity+'%s' , price=price+'%s' where raw_mat_id='%s' and purchasemaster_id='%s'"%(qty,total,rid,pmaster_id)
            update(q)
        else:
            q="insert into purchasechild values(null,'%s','%s','%s','%s','%s','available')"%(pmaster_id,rid,amount,qty,selling)
            insert(q)
      
        q="update purchasemaster set  total=total+'%s' where purchasemaster_id='%s'"%(total,pmaster_id)
        update(q)
        flash("Purchased Sucessfully")
        return redirect(url_for("admin.adminmanagepurchase"))

    q="SELECT *,purchasechild.quantity as quantity FROM `purchasemaster`, `purchasechild`, `rawmaterials`, vendor WHERE `purchasemaster`.`purchasemaster_id`=`purchasechild`.`purchasemaster_id` AND `purchasechild`.`raw_mat_id`=`rawmaterials`.`raw_mat_id` and purchasemaster.vendor_id=vendor.vendor_id and status='pending'"
    data['res']=select(q)

    if 'btn' in request.form:
        
        q="select * from purchasemaster inner join purchasechild using(purchasemaster_id) where status='pending'"
        res=select(q)
        q="select * from purchasemaster where status='pending' and staff_id=0"
        pm_id=select(q)[0]['purchasemaster_id']
                
        if res:
            for i in res:
                item=i['raw_mat_id']
                S_price=i['selling_price']
                P_qty=i['quantity']
                Pur_id=i['purchasechild_id']
                
                q="select * from rawmaterials where raw_mat_id='%s' and quantity='0'"%(item)
                print(q)
                res1=select(q)
                if res1:
                    q="update rawmaterials set quantity='%s',r_price='%s' where  raw_mat_id='%s'"%(P_qty,S_price,item)
                    update(q)
                    q="update purchasechild set pc_status='stock added' where purchasechild_id='%s'"%(Pur_id)
                    update(q)
                    q="update purchasemaster set status='purchase completed'  where purchasemaster_id='%s' "%(pm_id)
                    update(q)
                    q="select * from product inner join rawmaterials using (raw_mat_id) where raw_mat_id='%s'"%(item)
                    valley=select(q)
                    for z in valley:
                        sum=z['labour_cost']
                        rprice=z['r_price']
                        tot=int(float(sum)) + int(float(rprice))
                        q="update product set product_price='%s' where raw_mat_id='%s'"%(tot,item)
                        update(q)
                        
                    # q="select * from tbl_cart_child where Item_id='%s'"%(item)
                    # variable1=select(q)
                    # for j in variable1:
                    #     cart_qty=j['Quantity']
                    #     q="update tbl_cart_child set price='%s'+'%s' where Item_id='%s'"%(S_price,cart_qty,item)
                    #     update(q)
                        # q="select sum(price) from tbl_cart_child inner join tbl_cart_master where Cust_id=''"
                    # flash('Purchase Completed...')
                else:
                    q="update purchasemaster set status='purchase completed'  where purchasemaster_id='%s' "%(pm_id)
                    update(q)
                # flash('Purchase Completed...')
            return redirect(url_for("admin.adminmanagepurchase"))
                

    
        
        # q="select *  from `purchasemaster` INNER JOIN `purchasechild` USING (purchasemaster_id) where staff_id='0' and status='pending'"
        # rees=select(q)
        # print(",,,,,,,,,,,,,,,,,,,,,,",rees)
        # print("hellllllllllllllllllloooooooooooooooooooooo")
        # for i in rees:
        #     q="update rawmaterials set quantity=quantity+'%s' where raw_mat_id='%s'"%(i['quantity'],i['raw_mat_id'])
        #     update(q)
        #     print(q)
        # q="select * from purchasemaster where status='pending' and staff_id=0"
        # pm_id=select(q)[0]['purchasemaster_id']
        # q="update purchasemaster set status='purchase completed' where purchasemaster_id='%s' "%(pm_id)
        # update(q)
        # return redirect(url_for("admin.adminmanagepurchase"))
    return render_template("adminmanagepurchase.html",data=data)


@admin.route('/adminviewbooking')
def adminviewbooking():
    data={}
    q="SELECT * FROM `ordermaster`, `orderdetails`, `customer`, `product` WHERE `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` AND `ordermaster`.`customer_id`=`customer`.`customer_id` AND `orderdetails`.`product_id`=`product`.`product_id` ORDER BY ordermaster.ordermaster_id DESC"
    data['res']=select(q)
    return render_template('adminviewbooking.html',data=data)

@admin.route('/adminviewcustomer')
def adminviewcustomer():
    data={}
    # cid=request.args['cid']
    q="SELECT * FROM customer"
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
    # sid=session['sid']
    q="SELECT * FROM `purchasemaster`, `purchasechild`, `rawmaterials`, `vendor` WHERE `purchasemaster`.`purchasemaster_id`=`purchasechild`.`purchasemaster_id` AND `purchasechild`.`raw_mat_id`=`rawmaterials`.`raw_mat_id` AND `purchasemaster`.`vendor_id`=`vendor`.`vendor_id` and purchasemaster.staff_id='0'"
    data['res']=select(q)
    
    return render_template('adminviewpurchasedhistory.html',data=data)




@admin.route('/adminmanagetoppings',methods=['get','post'])
def adminmanagetoppings():
    data={}
    if 'submit' in request.form:
        name=request.form['name']
        price=request.form['price']
        desc=request.form['desc']
    
        q="insert into topping values (null,'%s','%s','%s','active')"%(name,price,desc)
        insert(q)
        return redirect(url_for("admin.adminmanagetoppings"))

    data={}
    q="select * from topping"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        top_id=request.args['top_id']

      
    else:
        action=None

    if action == "active":
        q="update topping set topping_status='active' where topping_id='%s' "%(top_id)
        update(q) 
        return redirect(url_for("admin.adminmanagetoppings"))
    if action == "inactive":
        q="update topping set topping_status='inactive' where topping_id='%s' "%(top_id)
        update(q)
        return redirect(url_for("admin.adminmanagetoppings"))

    if action == "update":
        q="select * from topping where topping_id='%s'"%(top_id)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            price=request.form['price']
            desc=request.form['desc']

            q="update topping set topping_name='%s', topping_price='%s', topping_desc='%s' where topping_id='%s' "%(name,price,desc,top_id)
            update(q)
            return redirect(url_for("admin.adminmanagetoppings"))
    return render_template('adminmanagetoppings.html',data=data) 

@admin.route('/adminassigndelivery',methods=['get','post'])
def adminassigndelivery():
    data={}
    
    q="select * from staff where staff_desig='Delivery Boy'"
    data['res']=select(q)
    
    if 'assign_del' in request.form:
        del_boy=request.form['del_boy']
        omid=request.args['omid']
        q="insert into delivery values(null,'%s','%s',curdate(),'pending')"%(omid,del_boy)
        insert(q)
        q="update ordermaster set order_status='assigned' where ordermaster_id='%s'"%(omid)
        update(q)
        return redirect(url_for('admin.adminhome'))
    return render_template('adminassigndelivery.html',data=data)
@admin.route('/adminmanagecustomer',methods=['post','get'])
def adminmanagecustomer():
    data={}
    if "searchcust" in request.form:
        search='%'+request.form['srcust']+'%'
        q="select * from customer where customer_fname like '%s'"%(search)
    else:
        q="select * from customer"
    res=select(q)
    data['custview']=res
    
    return render_template('adminmanagecustomer.html',data=data)

@admin.route('/customerreport')
def customerreport():
    data={}
    q="select * from customer"
    res=select(q)
    data['custview']=res
    
    return render_template('customerreport.html',data=data)

@admin.route('/adminviewsales', methods=['post','get'])
def adminviewsales():
    data={}
    # q="select * from ordermaster inner join orderdetails using (ordermaster_id) inner join product using (product_id) inner join customer using (customer_id) where order_status != 'pending'"
    # res=select(q)
    # data['salesview']=res

    if 'sale' in request.form: 
        daily=request.form['daily']
        if request.form['monthly']=="":
            monthly=""
        else:
            monthly=request.form['monthly']+'%'
            
        customer=request.form['customer']
        	
        q="SELECT * FROM `ordermaster` INNER JOIN `orderdetails` USING (ordermaster_id) INNER JOIN `customer` USING(`customer_id`) INNER JOIN `product` USING (product_id)  where (customer_fname like '%s' and order_status <> 'pending')  or (date like '%s' and order_status <> 'pending')  or (date like '%s' and order_status <> 'pending')   "%(customer,daily,monthly)
        res=select(q)
        print(q)
        data['salesview']=res
    else:
       qq="SELECT * FROM `ordermaster` INNER JOIN `orderdetails` USING (ordermaster_id) INNER JOIN `customer` USING(`customer_id`) INNER JOIN `product` USING (product_id)  WHERE  order_status <> 'pending'"
       ress=select(qq)
       data['salesview']=ress   
    return render_template('adminviewsales.html',data=data)

@admin.route('/salesreport')
def salesreport():
    data={}
    qq="SELECT * FROM `ordermaster` INNER JOIN `orderdetails` USING (ordermaster_id) INNER JOIN `customer` USING(`customer_id`) INNER JOIN `product` USING (product_id)  WHERE  order_status <> 'pending'"
    ress=select(qq)
    data['salesview']=ress   
    
    return render_template('salesreport.html',data=data)