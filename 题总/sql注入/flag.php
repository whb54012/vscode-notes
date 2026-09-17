<?php
session_start();
if(!isset($_SESSION['id'])||$_SESSION['id']!==1){
    echo "<script>
        window.location.href = 'login.php';
    </script>";
}
?>
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>管理后台</title>
<style>
  body { margin:0; font-family:sans-serif; background:#0f1117; color:#e6e6e6;
         display:flex; align-items:center; justify-content:center; min-height:100vh; }
  .box { text-align:center; }
  .box h1 { font-size:22px; color:#7c8cff; margin:0 0 10px; }
  .box p { color:#6b7280; font-size:14px; margin:0; }
</style>
</head>
<body>
  <div class="box">
    <h1>管理后台</h1>
    <p>CquetCTF{}</p>
  </div>
</body>
</html>