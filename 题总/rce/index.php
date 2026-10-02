<?php
echo "if(strlen(\$_GET['x'])<=8){
eval(\$_GET['x']);}
else{
    echo 'hacker';
}";
if(strlen($_GET['x'])<=8){
eval($_GET['x']);}
else{
    echo 'hacker';
}
?>