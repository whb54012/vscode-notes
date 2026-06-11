<?php
//implode(数组,'分割符')两者顺序写反也不影响，可以将复选框的多个同一属性的数组转换成字符串
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="复选框及其复选框数组与字符串相互转换.php" method="post">
    <label> <input type="checkbox" name="likes[]" value="1">1</label>
    <!--用label将其包含连接，可以使点击文字的时候就会点上复选框-->
    <input type="checkbox" name="likes[]" value="2">2
    <input type="checkbox" name="likes[]" value="3">3
    <input type="submit" name="" value="btn">
</form>
<!--对于多选可直接给name元素设置数值[],配置会默认将他归为一类，不用数组用相同名的话就会后一个覆盖前一个-->
</body>
</html>
