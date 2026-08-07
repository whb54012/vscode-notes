let b=document.getElementById('id属性名');
//获取id属性

let c=document.querySelector('标签/.属性/#id名');
// 获取任意属性和标签

document.getElementsByClassName('class属性名');
document.getElementsByTagName('标签');
// 这两特殊类,返回的是所有属性名或标签名的列表,使用时要加上索引
let a=document.getElementsByClassName('.box');
a[0]

function update(){
    let s=document.querySelector('img');
    console.log(s.src);
    // 获取标签属性
}
function update1(){
    let s=document.querySelector('h1');
    const a=s.id;
  // 获取截取对象的指定属性
    s.innerText="文本内容<br>"//不会被渲染,原样输出
    s.innerHTML="文本内容<br>"//会被渲染
// innerhtml和innertext区别在于会不会被html渲染
    console.log(s.innerHTML);
    // 获取内部文字 + 内嵌 HTML 标签
}
对象.innerText=文本内容;
// 当成文字执行,不会被渲染

对象.innerHTML=HTML内容;
//当成前端元素执行,标签代码会被执行