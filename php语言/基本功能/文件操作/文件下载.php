<?php
$dir='./';
$d=opendir($dir);//打开目录
$file=readdir($d);//按行读取目录结果
is_dir($file);//判断是否为文件夹
while($file=readdir($d)!==false){
    if($file=='.'&&$file='..')
        continue;//把当前目录和上级目录所表示的点跳过打印
    echo $file;
    //自动打印打开目录下的每一给目录或文件名
}
filetype($d);//0判断输入内容是文件还是目录
unlink('相对路径/文件');//删除文件,不能删除文件夹

// 文件下载设置http头格式控制
header('Content-Type: application/octet-stream');//声明二进制类型,用于兼容老浏览器
header('Content-Disposition: attachment; filename="自定义文件名"');//弹出下载框
header('Content-Length: ' . filesize('相对路径/文件'));//将文件大小告诉浏览器,显示下载进度

readfile('相对路径/文件')//打开文件,配合下载框头部设置可变成下载文件
?>