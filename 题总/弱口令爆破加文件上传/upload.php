<?php
session_start();
if(!isset($_SESSION['id'])||$_SESSION['id']!==1){
    echo "<script>
        alert('请先登录');
        window.location.href='index.php';
    </script>";
    exit();
}
if($_SERVER['REQUEST_METHOD']==='POST'&&isset($_FILES['file'])){
    $name=$_FILES['file']['name'];
    $tmp=$_FILES['file']['tmp_name'];
    $target='/var/www/html/upload/';
    $arr=array('.jpg','.png','.gif','.htaccess');//白名单
    $newname=strtolower($name);//转换为小写
    $newname = str_replace("\0", "", $newname);
    $newname=strrchr($newname,'.');//截取最后一个点后面的后缀，让其后缀名绕过直接失效
    if(in_array($newname,$arr)){
        move_uploaded_file($tmp,$target.$name);
    }elseif($_FILES['file']['error'] !== 0){
        echo '<script>alert("请上传文件");</script>';
    }else{
        echo '<script>alert("文件名错误");</script>';
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
    html{
        margin: 0px;
    }
        .btn{
            position:fixed;
            width: 150px;
            height:75px;
            background: greenyellow;
            top: 70%;
            left: 40%;
            border-radius: 15px;
            font-size: 24px;
        }
        .sb{
            position:fixed;
            width: 150px;
            height:75px;
            background: palevioletred;
            top: 70%;
            border-radius: 15px;
            left: 54%;
            font-size: 24px;
        }
        .im{
            position: fixed;
            top: 20%;          /* 垂直居中 */
            left: 50%;
            transform: translate(-50%,0%);
            width: 650px;
            height:450px;
        }
        .bg-video{
            margin: 0px;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .speak{
        position: absolute;
        height: 100%;
        width:100%;
        top: 0;
        left: 50%;
        transform: translate(-50%,0);
        background-color: rgba(0, 0, 0, 0.326);
    }
    </style>
</head>
<body>
    <video src="./15v3-1080p.mp4" autoplay muted loop playsinline class="bg-video"></video>
    <div class="speak"></div>
     <div class="box">
        <form action="" method="post" enctype="multipart/form-data">
            <input type="file" hidden class="file" name="file">
            <button type="button" class="btn" >打开文件</button>
            <button class="sb" type="submit" >提交文件</button>
        </form>
        <?php
        if(isset($name)&& $_FILES['file']['error'] === 0 ){
                $safe = htmlspecialchars($name, ENT_QUOTES, 'UTF-8');
                echo"<img src='upload/$safe' alt='' class='im'>";
        }
        ?>
    </div>
<script>
    let a=document.getElementsByClassName('btn')[0];
    let b=document.getElementsByClassName('file')[0];
    a.addEventListener('click',()=>{b.click()})
</script>
</body>
</html>