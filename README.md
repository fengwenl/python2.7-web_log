# python2.7-web_log
python日志分析

//mysql数据库创建
create database intest ;
use intest;
//创建表
create table ipinfo(id int auto_increment primary key,ipaddress varchar(200),countip int);
create table whereip(id int primary key auto_increment,country varchar(100),area varchar(100),region varchar(100),city varchar(100),ip varchar(100),time datetime);
