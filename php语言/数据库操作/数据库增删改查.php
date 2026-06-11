<?php
$link = mysqli_connect("localhost","root","root","database");
//增----------------
$sql1 = "insert into 表格名 values (null,'','','')";
//对于自增长元素不需要传值，要么就直接传null或0，记得变量用花括号包住以免出现问题
$sql1 = "insert into 表名(成员名1,成员名2,..) values (null,'','','')";
//指定接受的成员，就不用给自增长传值
//改----------------
$sql2 = "update 表格名 set 成员名='内容' where(条件)";
//更新数据库单个 ID 的单个字段值，将指定内容更新，不加条件会导致全部更新
//删------------------
$sql1 = "delete from 表格名 where(条件)";
//删字段用 update，删整行用delete
//注意，当元素不存在时delete也会认为是删除了的，会返回true
//查
$sql = "select */成员名 from 表格名 条件";
//mysqli_query($link, $sql)查询结果不管有或没有，只要mysql语句没有错误，就都是返回true
//即使账号密码错误也能通过，所以不可以用来判断账号密码是否输入正确
//mysqli_num_rows(); 用与统计查询结果后得到的行数
mysqli_num_rows(mysqli_query($link, $sql)); //通过查询行数
//来确定符合条件的行数是否为0，不为0说明条件满足的行数存在