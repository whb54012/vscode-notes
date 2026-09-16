<?php
$local='localhost';
$user='root';
$pass='root';
$end=0;
$t_name='user';
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
    global $t_name,$end;
    $link=connect();
    $create="CREATE DATABASE IF NOT EXISTS {$t_name}
    DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin";
    mysqli_query($link,$create);
    $use="use {$t_name}";
    mysqli_query($link,$use);
    $table="create table `user`(
    username varchar(20),
    password varchar(20)
    )charset=utf8mb4;";
    mysqli_query($link,$table);
    $sql="select * from user where username='{$username}' and password='{$password}'";
    if(preg_match('/[\s\'"]/',$username)||preg_match('/[\s\'"]/',$password)){
        $end=1;
    }
    if($end==1){
        return 0;
    }
    $result=mysqli_query($link,$sql);
    return $result;
}
?>