<?php
$dir='./';
$d=opendir($dir);//打开目录
$file=readdir($d);//按行读取目录结果
is_dir($file);//判断是否为文件夹
while($file=readdir($d)!==false){
    echo $file;
    //自动打印打开目录下的每一给目录或文件名
}
?>