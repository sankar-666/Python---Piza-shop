/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.3.20-MariaDB : Database - pizashop
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pizashop` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `pizashop`;

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  `category_desc` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`,`category_desc`,`status`) values (1,'bat','come goss','active'),(2,'this is our special dish maily for foreigners.','come and gosh','active'),(3,'cap','for style','active');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`customer_id`,`complaint`,`reply`,`date`) values (1,1,'worst piza ever','ok set','2023-01-02');

/*Table structure for table `courier` */

DROP TABLE IF EXISTS `courier`;

CREATE TABLE `courier` (
  `courier_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `courier_fname` varchar(100) DEFAULT NULL,
  `courier_lname` varchar(100) DEFAULT NULL,
  `courier_desig` varchar(100) DEFAULT NULL,
  `courier_street` varchar(100) DEFAULT NULL,
  `courier_city` varchar(100) DEFAULT NULL,
  `courier_dist` varchar(100) DEFAULT NULL,
  `courier_state` varchar(100) DEFAULT NULL,
  `courier_pincode` varchar(100) DEFAULT NULL,
  `courier_phone` varchar(100) DEFAULT NULL,
  `courier_gender` varchar(100) DEFAULT NULL,
  `courier_dob` varchar(100) DEFAULT NULL,
  `courier_join` varchar(100) DEFAULT NULL,
  `courier_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`courier_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `courier` */

insert  into `courier`(`courier_id`,`username`,`courier_fname`,`courier_lname`,`courier_desig`,`courier_street`,`courier_city`,`courier_dist`,`courier_state`,`courier_pincode`,`courier_phone`,`courier_gender`,`courier_dob`,`courier_join`,`courier_status`) values (1,'cor@gmail.com','ss','ssss','ssssss','sssss','sssssssssss','ssssssssss','sssssssss','222222','3333333333','female','2025-02-28','2022-12-28','active');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `customer_fname` varchar(100) DEFAULT NULL,
  `customer_lname` varchar(100) DEFAULT NULL,
  `customer_housename` varchar(100) DEFAULT NULL,
  `customer_street` varchar(100) DEFAULT NULL,
  `customer_city` varchar(100) DEFAULT NULL,
  `customer_dist` varchar(100) DEFAULT NULL,
  `customer_pincode` varchar(100) DEFAULT NULL,
  `customer_phone` varchar(100) DEFAULT NULL,
  `customer_dob` varchar(100) DEFAULT NULL,
  `customer_gender` varchar(100) DEFAULT NULL,
  `customer_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`username`,`customer_fname`,`customer_lname`,`customer_housename`,`customer_street`,`customer_city`,`customer_dist`,`customer_pincode`,`customer_phone`,`customer_dob`,`customer_gender`,`customer_status`) values (1,'cus@gmail.com','johny','john','kottakal','thuravoor','alappuzha','ernakulam','688523','9846354290','2022-12-17','male','active'),(2,'newcus@gmail.com','johny','john','kottakal','thuravoor','alappuzha','dsa','688523','9846354290','2023-01-21','male','active');

/*Table structure for table `delivery` */

DROP TABLE IF EXISTS `delivery`;

CREATE TABLE `delivery` (
  `delivery_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `courier_id` int(11) DEFAULT NULL,
  `delivery_date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`delivery_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `delivery` */

insert  into `delivery`(`delivery_id`,`ordermaster_id`,`courier_id`,`delivery_date`,`status`) values (1,24,1,'2023-01-02','Delivery Completed'),(3,19,1,'2023-01-02','Delivery Completed'),(4,20,1,'2023-01-02','Delivery Completed'),(5,24,1,'2023-01-02','Delivery Completed'),(6,23,1,'2023-01-02','Delivery Completed'),(7,22,1,'2023-01-02','Delivery Completed'),(8,20,1,'2023-01-02','Delivery Completed'),(9,19,1,'2023-01-02','Delivery Completed'),(10,22,1,'2023-01-02','Accepted by Courier');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`usertype`,`status`) values ('admin@gmail.com','Admin123','admin','active'),('staff@gmail.com','Staff123','staff','active'),('cor@gmail.com','cor','courier','active'),('cus@gmail.com','Cus123456','customer','active'),('newcus@gmail.com','Newcus123','customer','active');

/*Table structure for table `orderdetails` */

DROP TABLE IF EXISTS `orderdetails`;

CREATE TABLE `orderdetails` (
  `orderdetails_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `total_price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`orderdetails_id`)
) ENGINE=MyISAM AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;

/*Data for the table `orderdetails` */

insert  into `orderdetails`(`orderdetails_id`,`ordermaster_id`,`product_id`,`quantity`,`total_price`) values (54,37,2,'2','88'),(53,37,3,'2','80000'),(51,35,1,'2','88'),(52,36,1,'1','44');

/*Table structure for table `ordermaster` */

DROP TABLE IF EXISTS `ordermaster`;

CREATE TABLE `ordermaster` (
  `ordermaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `total_amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `order_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ordermaster_id`)
) ENGINE=MyISAM AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;

/*Data for the table `ordermaster` */

insert  into `ordermaster`(`ordermaster_id`,`customer_id`,`total_amount`,`date`,`order_status`) values (37,1,'80088','2023-01-04','pending'),(35,1,'88','2023-01-04','Dispatched'),(36,1,'44','2023-01-04','checkout');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`ordermaster_id`,`type`,`amount`,`date`) values (1,25,NULL,'500000','2023-01-02'),(2,1,'topping','not assigned','2023-01-02'),(3,1,'topping','not assigned','2023-01-02'),(4,1,'topping','500','2023-01-02'),(5,31,'booking','1600','2023-01-03'),(6,30,'booking','1600','2023-01-03'),(7,35,'booking','88','2023-01-04'),(8,36,'booking','44','2023-01-04');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcategory_id` int(11) DEFAULT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `product_desc` varchar(100) DEFAULT NULL,
  `product_image` varchar(100) DEFAULT NULL,
  `product_price` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`subcategory_id`,`product_name`,`product_desc`,`product_image`,`product_price`,`status`) values (1,2,'pizaa','pic of emotions','static/uploads/956e27db-fab7-41c3-b744-d453454217c51636385326712-01.jpeg','44','active'),(2,1,'donut','fun and chill','static/uploads/5db1d710-a21d-4e0b-928d-5cc81fefde5dbookair.png','44','active'),(3,3,'pizachi','for pleassure','static/uploads/0481ac5b-6bd7-4312-88e3-a2cfe5be9581bgc.jpg','40000','active');

/*Table structure for table `purchasechild` */

DROP TABLE IF EXISTS `purchasechild`;

CREATE TABLE `purchasechild` (
  `prurchasechild_id` int(11) NOT NULL AUTO_INCREMENT,
  `purchasemaster_id` int(11) DEFAULT NULL,
  `raw_mat_id` int(11) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`prurchasechild_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `purchasechild` */

insert  into `purchasechild`(`prurchasechild_id`,`purchasemaster_id`,`raw_mat_id`,`price`,`quantity`) values (5,3,9,'500','600'),(4,3,7,'10','2'),(6,3,8,'500','20'),(7,4,9,'50','800'),(8,5,8,'500','40'),(9,6,9,'10','1600');

/*Table structure for table `purchasemaster` */

DROP TABLE IF EXISTS `purchasemaster`;

CREATE TABLE `purchasemaster` (
  `purchasemaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `vendor_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `status` varbinary(100) DEFAULT NULL,
  `date_added` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`purchasemaster_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `purchasemaster` */

insert  into `purchasemaster`(`purchasemaster_id`,`vendor_id`,`staff_id`,`total`,`status`,`date_added`) values (3,1,0,'1020','purchase completed','2022-12-28'),(4,1,1,'50','purchase completed','2023-01-02'),(5,1,0,'500','purchase completed','2023-01-04'),(6,1,0,'10','pending','2023-01-04');

/*Table structure for table `rawmaterials` */

DROP TABLE IF EXISTS `rawmaterials`;

CREATE TABLE `rawmaterials` (
  `raw_mat_id` int(11) NOT NULL AUTO_INCREMENT,
  `vendor_id` int(11) DEFAULT NULL,
  `raw_mat` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`raw_mat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `rawmaterials` */

insert  into `rawmaterials`(`raw_mat_id`,`vendor_id`,`raw_mat`,`quantity`) values (9,1,'glucose','3200'),(8,1,'east','80'),(7,1,'Sweets','4');

/*Table structure for table `rawmaterialused` */

DROP TABLE IF EXISTS `rawmaterialused`;

CREATE TABLE `rawmaterialused` (
  `rawmaterialused_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `raw_mat_id` int(11) DEFAULT NULL,
  `qty` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rawmaterialused_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `rawmaterialused` */

insert  into `rawmaterialused`(`rawmaterialused_id`,`ordermaster_id`,`type`,`raw_mat_id`,`qty`) values (1,1,'topping',8,'40'),(2,23,'booking',9,'800');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `staff_fname` varchar(100) DEFAULT NULL,
  `staff_lname` varchar(100) DEFAULT NULL,
  `staff_desig` varchar(100) DEFAULT NULL,
  `staff_street` varchar(100) DEFAULT NULL,
  `staff_city` varchar(100) DEFAULT NULL,
  `staff_dist` varchar(100) DEFAULT NULL,
  `staff_state` varchar(100) DEFAULT NULL,
  `staff_pincode` varchar(100) DEFAULT NULL,
  `staff_phone` varchar(100) DEFAULT NULL,
  `staff_gender` varchar(100) DEFAULT NULL,
  `staff_dob` varchar(100) DEFAULT NULL,
  `staff_join` varchar(100) DEFAULT NULL,
  `staff_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`staff_fname`,`staff_lname`,`staff_desig`,`staff_street`,`staff_city`,`staff_dist`,`staff_state`,`staff_pincode`,`staff_phone`,`staff_gender`,`staff_dob`,`staff_join`,`staff_status`) values (1,'staff@gmail.com','aaaa','aa','sdsa','aaaaaa','aaaa','alpyaaa','aaaa','aaaa','aaaaa','other','2023-01-15','2022-12-27','active');

/*Table structure for table `stock` */

DROP TABLE IF EXISTS `stock`;

CREATE TABLE `stock` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `raw_mat_id` int(11) DEFAULT NULL,
  `qty` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `stock` */

/*Table structure for table `subcategory` */

DROP TABLE IF EXISTS `subcategory`;

CREATE TABLE `subcategory` (
  `subcategory_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `subcategory_name` varchar(100) DEFAULT NULL,
  `subcategory_desc` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`subcategory_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `subcategory` */

insert  into `subcategory`(`subcategory_id`,`category_id`,`subcategory_name`,`subcategory_desc`,`status`) values (1,1,'John Hona','come and goh','active'),(2,1,'pppppppp','sdsa','active'),(3,2,'len','str','active');

/*Table structure for table `topping` */

DROP TABLE IF EXISTS `topping`;

CREATE TABLE `topping` (
  `topping_id` int(11) NOT NULL AUTO_INCREMENT,
  `topping_name` varchar(100) DEFAULT NULL,
  `topping_price` varchar(100) DEFAULT NULL,
  `topping_desc` varchar(100) DEFAULT NULL,
  `topping_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`topping_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `topping` */

insert  into `topping`(`topping_id`,`topping_name`,`topping_price`,`topping_desc`,`topping_status`) values (1,'apple','250','have fun','active'),(2,'chery','10','chumma','active');

/*Table structure for table `topping_booked` */

DROP TABLE IF EXISTS `topping_booked`;

CREATE TABLE `topping_booked` (
  `toppingbooked_id` int(11) NOT NULL AUTO_INCREMENT,
  `orderdetails_id` int(11) DEFAULT NULL,
  `topping_id` int(11) DEFAULT NULL,
  `topping_quantity` varchar(100) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`toppingbooked_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `topping_booked` */

insert  into `topping_booked`(`toppingbooked_id`,`orderdetails_id`,`topping_id`,`topping_quantity`,`total`) values (1,54,1,'10','2750'),(2,54,2,'0','0'),(3,53,1,'9','2500'),(4,53,2,'0','0');

/*Table structure for table `vendor` */

DROP TABLE IF EXISTS `vendor`;

CREATE TABLE `vendor` (
  `vendor_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `vendor_email` varchar(100) DEFAULT NULL,
  `vendor_name` varchar(100) DEFAULT NULL,
  `vendor_godown_num` varchar(100) DEFAULT NULL,
  `vendor_street` varchar(100) DEFAULT NULL,
  `vendor_city` varchar(100) DEFAULT NULL,
  `vendor_dist` varchar(100) DEFAULT NULL,
  `vendor_pincode` varchar(100) DEFAULT NULL,
  `vendor_phone` varchar(100) DEFAULT NULL,
  `vendor_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `vendor` */

insert  into `vendor`(`vendor_id`,`staff_id`,`vendor_email`,`vendor_name`,`vendor_godown_num`,`vendor_street`,`vendor_city`,`vendor_dist`,`vendor_pincode`,`vendor_phone`,`vendor_status`) values (1,0,'sankusanku001@gmail.com','Arjun','Suresh','Alappuzha','Ernakulam','Kottayam','688523','6238526457','active');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
