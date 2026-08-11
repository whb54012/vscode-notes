select username from user;select password from user;
通过用分号隔绝语句来堆叠注入多个语句进行注入攻击
handler 表名 open;handler 表名 first;handler 表名 next;
handler 表名 close;读取表里的数据,读几行就用next往下面继续
后端php连接数据库函数要求
mysqli_query()
//只支持一条语句
mysqli_multi_query()
//支持多条语句,用于堆叠注入