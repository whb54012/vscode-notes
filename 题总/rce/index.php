<?php
error_reporting(0);
echo 'eval($_GET["cmd"]);';
if(preg_match('/system|exec|.|file|`|shell_exec|passthru|popen|proc_open|pcntl_exec|assert|preg_replace|create_function|call_user_func|file_get_contents|file_put_contents|fopen|readfile|highlight_file|show_source|include|require/i',$_GET['cmd'])){
    die("hacker");
}
else{
    eval($_GET["cmd"]);
}
?>