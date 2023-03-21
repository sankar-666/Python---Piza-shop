/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - pizashop
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
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`,`category_desc`,`status`) values 
(1,'Large','Large Pizza','active'),
(2,'Medium','Medium Pizza','active'),
(3,'Small','Small Pizza','active');

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

insert  into `complaint`(`complaint_id`,`customer_id`,`complaint`,`reply`,`date`) values 
(1,1,'worst piza ever','ok daa','2023-01-02');

/*Table structure for table `courier` */

DROP TABLE IF EXISTS `courier`;

CREATE TABLE `courier` (
  `courier_id` int(11) NOT NULL AUTO_INCREMENT,
  `courier_status` varchar(100) DEFAULT NULL,
  `license_no` varchar(100) DEFAULT NULL,
  `license_exp` varchar(100) DEFAULT NULL,
  `insurance_no` varchar(100) DEFAULT NULL,
  `insurance_exp` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`courier_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `courier` */

insert  into `courier`(`courier_id`,`courier_status`,`license_no`,`license_exp`,`insurance_no`,`insurance_exp`) values 
(1,'active',NULL,NULL,NULL,NULL),
(2,'active',NULL,NULL,NULL,NULL);

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

insert  into `customer`(`customer_id`,`username`,`customer_fname`,`customer_lname`,`customer_housename`,`customer_street`,`customer_city`,`customer_dist`,`customer_pincode`,`customer_phone`,`customer_dob`,`customer_gender`,`customer_status`) values 
(1,'sivanand@gmail.com','Sivanand','M Prabhu','Karthika','Jawahar Road','Tripunithura','Ernakulam','682034','9874512356','2002-06-12','Male','active'),
(2,'roshan@gmail.com','Roshan','Francis','Muttath','Kodikuthmala','Angamaly','Ernakulam','690503','7845214566','2001-10-13','male','active');

/*Table structure for table `delivery` */

DROP TABLE IF EXISTS `delivery`;

CREATE TABLE `delivery` (
  `delivery_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `courier_id` int(11) DEFAULT NULL,
  `delivery_date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`delivery_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `delivery` */

insert  into `delivery`(`delivery_id`,`ordermaster_id`,`courier_id`,`delivery_date`,`status`) values 
(1,1,3,'2023-03-01','Delivery Completed'),
(2,2,2,'2023-03-01','Delivery Completed'),
(3,3,2,'2023-03-01','Delivery Completed'),
(4,4,3,'2023-03-03','Delivery Completed'),
(5,5,2,'2023-03-04','Delivery Completed'),
(6,6,2,'2023-03-04','Delivery Completed'),
(7,7,4,'2023-03-04','Delivery Completed'),
(8,10,2,'2023-03-10','Delivery Completed'),
(9,8,2,'2023-03-10','Delivery Completed'),
(10,11,2,'2023-03-13','Delivery Completed'),
(11,12,2,'2023-03-13','Delivery Completed'),
(12,13,5,'2023-03-13','Delivery Completed'),
(13,14,2,'2023-03-14','pending');

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

insert  into `login`(`username`,`password`,`usertype`,`status`) values 
('admin@gmail.com','Admin123','admin','active'),
('aswin@gmail.com','Aswin123','staff','active'),
('roshan@gmail.com','Roshan123','customer','active'),
('devika@gmail.com','Devika123','staff','active'),
('aben@gmail.com','Aben1234','staff','active'),
('varkey@gmail.com','Varkey123','staff','active'),
('sivanand@gmail.com','Sivanand123','customer','active'),
('merin@gmail.com','Mer12345','staff','active');

/*Table structure for table `orderdetails` */

DROP TABLE IF EXISTS `orderdetails`;

CREATE TABLE `orderdetails` (
  `orderdetails_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `total_price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`orderdetails_id`)
) ENGINE=MyISAM AUTO_INCREMENT=50 DEFAULT CHARSET=latin1;

/*Data for the table `orderdetails` */

insert  into `orderdetails`(`orderdetails_id`,`ordermaster_id`,`product_id`,`quantity`,`total_price`) values 
(49,46,12,'1','215'),
(48,45,9,'3','651'),
(47,45,10,'1','217'),
(46,44,9,'3','1002');

/*Table structure for table `ordermaster` */

DROP TABLE IF EXISTS `ordermaster`;

CREATE TABLE `ordermaster` (
  `ordermaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `total_amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `order_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ordermaster_id`)
) ENGINE=MyISAM AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;

/*Data for the table `ordermaster` */

insert  into `ordermaster`(`ordermaster_id`,`customer_id`,`total_amount`,`date`,`order_status`) values 
(46,1,'215','2023-03-18','checkout'),
(45,1,'868','2023-03-18','checkout'),
(44,1,'1002','2023-03-18','checkout');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`ordermaster_id`,`type`,`amount`,`date`) values 
(1,1,'booking','848','2023-02-28'),
(2,2,'booking','641','2023-03-01'),
(3,3,'booking','621','2023-03-01'),
(4,4,'booking','976','2023-03-03'),
(5,5,'booking','1660','2023-03-04'),
(6,6,'booking','1016','2023-03-04'),
(7,6,'booking','1016','2023-03-04'),
(8,7,'booking','332','2023-03-04'),
(9,8,'booking','1006','2023-03-10'),
(10,8,'booking','1006','2023-03-10'),
(11,8,'booking','1006','2023-03-10'),
(12,8,'booking','1006','2023-03-10'),
(13,10,'booking','1670','2023-03-10'),
(14,11,'booking','4140','2023-03-13'),
(15,12,'booking','1710','2023-03-13'),
(16,13,'booking','424','2023-03-13'),
(17,14,'booking','1348','2023-03-14'),
(18,15,'booking','684','2023-03-15'),
(19,16,'booking','4761','2023-03-15'),
(20,20,'booking','621','2023-03-17'),
(21,37,'booking','830','2023-03-18'),
(22,38,'booking','8300','2023-03-18'),
(23,38,'booking','8300','2023-03-18'),
(24,39,'booking','1012','2023-03-18'),
(25,40,'booking','1002','2023-03-18'),
(26,41,'booking','1002','2023-03-18'),
(27,42,'booking','1336','2023-03-18'),
(28,43,'booking','1002','2023-03-18'),
(29,43,'booking','1002','2023-03-18'),
(30,43,'booking','1002','2023-03-18'),
(31,44,'booking','1002','2023-03-18'),
(32,45,'booking','868','2023-03-18'),
(33,46,'booking','215','2023-03-18');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `raw_mat_id` int(11) DEFAULT NULL,
  `subcategory_id` int(11) DEFAULT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `product_desc` varchar(100) DEFAULT NULL,
  `product_image` varchar(100) DEFAULT NULL,
  `product_price` varchar(100) DEFAULT NULL,
  `labour_cost` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`raw_mat_id`,`subcategory_id`,`product_name`,`product_desc`,`product_image`,`product_price`,`labour_cost`,`status`) values 
(12,5,4,'dasd','dasd','static/uploads/0eaeb02d-e3ac-439a-8160-ebe9d331d820blog1.jpg','111','100','active'),
(11,6,3,'kllll','jlkn','static/uploads/cc3f7f03-3201-4f77-86dc-a810d5bcdd15blog1.jpg','217','100','active'),
(9,6,1,'abc pizza','abc pizza','static/uploads/2878d2ec-9c39-4f8a-b836-fed7adb4cbaaab2.jpg','217','100','active'),
(10,6,3,'nqwd','mfmlksmd','static/uploads/0e36730d-a871-42a9-b4db-e91ade2e712ablog2.jpg','217','100','active');

/*Table structure for table `purchasechild` */

DROP TABLE IF EXISTS `purchasechild`;

CREATE TABLE `purchasechild` (
  `purchasechild_id` int(11) NOT NULL AUTO_INCREMENT,
  `purchasemaster_id` int(11) DEFAULT NULL,
  `raw_mat_id` int(11) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `selling_price` varchar(100) DEFAULT NULL,
  `pc_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`purchasechild_id`)
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

/*Data for the table `purchasechild` */

insert  into `purchasechild`(`purchasechild_id`,`purchasemaster_id`,`raw_mat_id`,`price`,`quantity`,`selling_price`,`pc_status`) values 
(40,31,5,'10','33','11.5','stock added'),
(39,31,6,'100','10','117.0','stock added');

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
) ENGINE=MyISAM AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

/*Data for the table `purchasemaster` */

insert  into `purchasemaster`(`purchasemaster_id`,`vendor_id`,`staff_id`,`total`,`status`,`date_added`) values 
(31,2,0,'1330','purchase completed','2023-03-18');

/*Table structure for table `rawmaterials` */

DROP TABLE IF EXISTS `rawmaterials`;

CREATE TABLE `rawmaterials` (
  `raw_mat_id` int(11) NOT NULL AUTO_INCREMENT,
  `vendor_id` int(11) DEFAULT NULL,
  `raw_mat` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `prof` varchar(100) DEFAULT NULL,
  `r_price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`raw_mat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `rawmaterials` */

insert  into `rawmaterials`(`raw_mat_id`,`vendor_id`,`raw_mat`,`quantity`,`prof`,`r_price`) values 
(6,1,'Non Vegetable Raw Materials','0','17','117.0'),
(5,1,'Vegetable Raw Materials','33','15','11.5');

/*Table structure for table `rawmaterialused` */

DROP TABLE IF EXISTS `rawmaterialused`;

CREATE TABLE `rawmaterialused` (
  `rawmaterialused_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `raw_mat_id` int(11) DEFAULT NULL,
  `qty` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rawmaterialused_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `rawmaterialused` */

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
  `staff_pincode` varchar(100) DEFAULT NULL,
  `staff_phone` varchar(100) DEFAULT NULL,
  `staff_gender` varchar(100) DEFAULT NULL,
  `staff_dob` varchar(100) DEFAULT NULL,
  `staff_join` varchar(100) DEFAULT NULL,
  `license_number` varchar(100) DEFAULT NULL,
  `license_expiry` varchar(100) DEFAULT NULL,
  `insurance_number` varchar(100) DEFAULT NULL,
  `insurance_expiry` varchar(100) DEFAULT NULL,
  `staff_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`staff_fname`,`staff_lname`,`staff_desig`,`staff_street`,`staff_city`,`staff_dist`,`staff_pincode`,`staff_phone`,`staff_gender`,`staff_dob`,`staff_join`,`license_number`,`license_expiry`,`insurance_number`,`insurance_expiry`,`staff_status`) values 
(1,'merin@gmail.com','Merin','Varghese','Worker','Cross Street','Angamaly','Ernakulam','682023','9898653224','Female','2002-07-20','2023-02-28','KLNO987456321','2026-07-10','789456','2030-06-10','active'),
(2,'varkey@gmail.com','Varkey','Mathan','Delivery Boy','Church Nagar','Angamaly','Ernakulam','685968','8745125364','Male','2001-12-05','2023-03-01','KLNO987456321','2026-07-10','789456','2030-06-10','active'),
(3,'aben@gmail.com','Aben','Reji','Delivery Boy','A P Varkey Road','Thiruvankulam','Ernakulam','685214','9865874125','Male','2002-02-01','2023-03-01','KLNO987456321','2026-07-10','789456','2030-06-10','active'),
(4,'devika@gmail.com','Devika','Sreenivas','Delivery Boy','ABC street','Padivattom','Ernakulam','685124','9856745812','Female','2002-07-22','2023-03-01','KLNO134679258','2026-07-25','852963','2026-08-20','active'),
(5,'aswin@gmail.com','Aswin','Sadhan','Delivery Boy','abc ','Kalamassery','Ernakulam','685441','9856742145','Male','2002-07-12','2023-03-13','KLNO123456789','11-06-2023','456123','2026-08-16','active');

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
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `subcategory` */

insert  into `subcategory`(`subcategory_id`,`category_id`,`subcategory_name`,`subcategory_desc`,`status`) values 
(1,1,'Non-veg (L)','Large Non-veg Pizza','active'),
(2,2,'Non-veg (M)','Medium Non-veg Pizza','active'),
(3,3,'Non-veg (S)','Small Non-veg Pizza','active'),
(4,1,'Veg (L)','Large Veg Pizza','active'),
(5,2,'Veg (M)','Medium Veg Pizza','active'),
(6,3,'Veg (S)','Small Veg Pizza','active');

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

insert  into `topping`(`topping_id`,`topping_name`,`topping_price`,`topping_desc`,`topping_status`) values 
(1,'Cheese','10','Cheese Topping','active'),
(2,'Fried Chicken','20','Fried Chicken toppings','active');

/*Table structure for table `topping_booked` */

DROP TABLE IF EXISTS `topping_booked`;

CREATE TABLE `topping_booked` (
  `toppingbooked_id` int(11) NOT NULL AUTO_INCREMENT,
  `orderdetails_id` int(11) DEFAULT NULL,
  `topping_id` int(11) DEFAULT NULL,
  `topping_quantity` varchar(100) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`toppingbooked_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `topping_booked` */

insert  into `topping_booked`(`toppingbooked_id`,`orderdetails_id`,`topping_id`,`topping_quantity`,`total`) values 
(7,41,1,'1','0');

/*Table structure for table `vendor` */

DROP TABLE IF EXISTS `vendor`;

CREATE TABLE `vendor` (
  `vendor_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `vendor_name` varchar(100) DEFAULT NULL,
  `vendor_godown_num` varchar(100) DEFAULT NULL,
  `vendor_city` varchar(100) DEFAULT NULL,
  `vendor_dist` varchar(100) DEFAULT NULL,
  `vendor_pincode` varchar(100) DEFAULT NULL,
  `vendor_phone` varchar(100) DEFAULT NULL,
  `vendor_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `vendor` */

insert  into `vendor`(`vendor_id`,`staff_id`,`vendor_name`,`vendor_godown_num`,`vendor_city`,`vendor_dist`,`vendor_pincode`,`vendor_phone`,`vendor_status`) values 
(1,0,'Roshan','Roshan Gno1','Aluva','Ernakulam','685126','8956214573','active'),
(2,0,'Akhil','Akhil Gno2','Thripunithura','Ernakulam','682309','9565214588','active');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
