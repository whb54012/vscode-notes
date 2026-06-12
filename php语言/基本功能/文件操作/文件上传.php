<?php
// $_FILES:php接收上传文件的超全局变量
$name=$_FILES['表单name值']['name'];//获取文件的上传原始名,获取时会截断/前面的符号
$type=$_FILES['表单name值']['type'];//获取文件的mime类型
$size=$_FILES['表单name值']['size'];//获取文件字节大小
$tmp=$_FILES['表单name值']['tmp_name'];//获取临时上传文件名,用于移动/校验/读取文件
$error=$_FILES['表单name值']['error'];//获取上传时的错误代码

move_uploaded_file($tmp,'文件保存目录/文件名');//将文件移动到保存目录的文件里,可自己设置上传文件名
strstr($tmp,'.');//找字符串里第一个匹配内容并返回后面的内容
$tmp1=strrchr($tmp,'.');//找字符串里最后一个匹配内容并返回后面的内容
//截取文件名后缀用strrchr,过滤特殊字符后面的内容就用strstr

$arr=array('jpg','png','gif');//设置白名单
in_array($tmp1,$arr)//白名单检验字符串是否存在于数组
?>