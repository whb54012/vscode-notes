<?php
getcwd();//显示当前目录
glob("字符串类型/可用chr()变化或其他函数组合返回");//*显示所有当前目录所有文件名
scandir("字符串类型/可用chr()变化或其他函数组合返回");//.显示当前目录所有文件名

print_r(getcwd());
// 返回文件当前目录

glob("*");glob(chr(42));
// 正则匹配返回数组,通过通配符来查找当前目录符合条件的文件,可通过../来逃逸

$变量=opendir(".");$变量=opendir(chr(46));$变量=opendir(current(localeconv()));
//  用变量接收当前目录的所有文件,./可以写成.,../写成..

while($f=readdir($变量)){echo $f;} 
// 循环接收每行数据并打印

scandir(".");scandir(chr(46));scandir(current(localeconv()));
// 和上述一样,返回数组
?>