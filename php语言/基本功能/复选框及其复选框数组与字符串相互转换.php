<?php
var_dump($_GET);
var_dump($_POST);
//检测是否传输数据过来
echo "<br>";
$shuzhu = $_POST['likes'];
print_r($shuzhu);
$shuzhu_string = implode(",", $shuzhu);
//将传过来的复选框的多个同一属性的数组转换成字符串,同元素表单数组用自己设置的符号分开，两者顺序写反也不影响
echo "<br>";
print_r($shuzhu_string);//likes元素表单勾选内容以逗号隔开展示
$shu = explode(',', $shuzhu_string);
echo "<br>";
print_r($shu);
//explode将字符串转换为数组，可用于将数据库的内容提取出来后重新合在一起,只要数据按设置的分割符分割的都可
