需要支持堆叠注入才能实现预处理语句注入
set @变量名='sql语句';
//将注入语句写入变量内部
prepare code(自定义名称) from @变量名;
execute code;