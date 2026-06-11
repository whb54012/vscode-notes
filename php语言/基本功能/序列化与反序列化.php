<?php
class person{
    public $name;
    public $age;
    protected $sex;
    function name()
    {
        echo $this->name;
   }//封装函数，给类构建功能
    function age()
    {
        echo $this->age;
    }
    function sex()
    {
        echo $this->sex;
    }
    public function __construct($name, $age, $sex) {
        $this->name = $name;
        $this->age = $age;
        $this->sex = $sex;
    }
}
$person = new person("张三",18,"boy");
//创造一个类对象
$person->name();
$person->age();
$person->sex();
//启用函数里的功能
echo serialize($person);//序列化格式
echo "<br>";
echo unserialize(serialize($person));//将序列化后的参数反序列化回去
$a =unserialize($_GET["html"]); //接受url里面写入序列化后的参数并将其反序列化
$a->name();
//结果会报错，无法反序列化
$b = urlencode(serialize($person));//接受通过url转义后的序列化编码
echo unserialize($b);//将通过url转义的编码反序列化，成功打印
//所以向url里面输入序列化参数时，需要将其url转义后在写进get参数里面，否则无法反序列化回去


