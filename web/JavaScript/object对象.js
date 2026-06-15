//自定义对象
let user = {
  name: "张三",
  age: 20,
  20:18,//键默认会被转换成字符串
  sayHello: function() {
    console.log("你好！");
  }
};
// 对象调用两种方式
console.log(user.name);
console.log(user['20']);

// 函数调用
// 1.普通函数直接调用
function per(name){
  return "hello"+name;
}
var x=per('whb');
console.log(x);
//2.构造函数加new
function Person(name, age) {
  this.name = name;//前一个name是自己设置的属性，也可以设置为其他单词，后一个为接受对象不可修改
  this.age = age;
}
let p1 = new Person("李四", 25);