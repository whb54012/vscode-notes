范围查找
1.select */表字段名 from 表格名 where  表字段名>=具体数值 and 表字段名<=具体数值;
2.select */表字段名 from 表格名 where  between 数值and数值;
;打印出此范围的成员
3.select */表字段名 from 表格名 where  not(between 数值and数值);
;打印出非此范围的成员
4.select */表字段名 from 表格名 where 表字段名 in(数值1,数值2);
;查找出数值之间的成员名
---------------分页查找
select * from 表格名 where 条件 limit 0,3;
;表示从0行开始查找,查找3行
select count(*/成员名) from 表格名;
;查询有多少行数,后面也可以加条件
select count(*/成员名) from 表格名 where 条件;
select max(*/成员名) from 表格名;
;查询成员中的最大者
select min(*/成员名) from 表格名;
;查询成员中的最小者
select sum(*/成员名) from 表格名;
;查询成员中的总和
select avg(*/成员名) from 表格名;
;查询成员名中的平均值
----------后面都可以像第一个一样加条件;
----------------分组查询
select 成员名1,sum(成员名2) from 表格名 group by 成员名1;
;将成员名1相同的成员分成一组,并总和对应每一组的成员名2,sum可以改成上面的的其他类型
对于成员2是字符串无法数字结合,或者不想将数字结合,而是将其列举出来就用:
select 成员名1,group_concat(成员名2) from 表格名 group by 成员名1;
--------注意,成员1和成员2之间用逗号隔开,而不是空格
--------------------内连接
select 表1.成员名1,表2.成员名2 from 表1 表2 on 表1.成员名3=表2.成员名3;
;成员名3是连接核心,只有两者相同部分的成员1和成员2才会连接

