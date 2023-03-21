from flask import *
from database import *

customer=Blueprint('customer',__name__)

@customer.route("/customerhome")
def customerhome():
    data={}
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    count=select(q)
    data['count']=len(count)
    return render_template("customerhome.html",data=data)


@customer.route("/customerviewitems",methods=['get','post'])
def customerviewitems():
    data={}
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    count=select(q)
    data['count']=len(count)
    

    if 'searchbtn' in request.form:
        serach='%'+request.form['search']+'%'
       
        q="""SELECT * FROM `product`, `subcategory`, `category` WHERE (`product`.`subcategory_id`=`subcategory`.`subcategory_id` 
            AND `subcategory`.`category_id`=`category`.`category_id` AND `product`.`status`='active' AND `category`.`status`='active' 
            AND `subcategory`.`status`='active' 
            AND product_name LIKE '%s')
            OR

            (`product`.`subcategory_id`=`subcategory`.`subcategory_id` 
            AND `subcategory`.`category_id`=`category`.`category_id` AND `product`.`status`='active' AND `category`.`status`='active' 
            AND `subcategory`.`status`='active' 
            AND category_name LIKE '%s')
            OR
            (`product`.`subcategory_id`=`subcategory`.`subcategory_id` 
            AND `subcategory`.`category_id`=`category`.`category_id` AND `product`.`status`='active' AND `category`.`status`='active' 
            AND `subcategory`.`status`='active' 
            AND subcategory_name LIKE '%s')
            
            GROUP BY product_id"""%(serach,serach,serach)
        # print(q)
    else:
        q="SELECT * FROM `product`, `subcategory`, `category` WHERE `product`.`subcategory_id`=`subcategory`.`subcategory_id` AND `subcategory`.`category_id`=`category`.`category_id` AND `product`.`status`='active' AND `category`.`status`='active' AND `subcategory`.`status`='active' group by product_id"
        # print(q)
    data['res']=select(q)
    # return redirect(url_for("customer.customerviewitems"))   
    return render_template("customerviewitems.html",data=data)


@customer.route("/customeraddtocart",methods=['get','post'])
def customeraddtocart():
    data={}
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    count=select(q)
    data['count']=len(count)
    item=request.args['item']
    category=request.args['category']
    amount=request.args['amount']
    pid=request.args['pid']
    if 'btn' in request.form:
        quantity=request.form['quantity']
        total=request.form['total']
        
        # q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
        # res77=select(q)
        # # q="select * from rawmaterials where "
        # flag=0
        # for i in res77:
        #     print(i['product_id'])
        qt = int(quantity)
        q="select raw_mat_id as raw_mat_id from product where product_id='%s'"%(pid)
        print(q)
        qw11=select(q)
        # for j in qw11:
        raws=qw11[0]['raw_mat_id']
        q="select quantity as quantity from rawmaterials where raw_mat_id='%s'"%(raws)
        mes=select(q)
        # for w in mes:
        rawqtys=int(mes[0]['quantity'])
        print("....................",rawqtys)
        if category == "Medium":
            if qt*2 > rawqtys:
                flag=1
            else:
                flag=0
        elif category == "Large":
            if qt*3 > rawqtys:
                flag=1
            else:
                flag=0
        elif category == "Small":
            if qt > rawqtys:
                flag=1
            else:
                flag=0
         
      
        print("Flag: ",flag)    
        if flag == 1:
            flash("Cant Proceed! Rawquantity out of Stock")
            return redirect(url_for("customer.customerhome"))
        else:  
            q="select * from ordermaster where order_status='pending' and customer_id='%s'"%(session['cid'])
            res=select(q)
            if res:
                oid=res[0]['ordermaster_id']
            else:
                q="insert into ordermaster values(null,'%s',0,curdate(),'pending')"%(session['cid'])
                oid=insert(q)
            q="select * from orderdetails where product_id='%s' and ordermaster_id='%s'"%(pid,oid)
            val=select(q)
            if val:
                q="update orderdetails set quantity=quantity+'%s', total_price=total_price+'%s' where product_id='%s' and ordermaster_id='%s' "%(quantity,total,pid,oid)
                update(q)
            else:
                q="insert into orderdetails values (null,'%s','%s','%s','%s')"%(oid,pid,quantity,total)
                insert(q)
            q="update ordermaster set total_amount=total_amount+'%s' where ordermaster_id='%s'"%(total,oid)
            update(q)
            flash("Successfully added to Cart")
            return redirect(url_for("customer.customerviewitems"))
    return render_template("customeraddtocart.html",item=item,amount=amount,data=data)




@customer.route("/customerviewcart",methods=['get','post'])
def customerviewcart():
    data={}
    total=""
    omid=""
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    count=select(q)
    data['count']=len(count)
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    res=select(q)
    # print(len(res))
    data['val']=len(res)

    for i in range(1,len(res)+1):
        if 'del'+str(i) in request.form:
            product_id=request.form['pid'+str(i)]
            total_single_price=request.form['singletotal'+str(i)]
            omid=request.form['om_id']

            q="delete from orderdetails where ordermaster_id='%s' and product_id='%s' "%(omid,product_id)
            delete(q)
            q="update ordermaster set total_amount=total_amount-'%s' where ordermaster_id='%s'"%(total_single_price,omid)
            update(q)
            q=" select * from ordermaster where ordermaster_id='%s' and total_amount='0'"%(omid)
            ves=select(q)
            if ves:
                q="delete from ordermaster where ordermaster_id='%s'"%(omid)
                delete(q)
            
            return redirect(url_for("customer.customerviewcart"))


    
    data['res']=res
    if 'btncheckout' in request.form:
        
        q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
        res77=select(q)
        # q="select * from rawmaterials where "
        flag=0
        for i in res77:
            print(i['product_id'])
            qt = int(i['quantity'])
            pids=i['product_id']
            q="select raw_mat_id as raw_mat_id from product where product_id='%s'"%(pids)
            print(q)
            qw11=select(q)
            for j in qw11:
                raws=j['raw_mat_id']
                q="select quantity as quantity from rawmaterials where raw_mat_id='%s'"%(raws)
                mes=select(q)
                for w in mes:
                    rawqtys=int(w['quantity'])
                    print("....................",rawqtys)
                    if qt*3 > rawqtys or qt*2 > rawqtys or qt*1 > rawqtys:
                        flag=1
                        break
                    else:
                        flag=0
            
        if flag == 1:
            flash("Cant Proceed! Rawquantity out of Stock")
            return redirect(url_for("customer.customerviewcart"))
        else:
            total=request.form['total']
            print("ssssssssssssssssssssssssssssssss"+total)
            omid=request.form['om_id']
            q="update ordermaster set order_status='checkout', total_amount='%s' where ordermaster_id='%s'"%(total,omid)
            update(q)
                    
            for i in range(1,len(res)+1):
            
                qty=request.form['qty'+str(i)]
                single_price=request.form['single'+str(i)]
                product_id=request.form['pid'+str(i)]
                total_single_price=request.form['singletotal'+str(i)]
                print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"+total)
            
                q="update orderdetails set quantity='%s', total_price='%s' where product_id='%s' and ordermaster_id='%s'"%(qty,total_single_price,product_id,omid)
                update(q)
            return redirect(url_for("customer.customerpayment",total=total,omid=omid))
    return render_template("customerviewcart.html",data=data)



@customer.route("/customerpayment",methods=['get','post'])
def customerpayment():
    data={}
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    count=select(q)
    data['count']=len(count)
    total=request.args['total']
    omid=request.args['omid']

    if 'btn' in request.form:
        q="insert into payment values(null,'%s','booking','%s',curdate())"%(omid,total)
        insert(q)
        q="select * from ordermaster inner join orderdetails using(ordermaster_id) where ordermaster_id='%s'"%(omid)
        res=select(q)
                
        for i in res:
            print(i['product_id'])
            
            
            
            
        
        q="select *,orderdetails.quantity as quantity from ordermaster inner join orderdetails using(ordermaster_id) inner join product using (product_id) inner join rawmaterials using (raw_mat_id) where ordermaster_id='%s'"%(omid)	
        result=select(q)
        if result:
            for i in result:
                raw_id=i['raw_mat_id']
                qt = int(i['quantity'])      
                q="select * from product inner join subcategory using (subcategory_id) where product_id='%s'" %(i['product_id'])
                res1=select(q)
                for x in res1:
                    if x['subcategory_name'] == 'Non-veg (L)' or x['subcategory_name'] == 'Veg (L)':
                        qty=3*qt
                    if x['subcategory_name'] == 'Non-veg (M)' or x['subcategory_name'] == 'Veg (M)':
                        qty=2*qt
                    if x['subcategory_name'] == 'Non-veg (S)' or x['subcategory_name'] == 'Veg (S)':
                        qty=1*qt
                        
                q="update rawmaterials set quantity=quantity-'%s'where raw_mat_id='%s'"%(qty,raw_id)
                update(q)
                    
           
                q="select * from rawmaterials where raw_mat_id='%s' and quantity='0'"%(raw_id)
                
                res5=select(q)
                if res5:
                    q="select * from purchasechild where raw_mat_id ='%s' and pc_status='available' order by purchasechild_id desc"%(raw_id)
                    print(q)
                    res=select(q)
                    if res:
                        pdid=res[0]['purchasechild_id']
                        quan=res[0]['quantity']
                        sellp=res[0]['selling_price']
                        q="update rawmaterials set r_price='%s', quantity='%s' where raw_mat_id='%s'"%(sellp,quan,raw_id)
                        print(q)
                        update(q)
                        q="update purchasechild set pc_status='stock added' where purchasechild_id='%s'"%(pdid)
                        update(q)
                        
                        q="select * from product inner join rawmaterials using (raw_mat_id) where raw_mat_id='%s'"%(raw_id)
                        valley=select(q)
                        for z in valley:
                            sum=z['labour_cost']
                            rprice=z['r_price']
                            tot=int(float(sum)) + int(float(rprice))
                            q="update product set product_price='%s' where raw_mat_id='%s'"%(tot,raw_id)
                            update(q)
                    else:
                        a=5
                else:
                    b=4 
        # return redirect(url_for("customer.cust_home"))
        flash("Order placed Successfully")
        return redirect(url_for("customer.customerhome"))
    
    
    return render_template("customerpayment.html",data=data,total=total)


@customer.route("/customersingleproduct",methods=['get','post'])
def customersingleproduct():
    data={}
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    count=select(q)
    data['count']=len(count)
    pid=request.args['pid']

    q="SELECT * FROM product,`subcategory`, `category` WHERE `product`.`subcategory_id`=`subcategory`.`subcategory_id` AND `subcategory`.`category_id`=`category`.`category_id` and  product_id='%s'"%(pid)
    data['res']=select(q)
    return render_template("customersingleproduct.html",data=data)



@customer.route("/customervieworders",methods=['get','post'])
def customervieworders():
    data={}
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    count=select(q)
    data['count']=len(count)
    cid=session['cid']

    q="SELECT * FROM `ordermaster`, `orderdetails`, `product` WHERE `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` AND `orderdetails`.`product_id`=`product`.`product_id` AND  customer_id='%s' ORDER BY ordermaster.ordermaster_id DESC"%(cid)
    data['res']=select(q)
    return render_template("customervieworders.html",data=data)


@customer.route("/customercomplaints",methods=['get','post'])
def customercomplaints():
    data={}
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    count=select(q)
    data['count']=len(count)
    cid=session['cid']

    if 'btn' in request.form:
        comp=request.form['comp']

        q="insert into complaint values(NULL,'%s','%s','pending',curdate())"%(cid,comp)
        print(q)
        insert(q)
        return redirect(url_for("customer.customercomplaints"))
    
    q="select * from complaint where customer_id='%s'"%(cid)
    data['res']=select(q)
    return render_template("customercomplaints.html",data=data)



@customer.route("/customeraddtoppings",methods=['get','post'])
def customeraddtoppings():
    data={}
    od_id=request.args['od_id']
    q="select * from `ordermaster`,`orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    count=select(q)
    data['count']=len(count)
    cid=session['cid']

    
    q="""SELECT topping_id,topping_status,topping_name,topping_price,topping_desc,topping_status,topping_booked.`topping_quantity` AS qty FROM topping INNER JOIN topping_booked USING (topping_id) WHERE orderdetails_id='%s' and topping_status='active'
        UNION 
        SELECT topping_id,topping_status,topping_name,topping_price,topping_desc,topping_status,0 AS qty FROM topping WHERE topping_id not in (SELECT topping_id FROM topping_booked WHERE orderdetails_id='%s') and topping_status='active' order by topping_id"""%(od_id,od_id)
    res=select(q)
    data['res']=res

    # q="select * from "

    for i in range(1,len(res)+1):
        if 'qtyadd'+str(i) in request.form:
            qty=request.form['qty'+str(i)]
            topid=request.form['topid'+str(i)]
            print(topid)

            q="select topping_price from topping where topping_id='%s'"%(topid)
            print(q)
            topamount=select(q)
            top=int(topamount[0]['topping_price'])
            print("ssssssssssssssssssssssssssssssssssssssssssssss",top)
            total=int(topamount[0]['topping_price'])*int(qty)

            q="select * from topping_booked where orderdetails_id='%s' and topping_id='%s'"%(od_id,topid)
            val=select(q)
            if val:
                q="update topping_booked set topping_quantity=topping_quantity+'1', total='%s' where orderdetails_id='%s' and topping_id='%s' "%(total,od_id,topid)
                update(q)
            else:
                q="insert into topping_booked values(null,'%s','%s',1,'%s')"%(od_id,topid,total)
                insert(q)
            q="update orderdetails set total_price=total_price+'%s' where orderdetails_id='%s' "%(top,od_id)
            update(q)
            q="update ordermaster set total_amount=total_amount+'%s' where ordermaster_id=(select ordermaster_id from orderdetails where orderdetails_id='%s') "%(top,od_id)
            update(q)
            return redirect(url_for("customer.customeraddtoppings",od_id=od_id))
    
    
    for i in range(1,len(res)+1):
        if 'qtydec'+str(i) in request.form:
            qty=request.form['qty'+str(i)]
            topid=request.form['topid'+str(i)]

            q="select topping_price from topping where topping_id='%s'"%(topid)
            topamount=select(q)
            top=int(topamount[0]['topping_price'])
            print("ssssssssssssssssssssssssssssssssssssssssssssss",qty)
            total=int(topamount[0]['topping_price'])*int(qty)

            if int(qty) == 0:
                print("quantity is already Zero")
            else:
                q="select * from topping_booked where orderdetails_id='%s' and topping_id='%s'"%(od_id,topid)
                val=select(q)
                if val:
                    q="update topping_booked set topping_quantity=topping_quantity-'1', total='%s' where orderdetails_id='%s' and topping_id='%s' "%(total,od_id,topid)
                    update(q)
                else:
                    q="insert into topping_booked values(null,'%s','%s','%s','%s')"%(od_id,topid,qty,total)
                    insert(q)
                q="update orderdetails set total_price=total_price-'%s' where orderdetails_id='%s' "%(top,od_id)
                update(q)
                q="update ordermaster set total_amount=total_amount-'%s' where ordermaster_id=(select ordermaster_id from orderdetails where orderdetails_id='%s') "%(top,od_id)
                update(q)
            return redirect(url_for("customer.customeraddtoppings",od_id=od_id))
    return render_template("customeraddtoppings.html",data=data)



@customer.route("/customertoppingpayment",methods=['get','post'])
def customertoppingpayment():
    data={}
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    count=select(q)
    data['count']=len(count)
    total=request.args['amount']
    tid=request.args['tid']

    if 'btn' in request.form:
        q="insert into payment values(null,'%s','topping','%s',curdate())"%(tid,total)
        insert(q)
        q="update topping set topping_status='Payment Completed' where topping_id='%s'"%(tid)
        update(q)
        flash("Payment Successfull")
        return redirect(url_for("customer.customerhome"))
    return render_template("customertoppingpayment.html",data=data,total=total)


@customer.route("/countforcart",methods=['get','post'])
def countforcart():
    data={}
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    count=select(q)
    data['count']=len(count)
    return render_template("customerheader.html",data=data)

@customer.route('/bill')    
def bill():
  data={}
  oid=request.args['oid']
  q="SELECT * FROM `ordermaster`,`orderdetails`,`product` WHERE `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` AND `orderdetails`.product_id=`product`.`product_id` and ordermaster.customer_id='%s' and ordermaster.ordermaster_id='%s'"%(session['cid'],oid)
  data['res']=select(q)
  return render_template('bill.html',data=data)

# @customer.route('/customer_profile')    
# def customer_profile():
    
#     return render_template('customer_profile.html')