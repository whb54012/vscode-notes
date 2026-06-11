<?php
$con=mysqli_connect("localhost","root","root","database");
$sql="select * from 表名";
$data=mysqli_query($con,$sql);
$row=mysqli_fetch_row($data);
//接收执行后结果,$row每接收一行,$data就会指向下一行,逐行读取
//row[0]   row[1]      row[2]
// id	    name	   age  <--row[]
// 1	    张三	    18  <--$data
// 2	    李四	    19
// 3	    王五	    20
while($row=mysqli_fetch_row($data)){
    //不可直接用$row,$row必须每次都要去接收新行,否则单独的$row永远有结果成为死循环
    echo $row[0],$row[1],$row[2];
}
// 1,张三,18
// 2,李四,19
// 3,王五,20
?>