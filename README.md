# python2.7-web_log
python日志分析<br>


### 日志格式<br>
54.36.149.5 - - [07/Oct/2018:00:09:44 +0800] "GET /xxxxx.php?aid=2924 HTTP/1.1" 200 2261 "-" "Mozilla/5.0 (compatible; AhrefsBot/5.2; +http://xxx.com/robot/)"<br>


#### mysql数据库创建<br>
create database intest default character set utf8 collate utf8_general_ci ;<br>
use intest;<br>

#### 创建表<br>
create table ipinfo(id int auto_increment primary key,ipaddress varchar(200),countip int);<br>
create table whereip(id int primary key auto_increment,country varchar(100),area varchar(100),region varchar(100),city varchar(100),ip varchar(100),time datetime);<br>

#### 查询点击排名<br>
select country,area,region,city,ip,count(ip) as 点击数排名 from whereip group by ip order by 点击数排名 desc <br>
<br>
 ![image](https://github.com/fengwenl/python2.7-web_log/blob/master/img1.png)<br>
