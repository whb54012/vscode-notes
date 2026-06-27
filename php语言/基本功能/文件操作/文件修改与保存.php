<?php
$file=file_get_contents('文件路径');//一次读取全部文件内容
echo "<form method='post'>
    <textarea name='txt' rows='15' cols='80'><?=$file?></textarea>
    <br>
    <button type='submit'>保存修改</button>
</form>";
//将文件内容打印到textarea内部进行修改并上传
$txt=$_POST['txt'];
file_put_contents($file,$txt);
//file_put_contents(文件路径,修改内容);将旧内容覆盖到新内容里面完成修改文件

// 直接写入
$content='内容';
$f=fopen($file,'w');
//fopen(文件路径,'操作模式')
// r           r+          w           w+          a           a+
// 读取        读写        写入        读写        追加写入      追加读写
// 读取内容    写入内容    清空内容    可读可写    在尾部写入     可读可写
//            一个个覆盖   写入,没有
//            前面内容     就新建个
fgetc($f);//读取打开的文件,只适用于有读取功能的
fwrite($f,$content);
//fwrite(打开的文件,写入内容)
fclose($f);
// 关闭文件
?>