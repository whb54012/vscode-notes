密码whb54012
show databases; 展示数据库
create database 数据库名; 添加数据库
drop database 库名; 删除数据库
select database();查看当前所在的数据库
为数据库内创建表格
use 数据库名;选择数据库
create table 表格名(
    ID int auto_increment,id自增长,删去后将每行不会有id显示
    name varchar(20), 表字段名 类型,字符串varchar()内部添加数字来容纳相对应的字符
    sex varchar(5),表字段名 类型
    age int NOT NULL,添加限制，不能为空
    primary key(ID)与第一排内容一体,两者可同时删去,也可直接在第一句后写primary key就不用另起一行
)default charset=utf8mb4;可简写为charset=utf8mb4
//在打开的数据库中创造新的表格
show tables;打开选择数据库中的表格名
desc 表格名;打开指定的表格并查看其内部结构类型
insert into 表格名(可指定表字段名,多个用逗号隔开,也可以不写，直接指定全局) values (表制段对应的内容);为表制段名添加新数据
select */表字段名 from 数据库名.表格名;从数据库层面查看某个表
select */表字段名 from 表格名;进入数据库后查看表格指定一列内容，与查看结构类型不一样
select group_concat(*/表字段名) from 表格名;将查询得到的一列字段的多行数据拼接在一起
/*星号代表全部,也可替换成结构内所有列的成员名*/
drop table 表格名; 删除表格
rename table 原表格名 to 新表格名;重命名表格
alter table 表格名 drop 字段名;删除指定字段
truncate table 表格名;清空表格
delete from 表格名 where 表制段名=表制段值;删除符合内容的一行或多行内容
alter table 表格名 修改类型(modify:改变表字段名数据类型,add:添加新表字段名) 表字段名 数据(根据前面修改类型来填写相应数据);
////举例:alter table one add love int;为表格名添加新的字段名love,类型为int
alter table 表格名 change 表字段名 新表字段名 类型;将原有成员表字段名改成新表字段名并改变类型
update 表格名 set password=新内容;修改表格内的内容
update 表格名 set password=新内容(不是字符串就不用加引号),age=新内容 where username='条件';修改符合条件的内容(多条件也可以)
举例:update one set password=123 where username='whb';将表格one中username为whb的password修改成123