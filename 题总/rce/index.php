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
    <!-- 点击按钮跳转，GET参数 cmd=ls -->
    <button onclick="location.href='/test.php?cmd=ls'">点击执行 ls</button>
</body>
</html>