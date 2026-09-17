<?php
header("Content-Type: text/html; charset=utf-8");
error_reporting(0);
$result=0;
$id='';
if($_SERVER["REQUEST_METHOD"]==='POST'){
    $ua = $_SERVER['HTTP_USER_AGENT'] ?? '';
    $target='/var/log/apache2/access.log';
    file_put_contents($target,$ua, FILE_APPEND); 
    $result=1;
    $id=$_POST['id'];
    $id=strtolower($id);
    $arr=array('php://','filter://','data://','zip://','phar://');
    foreach($arr as $key){
        if(strpos($id,$key)!==false){$result=2; break;}}
}
?>
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>文件查看器</title>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body { font-family: system-ui, sans-serif; background:#0f172a; color:#e2e8f0;
         display:flex; justify-content:center; padding:40px 16px; }
  .wrap { width:720px; }
  h2 { font-size:20px; margin-bottom:6px; }
  .sub { font-size:13px; color:#94a3b8; margin-bottom:18px; }
  .bar { display:flex; gap:10px; margin-bottom:14px; }
  input { flex:1; padding:10px; border-radius:6px; border:1px solid #334155;
          background:#1e293b; color:#e2e8f0; font-family:monospace; }
  button { padding:10px 20px; border:none; border-radius:6px; background:#22c55e;
           color:#052e16; font-weight:bold; cursor:pointer; }
  button:hover { background:#16a34a; }
  pre { background:#1e293b; border:1px solid #334155; border-radius:8px;
        padding:16px; min-height:200px; white-space:pre-wrap; word-break:break-all;
        font-family:monospace; font-size:13px; color:#a5f3fc; }
  .tip { margin-top:14px; font-size:12px; color:#64748b; }
</style>
</head>
<body>
<div class="wrap">
  <h2>文件查看器</h2>
  <div class="sub">输入文件名查看内容</div>
  <div class="bar">
    <form action="" method="post">
        <input name="id" id="text" placeholder="例如：readme.txt">
        <button onclick="load()" type="submit">发送</button>
    </form>
  </div>
  <pre id="out"><?php
   if ($result!=0){
        if($result==1){include($id);}
        elseif ($result == 2) {echo "<script>alert('违规字符')</script>";}
        else{echo "禁止包含自身";}}
        else{echo "等待操作...";}?>
</pre>
  <div class="tip">提示：只允许查看部分目录下的文件哦</div>
</div>
</body>
</html>