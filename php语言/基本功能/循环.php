<?php
$age=1;
while($age<5){
    echo $age,"\n";
    $age=$age+1;}
for($i=1;$i<=$age;$i++){
    echo $i;}
echo"\n";
do{
    echo $age;
    $age--;
}while($age>=1);
//遍历数组
$arr=["张三"."李四","王五"];
foreach ($arr as $values) { //as为核心，将数值的每一个元素映射到临时变量;
    echo $values;
}
echo "\n";
$arr2=["name"=>"王麻子","love"=>"song","sex"=>"男"];
foreach ($arr2 as $key=>$values){
    echo  $key,$values."\n";
}//键=>值为一体，创建核心也要按照键=>值格式创建临时变量
$arr3=["name"=>["王麻子"=>"a"],"love"=>["song"=>"b"],"sex"=>["男"=>"c"]];
foreach ($arr3 as $key1=>$values1){
    foreach ($values1 as $key2=>$values2){
    echo  $key1,$key2,$values2."\n";
}}//嵌套数组
?>