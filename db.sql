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
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`,`category_desc`,`status`) values (1,'aaa aaaa','come go','inactive'),(2,'pt','come and gosh','inactive');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

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

insert  into `courier`(`courier_id`,`username`,`courier_fname`,`courier_lname`,`courier_desig`,`courier_street`,`courier_city`,`courier_dist`,`courier_state`,`courier_pincode`,`courier_phone`,`courier_gender`,`courier_dob`,`courier_join`,`courier_status`) values (1,'sankusanku001@gmail.com','ss','ssss','ssssss','sssss','sssssssssss','ssssssssss','sssssssss','222222','3333333333','female','2025-02-28','2022-12-28','inactive');

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
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

/*Table structure for table `delivery` */

DROP TABLE IF EXISTS `delivery`;

CREATE TABLE `delivery` (
  `delivery_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `courier_id` int(11) DEFAULT NULL,
  `delivery_date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`delivery_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `delivery` */

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

insert  into `login`(`username`,`password`,`usertype`,`status`) values ('admin@gmail.com','admin','admin','active'),('staff@gmail.com','staff','staff','inactive'),('sankusanku001@gmail.com','dsasdad','courier','inactive');

/*Table structure for table `orderdetails` */

DROP TABLE IF EXISTS `orderdetails`;

CREATE TABLE `orderdetails` (
  `orderdetails_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  `total_price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`orderdetails_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `orderdetails` */

/*Table structure for table `ordermaster` */

DROP TABLE IF EXISTS `ordermaster`;

CREATE TABLE `ordermaster` (
  `ordermaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `total_amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `order_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ordermaster_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `ordermaster` */

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `ordermaster_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

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
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`subcategory_id`,`product_name`,`product_desc`,`product_image`,`product_price`,`status`) values (1,2,'sdasd','asdasd','static/uploads/2b1f073a-5f32-46f6-b9b8-0a25f22f9184blackmain.jpg','111111111111111','active'),(2,1,'donut','fun and chill','static/uploads/5db1d710-a21d-4e0b-928d-5cc81fefde5dbookair.png','40','inactive');

/*Table structure for table `purchasechild` */

DROP TABLE IF EXISTS `purchasechild`;

CREATE TABLE `purchasechild` (
  `prurchasechild_id` int(11) NOT NULL AUTO_INCREMENT,
  `purchasemaster_id` int(11) DEFAULT NULL,
  `raw_mat_id` int(11) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`prurchasechild_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `purchasechild` */

insert  into `purchasechild`(`prurchasechild_id`,`purchasemaster_id`,`raw_mat_id`,`price`,`quantity`) values (4,3,7,'10','2');

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
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `purchasemaster` */

insert  into `purchasemaster`(`purchasemaster_id`,`vendor_id`,`staff_id`,`total`,`status`,`date_added`) values (3,1,0,'10','pending','2022-12-28');

/*Table structure for table `raswmaterialused` */

DROP TABLE IF EXISTS `raswmaterialused`;

CREATE TABLE `raswmaterialused` (
  `rawmaterialuser_id` int(11) NOT NULL,
  `ordermaster_id` int(11) DEFAULT NULL,
  `raw_mat_id` int(11) DEFAULT NULL,
  `qty` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rawmaterialuser_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `raswmaterialused` */

/*Table structure for table `rawmaterials` */

DROP TABLE IF EXISTS `rawmaterials`;

CREATE TABLE `rawmaterials` (
  `raw_mat_id` int(11) NOT NULL AUTO_INCREMENT,
  `vendor_id` int(11) DEFAULT NULL,
  `raw_mat` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`raw_mat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `rawmaterials` */

insert  into `rawmaterials`(`raw_mat_id`,`vendor_id`,`raw_mat`,`quantity`) values (7,1,'Sweets','4');

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

insert  into `staff`(`staff_id`,`username`,`staff_fname`,`staff_lname`,`staff_desig`,`staff_street`,`staff_city`,`staff_dist`,`staff_state`,`staff_pincode`,`staff_phone`,`staff_gender`,`staff_dob`,`staff_join`,`staff_status`) values (1,'staff@gmail.com','aaaa','aa','sdsa','aaaaaa','aaaa','alpyaaa','aaaa','aaaa','aaaaa','male','2023-01-15','2022-12-27','inactive');

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

insert  into `subcategory`(`subcategory_id`,`category_id`,`subcategory_name`,`subcategory_desc`,`status`) values (1,1,'John Hona','come and goh','inactive'),(2,1,'pppppppp','sdsa','inactive'),(3,2,'John Hona','sdas','active');

/*Table structure for table `topping` */

DROP TABLE IF EXISTS `topping`;

CREATE TABLE `topping` (
  `topping_id` int(11) NOT NULL AUTO_INCREMENT,
  `topping_name` varchar(100) DEFAULT NULL,
  `topping_price` varchar(100) DEFAULT NULL,
  `topping_desc` varchar(100) DEFAULT NULL,
  `topping_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`topping_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `topping` */

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

insert  into `vendor`(`vendor_id`,`staff_id`,`vendor_email`,`vendor_name`,`vendor_godown_num`,`vendor_street`,`vendor_city`,`vendor_dist`,`vendor_pincode`,`vendor_phone`,`vendor_status`) values (1,0,'sankusanku001@gmail.com','ssss','sssssssss','sssssss','sssssss','sssssss','111111','2222222222','active');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
