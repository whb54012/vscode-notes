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

-- show查找 后面加关键字而不是自定义的表名和列名
show schemas; = show databases;
展示所有数据库
show tables from 库名;
-- 展示数据库所有表名
show columns from 表名
show columns from 表名 from 库名(如果没有use库名就需要在后面在指定一个库名)
-- 展示指定某个表中的字段名

-- mysql.innodb_table_stats innodb查找引擎使用(MySQL5.6 及以上版本)
select (table_name,database_name)\* from innodb_table_stats(where 条件)
-- 查找所有用innodb引擎查找的数据库和数据表,不能查字段

-- mysql.innodb_index_stats innodb查找引擎使用(MySQL5.6 及以上版本)
select table_name,database_name,index_name from mysql.innodb_index_stats
-- 查找表名与库名以及索引名