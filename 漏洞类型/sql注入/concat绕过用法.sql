利用concat()拼接构建字符类串模式并写入语句内部

username = CONCAT(0x61, 0x64, 0x6D, 0x69, 0x6E) == CHAR(97, 100, 109, 105, 110)
构建条件匹配,等价于 'admin',自动用单引号包裹字符串,用于那些写条件时过滤引号的情况
列如注入途中需要打印符合admin的一行,但你无法写入用单引号包裹admin导致匹配的问题

concat()条件拼接
SELECT * FROM users WHERE CONCAT(user,name) = 'admin'
筛选出user列和name列的值拼接在一起,符合'admin'的打印出来