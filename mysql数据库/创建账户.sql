create user '用户名'@'%' identfied by '密码';
@'localhost'：只能在数据库本机登录（最安全）；
@'192.168.85.%'：只能从指定内网段登录；
@'%'：允许从任何 IP 登录（方便但风险高，生产环境慎用）
grant 权限 on 库名.表面(可以空白表示整个库)* to '用户'@'(是否指定ip)%';
例如：
grant all on *.* to 'whb'@'%'
grant:给予
all:全部权限
on:在..上
*.*:*通配符,表示所有库
to:目标
'whb'@'%':任意网段上都可登录此账号
flush privileges
#刷新赋予的权限使其生效
select user from mysql.user;
#查看数据库中所有的用户