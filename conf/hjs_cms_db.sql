-- Adminer 4.2.1 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `tb_custom`;
CREATE TABLE `tb_custom` (
  `cid` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `ctype` enum('N','O') NOT NULL DEFAULT 'N',
  `class` varchar(10) DEFAULT 'A',
  `status` enum('normal','cancel','delete') NOT NULL DEFAULT 'normal',
  `remark` text,
  `insert_tm` datetime DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_order`;
CREATE TABLE `tb_order` (
  `oid` int(10) NOT NULL AUTO_INCREMENT,
  `cid` int(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `otype` varchar(10) NOT NULL DEFAULT 'A',
  `order_tm` datetime NOT NULL,
  `start_tm` date NOT NULL,
  `end_tm` date NOT NULL,
  `amount` float NOT NULL,
  `cash` float NOT NULL,
  `status` enum('normal','stop') NOT NULL DEFAULT 'normal',
  `remark` text NOT NULL,
  `insert_tm` datetime NOT NULL,
  PRIMARY KEY (`oid`),
  KEY `cid` (`cid`),
  CONSTRAINT `tb_order_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `tb_custom` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user` (
  `uid` int(10) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `privilege` int(1) NOT NULL DEFAULT '1',
  `lastlogin` datetime DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- 2016-12-09 20:07:47
