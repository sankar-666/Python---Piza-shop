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
        print(q)
    else:
        q="SELECT * FROM `product`, `subcategory`, `category` WHERE `product`.`subcategory_id`=`subcategory`.`subcategory_id` AND `subcategory`.`category_id`=`category`.`category_id` AND `product`.`status`='active' AND `category`.`status`='active' AND `subcategory`.`status`='active' group by product_id"
        print(q)
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




@customer.route("/customerviewcart")
def customerviewcart():
    data={}
    q="select * from `ordermaster`, `orderdetails`, `product` where `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` and `orderdetails`.`product_id`=`product`.`product_id` and  customer_id='%s'"%(session['cid'])
    data['res']=select(q)
    return render_template("customerviewcart.html",data=data)