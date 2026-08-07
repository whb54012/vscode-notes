var a=1;
var b='abc';
var x=a+b;
// 数值与字符串之间可以直接拼接
let arr1=[1,2,3];
let arr2=Array(1,2,3);
let arr3=new Array(1,2,3);
//若内部元素只有一个，就用第一个，第二格和第三个有歧义，会将它输入的元素默认为此数组长度
//如let arr1=Array[1]会将它理解为长度为一的数组;
document.write(arr1);
//当输出直接写数组本身时，他是直接输出所有元素
var c="1";
var d="2";
console.log(a==b);
console.log(a==c);//双等号时比较内容，无需在意类型
console.log(a===c);//三等号时会比较类型和内容两者
console.log(a!==c);//不等或不全等
