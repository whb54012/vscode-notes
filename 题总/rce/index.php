<?php
echo "";
if(strlen($_GET['x'])<=8){
eval($_GET['x']);}
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
    <a href="/test.php?cmd=ls">
  <button>执行ls</button>
</a>
</body>
</html>