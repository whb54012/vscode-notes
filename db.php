<?php
$local='localhost';
$user='root';
$pass='root';
$t_name='user';
$link='';
function connect(){
    global $local,$user,$pass;
    $link=mysqli_connect($local,$user,$pass);
    mysqli_query($link,"set name utf8mb4");
    if(!$link){
        die("数据库连接失败". mysqli_connect_error());
    }
    return $link;
}
function check($username,$password){
    global $t_name;
    $link=connect();
    $create="CREATE DATABASE IF NOT EXISTS {$t_name}
    DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_bin";
    mysqli_query($link,$create);
    $use="use {$t_name}";
    mysqli_query($link,$use);
    $table="create table `user`(
    username varchar(20),
    password varchar(20)
    )charset=utf8mb4;";
    mysqli_query($link,$table);
    $sql="select * from user where username='{$username}' and password='{$password}'";
    $result=mysqli_query($link,$sql);
    return $result;
}
?>