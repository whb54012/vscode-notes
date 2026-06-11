<?php
$a = 1;
$b = 2;
if(isset($_POST["username"])&&$_POST["username"] != null){
    echo "正确";
}
//isset()用于判断变量/数组索引是否定义且不为null，存在则为true，否则为false
//if (isset($a>=$b)){}错误，isset无法用来比较大小来判断正负，且$a和$b比较直接就可以得出布尔值