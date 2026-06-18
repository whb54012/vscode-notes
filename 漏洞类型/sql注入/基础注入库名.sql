database();显示当前所在数据库
version();获取当前数据库版本
user();获取当前数据库用户
information_schema:记录所有库名的表
information_schema.tables:记录所有表名的表
information_schema.columns:记录所有成员名的表
table_name:表名
column_name:成员名/列名
table_schema:数据库名
select * from information_schema.tables where table_schema = database();
查找当前指定数据库下的所有表名
select * from information_schema.columns where table_schema = database() and table_name = '表名';
查找指定数据库下指定表名的成员名
select group_concat(成员名) from 表名;
将查出来的成员名用group_concat函数变成一行直接输出
load_file('绝对路径');
高频语句