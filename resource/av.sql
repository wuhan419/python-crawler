/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.5.9 : Database - avdb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`avdb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `avdb`;

/*Table structure for table `av_info_main` */

DROP TABLE IF EXISTS `av_info_main`;

CREATE TABLE `av_info_main` (
  `video_id` varchar(20) DEFAULT NULL,
  `video_name` varchar(300) DEFAULT NULL,
  `video_src` varchar(100) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `maker` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `av_info_main` */

/*Table structure for table `av_tag` */

DROP TABLE IF EXISTS `av_tag`;

CREATE TABLE `av_tag` (
  `video_id` varchar(100) DEFAULT NULL,
  `video_tag` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `av_tag` */

/*Table structure for table `href_list` */

DROP TABLE IF EXISTS `href_list`;

CREATE TABLE `href_list` (
  `title` varchar(200) DEFAULT NULL,
  `href` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `href_list` */

/*Table structure for table `video_cast` */

DROP TABLE IF EXISTS `video_cast`;

CREATE TABLE `video_cast` (
  `video_id` varchar(20) DEFAULT NULL,
  `actor` varchar(100) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `video_cast` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
