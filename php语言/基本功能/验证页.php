<?php
if ($_SERVER["REQUEST_METHOD"]=="POST"){
    if (isset($_POST["user"])&&isset($_POST["password"])){
        echo "hello";
    }
    else{
        echo "请不要留空";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    .box{
    height: 250px;
        width: 450px;
        margin: auto;
        background-color: pink;
        position: relative;
        top: 150px;
    }
    .shuru{
    height: 30px;
        width: 400px;
        margin: 40px 0 0 10px;
    }
    .btn{
    margin: 20px 0 0 150px;
        width: 60px;
        height: 30px;
    }
</style>
<body>
    <div class="box">
        <form action="">
            <input type="text" placeholder="请输入账户名称" class="shuru" name="user" value="">
            <br>
            <input type="password" placeholder="请输入密码" class="shuru" name="password" value="">
            <br>
            <input type="radio" name="" value=""><a href="">请同意一下用户协议</a>
            <br>
            <input type="submit" value="登录" name="action" class="btn">
        </form>
    </div>
</body>
</html>