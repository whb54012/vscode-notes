<?php 
// serialize():序列化函数数,将一个对象转换成字符串
// unserialize():反序列化函数,将一个字符串转换成对象
class 对象名{
    //类的变量称之为属性
    //类的函数称之为方法
}
$变量名 = new 对象名();
//调用类属性对象,创造对象

// 权限属性(不加默认public公共属性):
// public:公共属性,在类的外部和内部都可以访问
// protected:受保护属性,只能类的内部和子类访问,在类的外部无法访问
// private:私有属性,只能在类的内部访问,在类的外部无法访问,在子类也无法访问 

// 类的方法(魔术方法前面需加上function):
// __construct():构造方法,在创建对象时自动调用,通常用来初始化对象的属性
// __destruct():析构方法,在对象运行到程序末尾或销毁时自动调用,通常用来释放资源或执行清理操作
// __call():当调用一个不可访问的方法时自动调用,可以用来处理方法不存在的情况
// __get():当读取一个不存在的属性时自动调用,可以用来处理属性不存在的情况
// __set():当给一个不可访问或不存在的属性赋值时自动调用,可以用来处理属性不存在的情况
// __isset():当用isset()传进一个不存在或不可访问的属性时自动调用,返回布尔值
// __toString():当对象被当成字符串使用时自动调用,可以用来定义对象的字符串表示形式
// __invoke():当对象被当成函数调用时自动调用,可以用来定义对象的可调用行为
// __clone():当对象被克隆时自动调用,可以用来定义对象的克隆行为
// __sleep():当对象被序列化时自动调用,可以用来指定哪些属性 需要被序列化
// __wakeup():当对象被反序列化时自动调用,可以用来重新初始化对象的属性或资源 -->
?>
<?php
class person{
    public $name='whb';//类属性$name
    private $age=18;
    protected $a=1;
    public function __construct($name){//接收外界参数的变量,与类属性$name无关,可改名
        $this->name = $name;
//$this->name:因为前面已经调用了$this,后面的类属性name就不需要$
    }
    public function __wakeup() {
        echo "对象被反序列化了\n";
    }
    public function __invoke(){
        echo "对象被当函数调用了\n";
    }
    public function __destruct() {
        echo "对象销毁了\n";
    }
    public function __unset($n)//写一个参数顶位
    {
        echo "对象调用unset方法销毁不存在或不可访问的属性了\n";
    }
    public function __call($a, $b){//必须写两个参数顶位,随意命名
        echo "对象使用了不可访问或不存在的函数方法\n";
    }
    public function __get($a){//和invoke一样,必须写一个参数顶位
        echo "对象读取了不可访问或不存在的属性\n";
    }
    public function __set($name, $value)//必须写两个参数顶位
    {
        echo "对象为不可访问或不存在的属性赋值了\n";
    }
    public function __isset($content)//创建变量接收传进的属性名,而非熟属性值
    {
        echo "为isset传入了不可访问或不存在的值\n";
        return isset($this->$content);
        //$content为动态属性,指向传进来的age，而非$a->age的值,保证传进来
        //的属性存在并能被读取,否则isset/empty()又会调用__isset方法陷入死循环
    }
}
$a = new person('参数');
echo $a->name;//打印whb
$serialized = serialize($a);
//先将对象序列化为字符串

$b = unserialize($serialized);
//对象被反序列化了

$b();
//对象被当成函数方法调用了
//对象属性有invoke时对象才可当成方法调用,否则会报错

$b->run();
// 对象使用了不存在或不可访问的方法了
//触发__call方法

$a->yes;
//对象读取了不存在或不可访问的属性

$a->yes=1;
//为不存在或不可访问的属性赋值了

echo isset($a->age);//empty($a->age)
//对isset/empty传进了一个不存在的属性

unset($b->c);
//对象调用unset删除不存在或不可访问属性了

//php结束,变量销毁,打印对象销毁了
?>
<!-- 序列化的对象将不是对象,而是一个字符串,所以接收序列化的对象在销毁时不会触发析构 -->
