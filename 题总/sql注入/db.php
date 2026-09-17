<?php
$local='localhost';
$user='root';
$pass='root';
$t_name='sql';
function connect(){
    global $local,$user,$pass;
    $link=mysqli_connect($local,$user,$pass);
    if(!$link){
        die("数据库连接失败". mysqli_connect_error());
    }
    mysqli_query($link,"set names utf8mb4");
    return $link;
}
function check(string $username,string $password){
    global $t_name;
    $link=connect();
    $create="CREATE DATABASE IF NOT EXISTS `{$t_name}`
    DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin";
    mysqli_query($link,$create);
    $use="use `{$t_name}`";
    mysqli_query($link,$use);
    $table="create table IF NOT EXISTS `user`(
    username varchar(20),
    password varchar(20)
    )charset=utf8mb4;";
    mysqli_query($link,$table);
    mysqli_query($link, "INSERT IGNORE INTO `user` (username,password) VALUES
    ('admin', 'admin123'),
    ('test',  'test123')");
    $sql="select * from user where username='{$username}' and password='{$password}'";
    if(preg_match('/[\s\'"\/]/',$username.$password)){
        return 0;
    }
    $result=mysqli_query($link,$sql);
    return $result;
}
?>