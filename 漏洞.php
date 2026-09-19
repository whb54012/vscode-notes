<?php
$dir = '/var/www/html/upload/';
$result=0;?>
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>文件上传</title>
<style>
  body {
    display: flex; justify-content: center; align-items: center;
    height: 100vh; margin: 0;
    background: #0f172a; color: #e2e8f0;
    font-family: system-ui, sans-serif;
  }
  .file{
    position: absolute;
    top: 200px;
  }
  form {
    background: #1e293b; padding: 30px 36px;
    border-radius: 12px; width: 340px;
    box-shadow: 0 10px 30px rgba(0,0,0,.4);
  }
  h2 { margin: 0 0 18px; font-size: 17px; }
  input[type=file] { width: 100%; margin-bottom: 16px; color: #94a3b8; }
  button {
    width: 100%; padding: 10px; border: 0; border-radius: 8px;
    background: #38bdf8; color: #0f172a;
    font-weight: 600; cursor: pointer;
  }
  button:hover { background: #7dd3fc; }
</style>
</head>
<body>
  <form action="" method="post" enctype="multipart/form-data">
    <h2>文件上传</h2>
    <?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $result=1;
    $tmp  = $_FILES['file']['tmp_name'];
    $name =basename($_FILES['file']['name']);   
    $target = $dir . $name;
    //先落盘：文件先真实存在于服务器上
    move_uploaded_file($tmp, $target);
?>
    <?php if (stripos($name, 'php') !== false) {
        usleep(30000);
        unlink($target);     // 删除
        echo "<div>恶意文件，已删除</div>";
    } else {
        echo "<div>上传成功:{$name}</div>";
    }}?>
    <input type="file" name="file" required>
    <button>上传</button>
  </form>
</body>
</html>