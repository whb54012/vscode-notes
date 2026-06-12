<?php
$dir='./';
$d=opendir($dir);//打开目录
$file=readdir($d);//按行读取目录结果
while($file=readdir($d)!==false){
    echo $file;
}
?>