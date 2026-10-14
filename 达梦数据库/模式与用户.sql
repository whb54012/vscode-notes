达梦的模式就接近于mysql的库,不同的表格中只有在不同的模式下才能被查看

set schema 实例名;--选择不同的实列，类似于mysql的选择库
create schema 模式;--创建模式
create user 用户名 identified by "密码" default TABLESPACE 表格空间;
--创建用户和对应的模式
-- 密码如果不用引号包裹会自动转换成大写写进去
drop user 用户;
-- 删除用户会将携带的模式及模式里面的表格一同删除
drop schema 模式;
-- 单独删除模式

GRANT 权限 ON 模式.表名 TO 用户;--(SELECT,INSERT,UPDATE,DELETE)四个权限
--给用户其他某个模式下表名整个模式的指定权限
GRANT 权限 ANY TABLE ON SCHEMA 模式 TO 用户;
-- 给用户整个模式的指定权限
-- GRANT SELECT,INSERT,UPDATE,DELETE ANY TABLE ON SCHEMA bus TO TEST;
-- 直接给test用户在bus模式下对所有表格的所有执行权限