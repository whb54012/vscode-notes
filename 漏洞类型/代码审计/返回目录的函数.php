<?php
getcwd();//显示当前目录
glob("通配符*");//*显示所有当前目录所有文件名
scandir("字符串.或者当前目录路径");//.显示当前目录所有文件名
localeconv();//返回一个数组,第一个数组值为.
current(localeconv());//取出数组第一个元素，搭配localeconv()取出点

print_r(getcwd());
echo __DIR__;
// 返回文件当前目录

glob("*");glob(chr(42));
// 正则匹配返回数组,通过通配符来查找当前目录符合条件的文件,可通过../来逃逸

$变量=opendir(".");$变量=opendir(chr(46));$变量=opendir(current(localeconv()));
//  用变量接收当前目录的所有文件,./可以写成.,../写成..

while($f=readdir($变量)){echo $f;} 
// 循环接收每行数据并打印

scandir(".");scandir(chr(46));scandir(current(localeconv()));scandir(getcwd());
// 接收目录或.来打印当前目录文件，和上述一样,返回数组

scandir("内容")['下标'];
glob("内容")['下标'];
// 直接取出数组元素也可用
?>