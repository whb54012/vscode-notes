<?php
$link = mysqli_connect("localhost", "root", "root","shujukuming") or die("连接失败");
//die（）为终止函数，会将内容输出后结束整个程序，多用于条件判断
//连接mysql数据库指令，内部四个元素，ip/域名:端口(端口默认3306，没改就不用写)，数据库用户名，数据库密码。要连的数据库名
//注意连接后就会绑定一个连接口使用后一定要关闭，否则下次连接就会新开一个连接占用资源
mysqli_query($link,"SET NAMES utf8");
//SET NAMES utf8设置连接通信，确保中文不会乱码
////前面写连接对象，后面写sql参数，包括写use 数据库名可直接切换其他数据库
mysqli_set_charset($link,'utf8');
//和上述功能一样，连接数据库元素，设置通信模式
mysqli_query:
mysqli_query($link,"use 数据库名");
//选择或切换数据库，如果mysqli_connect中已经绑定了数据库且不需要换库就可以不用写了
mysqli_query($link,"sql语句");
//执行sql语句，返回值为查询结果的资源类型，增删改返回true或false
mysqli_close($link);
//关闭连接节省资源