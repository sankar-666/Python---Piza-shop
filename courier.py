from flask import *
from database import *

courier=Blueprint('courier',__name__)

@courier.route("/courierhome")
def courierhome():
    return render_template("courierhome.html")


def sweetAlert(c):
    return "<script>c</script>"

@courier.route("/courierviewallreq")
def courierviewallreq():
    data={}
    q="SELECT * FROM `ordermaster`, `orderdetails`, `customer`, `product`,delivery WHERE `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` AND `ordermaster`.`customer_id`=`customer`.`customer_id` AND `orderdetails`.`product_id`=`product`.`product_id` and ordermaster.ordermaster_id=delivery.ordermaster_id and delivery.courier_id='%s'"%(session['sid'])
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        omid=request.args['omid']
    else:
        action=None

    if action == "accept":
        q="insert into delivery values(null, '%s','%s',curdate(),'Accepted by Courier')"%(omid,session['sid'])
        insert(q)
        q="update ordermaster set order_status='Accepted by Courier' where ordermaster_id='%s'"%(omid)
        update(q)
        flash("Couier Accepted")
        # sweetAlert("Hello")
        return redirect(url_for("courier.courierhome"))
    return render_template("courierviewallreq.html",data=data)


@courier.route("/courierdelivery")
def courierdelivery():
    data={}
    q="SELECT * FROM `ordermaster`, `orderdetails`, `customer`, `product`, delivery WHERE `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` AND `ordermaster`.`customer_id`=`customer`.`customer_id` AND `orderdetails`.`product_id`=`product`.`product_id` and `ordermaster`.`ordermaster_id`=delivery.ordermaster_id and courier_id='%s' order by delivery_id desc"%(session['sid'])

    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        omid=request.args['omid']
        did=request.args['did']
    else:
        action=None

    if action == "accept":
        q="update delivery set status='Delivery Completed' where delivery_id='%s' "%(did)
        insert(q)
        q="update ordermaster set order_status='Delivery Completed' where ordermaster_id='%s'"%(omid)
        update(q)
        flash("Delivered Successfully")
        return redirect(url_for("courier.courierhome"))
    return render_template("courierdelivery.html",data=data)


