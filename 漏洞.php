<?php
session_start();
$_SESSION['id']=0;
header("Content-Type: text/html; charset=utf-8");
if($_SERVER["REQUEST_METHOD"]==="POST"){
    $user = $_POST["user"];
    $password = $_POST["password"];
    if($user!=null&&$password!=null){
        if($user=='admin'&&$password=='admin123'){
            $_SESSION['id']=1;
            echo "<script>
            alert('欢迎进入网页{$user}');
            window.location.href = '音乐.php';
            </script>";}
        else{
            echo "<script>
            document.addEventListener('DOMContentLoaded', function() {
            const error = document.getElementById('error');
            error.classList.add('fade');
            setTimeout(() =>{
            error.classList.add('fade1');
            setTimeout(() =>{
                error.classList.remove('fade','fade1');
                },500)
            },3000);
            });
            </script>";
        };
    }
    else{
        echo "<script>
        alert('请不要留空！');
        </script>";
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
body{
    background-image: linear-gradient(
        135deg,
        #11b0e1ee,
        #dc09dcfb
    );
    min-height: 100vh;
}
.box{
    height: 500px;
    width: 450px;
    margin: auto;
    background-image: linear-gradient(
        #11b0e1,
        blue
    );
    position: relative;
    top: 150px;
    border-radius: 15px;
    transition: all 0.5s;
    animation: donghua 0.5s linear;
}
.box:hover{
    transform: translateY(-5px);
}
.logo{
    height: 80px;
    width: 80px;
    background-image: url(../图片/preview.gif);
    background-size: cover;
    border-radius: 50%;
    position: absolute;
    left: 50%;
    transform: translate(-40px,50%);
}
.shuru{
    height: 40px;
    width: 400px;
    margin: 150px 0px 0px 20px;
    border-radius: 15px;
    border: 0px solid;
    outline: none
}
.shuru1{
    height: 40px;
    width: 400px;
    margin: 40px 0px 0px 20px;
    border-radius: 15px;
    border: 1px solid;
    outline: none
}
.btn{
    margin: 20px 0px 0px 22px;
    width: 400px;
    height: 40px;
    border-radius: 10px;
    border: 0px solid;
    background-color: #11b0e1;
    font-size: 18px;
    cursor: pointer;
}
.zhuche{
    position: absolute;
    top: 80%;
    height: 30px;
    margin-left: 120px;
}
#error{
    color: red;
    position: absolute;
    opacity: 0;
    left: 50%;
    transform: translateX(-50%);
}
.fade{
    opacity: 1 !important;
    transition:opacity 0.5s;
}
.fade1{
    opacity: 0 !important;
}
@keyframes donghua{
    0%{transform: translateY(-650px);}
    100%{transform: translateY(0px);}
}
</style>
<body>
    <div class="box">
        <div class="logo"></div>
        <form action="" method="post">
            <input type="text" placeholder="请输入账户名称" class="shuru" name="user" value="">
            <br>
            <input type="password" placeholder="请输入密码" class="shuru1" name="password" value="">
            <br>
            <input type="radio" name="" value="" style="margin:20px 0 0 20px;"><a href="">请同意一下用户协议</a>
            <br>
            <input type="submit" value="登录" name="action" class="btn">
            <div class="zhuche">如未有账号,请点击<a href="注册页.php">注册账号</a></div>
            <div id="error">密码错误</div>
        </form>
    </div>
</body>
</html>