<?php
function one(){
    echo "我是你爸爸\n";
}//函数定义
function two(){
    global $num;
    echo "真伟大\n",$num;//先定义在使用，如果调用函数在定义num前面将不会输出num
}
$num=100;//全局变量
function three(string $name,int $age){
//函数值形参可以给定类型,更规范
echo $name,$age."\n";
return $name;
}
one();//函数调用
two();
three("sb",18);
echo three("hh",18)."\n";
three(age:"18",name:"sb");//命名传参,通过变量名来传递值，无需按照顺序
?>