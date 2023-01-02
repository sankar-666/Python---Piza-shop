from flask import *
from database import *

customer=Blueprint('customer',__name__)

@customer.route("/customerhome")
def customerhome():
    return render_template("customerhome.html")


@customer.route("/customerviewitems",methods=['get','post'])
def customerviewitems():
    data={}
    

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
    item=request.args['item']
    amount=request.args['amount']
    pid=request.args['pid']
    if 'btn' in request.form:
        quantity=request.form['quantity']
        total=request.form['total']

        q="select * from ordermaster where order_status='pending'"
        res=select(q)
        if res:
            oid=res[0]['ordermaster_id']
        else:
            q="insert into ordermaster values(null,'%s',0,curdate(),'pending')"%(session['cid'])
            oid=insert(q)
        q="select * from orderdetails where product_id='%s' and ordermaster_id='%s'"%(pid,oid)
        val=select(q)
        if val:
            q="update orderdetails set quantity=quantity+'%s', total_price=total_price+'%s' "%(quantity,total)
            update(q)
        else:
            q="insert into orderdetails values (null,'%s','%s','%s','%s')"%(oid,pid,quantity,total)
            insert(q)
        q="update ordermaster set total_amount=total_amount+'%s' where ordermaster_id='%s'"%(total,oid)
        update(q)
        flash("Successfully added to Cart")
        return redirect(url_for("customer.customerviewitems"))
    return render_template("customeraddtocart.html",item=item,amount=amount)




@customer.route("/customerviewcart",methods=['get','post'])
def customerviewcart():
    data={}
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s' and order_status='pending'"%(session['cid'])
    res=select(q)
    # print(len(res))
    data['val']=len(res)
    
    data['res']=res

    # if 'action' in request.args:
    #     action=request.args['action']
    #     omid=request.args['omid']
    # else:
    #     action=None
    # if action == "checkout":
    if 'btncheckout' in request.form:
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
    total=request.args['total']
    omid=request.args['omid']

    if 'btn' in request.form:
        q="insert into payment values(null,'%s','%s',curdate())"%(omid,total)
        insert(q)
        flash("Order placed Successfully")
        return redirect(url_for("customer.customerhome"))
    return render_template("customerpayment.html",data=data,total=total)


@customer.route("/customersingleproduct",methods=['get','post'])
def customersingleproduct():
    data={}
    pid=request.args['pid']

    q="SELECT * FROM product,`subcategory`, `category` WHERE `product`.`subcategory_id`=`subcategory`.`subcategory_id` AND `subcategory`.`category_id`=`category`.`category_id` and  product_id='%s'"%(pid)
    data['res']=select(q)
    return render_template("customersingleproduct.html",data=data)



@customer.route("/customervieworders",methods=['get','post'])
def customervieworders():
    data={}
    cid=session['cid']

    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s'"%(cid)
    data['res']=select(q)
    return render_template("customervieworders.html",data=data)


@customer.route("/customercomplaints",methods=['get','post'])
def customercomplaints():
    data={}
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