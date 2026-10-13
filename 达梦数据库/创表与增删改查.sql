达梦数据库里字段名属性用双引号""表示,在条件匹配的情况下写属性值必须用单引号'',
否则会去匹配字段名而非内部属性值,并且在创建模式或者表格名之类的字段名的时候如果
不用双引号包裹起来,就算是小写他也会给你大写写进去

create TABLESPACE 表名 DATAFILE "硬盘路径" 
SIZE 128          -- 初始大小128MB
AUTOEXTEND ON NEXT 64 -- 自动扩容,每次+64M,给表空间设置大小能容纳多少数据
MAXFILES 2000;    -- 最多2000个dbf文件，不写默认最多256个表文件
--创建表空间，用来容纳创建的表

DROP TABLESPACE TS_BIZ;
-- 删除表空间，连带里面所有数据

create table 表名(
    id int identity(1,1),
    -- id int identity(1,1) primary key,IDENTITY(起始值,步长)
    -- 和mysql一样，直接写在id后面也可以实现自增长,省略最后一行
    name varchar(50) not NULL,
    age float default 0,
    money numeric(12,2) default 0,--numeric(12,2)十进制2位小数,数值12位,避免float的精度问题
    primary key(id),--
)TABLESPACE 表格空间;--不写放进当前模式的默认表空间
--创建表格，放进指定的表格空间

drop table 表名;--删除表格

select 字段名 from 表名/实例.表名 where 条件;
INSERT INTO t_user(username,age) VALUES('张三',20);
UPDATE t_user SET age=21 WHERE id=1;
DELETE FROM t_user WHERE id=1;
-- 增删改查和mysql完全一样


-- 与mysql完全相同
alter table 表名 add column 字段名 varchar(100);增添字段名
alter table 表名 drop column 字段名;删除指定字段
alter table 表名 modify 字段名 类型;修改指定字段类型
-- 达梦独有
alter table 表名 rename column 旧字段名 to 新表字段名;
--增删改字段完全一样,修改字段名不同