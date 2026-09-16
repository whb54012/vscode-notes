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
    $link=connect();
    $sql="select * from user where username='{$username}' and password='{$password}'";
    
}
?>