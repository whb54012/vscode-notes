<?php
// 数组类型键值对
$arr1=array('a','b','c');
echo $arr1[1].'\n';
// 键   值
// 1    a
// 自定义键值对
$data=[
    'name'=>'whb',
    'age'=>18
];
foreach ($data as $value){
    echo $value.'\n';
}
// 取值
foreach ($data as $key=>$value){
    echo $key.'\n';
    echo $value;
}
?>