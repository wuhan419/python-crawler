SET NAMES utf8;
CREATE DATABASE avdb  DEFAULT CHARACTER SET utf8;

USE avdb;


DROP TABLE IF EXISTS av_info_main;

CREATE TABLE av_info_main (
  video_id varchar(20) DEFAULT NULL,
  video_name varchar(300) DEFAULT NULL,
  video_src varchar(100) DEFAULT NULL,
  img varchar(255) DEFAULT NULL,
  maker varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



DROP TABLE IF EXISTS av_tag;

CREATE TABLE av_tag (
  video_id varchar(100) DEFAULT NULL,
  video_tag varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



DROP TABLE IF EXISTS href_list;

CREATE TABLE href_list (
  title varchar(200) DEFAULT NULL,
  href varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



DROP TABLE IF EXISTS video_cast;

CREATE TABLE video_cast (
  video_id varchar(20) DEFAULT NULL,
  actor varchar(100) DEFAULT NULL,
  url varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


