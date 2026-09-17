<?php
session_start();
include 'db.php';
if(!isset($_SESSION['id'])){
        $_SESSION['id']=0;
        $_SESSION['one']=0;
}
if($_SERVER['REQUEST_METHOD']==='POST'){
    if(!isset($_POST['username'])||!isset($_POST['password'])){
    echo "<script>alert('请输入账号或密码');
        window.location.href = 'index.php';</script>";
        exit();
    }
    $result=check($_POST['username'],$_POST['password']);
    if($result===0||$result===false){
        echo "<script>alert('输入有误');
        window.location.href = 'index.php';</script>";
        exit();
    }
    elseif(mysqli_num_rows($result)>0){
    $row=mysqli_fetch_row($result);
    if($_POST['username']==='admin'){
        $_SESSION['id']=1;
        echo "<div class='name'>管理员'{$row[0]}',你的密码是'{$row[1]}'</div>";
    }else{
        echo "<div class='name'>用户'{$row[0]}',你的密码是'{$row[1]}'</div>";
    }
    }else{
        echo "<script>alert('登陆失败');
        window.location.href = 'index.php';</script>";
    }
}
?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>登录</title>
  <style>
    body {
      min-height: 100vh;
      display: flex;
      position: relative;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #667eea, #764ba2);
      font-family: sans-serif;
    }
    .name{
      background-color: #667eea;
      position: absolute;
      top: 200px;
    }
    .box {
      width: 320px;
      padding: 30px;
      border-radius: 16px;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.3);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    h2 { text-align: center; color: #fff; margin: 0 0 24px; }
    /* ★ 输入框外面的壳，毛玻璃加这层 */
    .glass-input {
      margin-bottom: 16px;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.3);
      border-radius: 8px;
    }
    /* ★ 输入框自己透明 */
    .glass-input input {
      width: 100%;
      padding: 10px 12px;
      background: transparent;
      border: none;
      outline: none;
      color: #fff;
      font-size: 14px;
      box-sizing: border-box;
    }
    .glass-input input::placeholder {
      color: rgba(255, 255, 255, 0.6);
    }
    button {
      width: 100%;
      padding: 11px;
      margin-top: 8px;
      border: none;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.3);
      color: #fff;
      font-size: 15px;
      cursor: pointer;
    }
    button:hover { background: rgba(255, 255, 255, 0.45); }
  </style>
</head>
<body>
  <form class="box" action="" method="POST">
    <h2>登录</h2>
    <div class="glass-input">
      <input type="text" name="username" placeholder="请输入用户名">
    </div>
    <div class="glass-input">
      <input type="password" name="password" placeholder="请输入密码">
    </div>
    <button type="submit">登录</button>
  </form>
</body>
</html>