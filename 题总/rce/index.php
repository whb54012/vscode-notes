<?php
if(strlen($_GET['cmd'])<=9){
eval($_GET['cmd']);}
else{
    echo 'hacker';
}
?>
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>发送GET ls请求</title>
</head>
<body>
    <a href="?cmd=ls">
  <button>执行ls</button>
</a>
</body>
</html>