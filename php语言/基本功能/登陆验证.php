<?php
if($_SERVER["REQUEST_METHOD"]==="POST"){
// $_user=$_POST["user"]??"";版本升级为8.0后的选择语法
 $_password=isset($_POST["password"])?$_POST["password"]:"=";
}//老板选择法，条件为真就选择？后面的，假就选择：后面的
//$_SERVER["REQUEST_METHOD"]==="POST"对提交的信息进行判断，以免对刷新页面这类的get请求也会产生登录时的post提示
