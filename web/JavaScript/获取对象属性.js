let b=document.getElementById('id属性名');
//获取id属性

let c=document.querySelector('标签/.属性/#id名');
// 获取任意属性和标签

document.getElementsByClassName('class属性名');
document.getElementsByTagName('标签');
// 这两特殊类,返回的是所有属性名或标签名的列表,使用时要加上索引,就算新增元素也会自动加进去
let a=document.getElementsByClassName('.box');
a[0].style.color='red';
// 对页面抓取的所有.box属性的第一个进行颜色更换

const a=querySelector('.box')
a.style.backgroundColor='red';
// 对于属性元素有像background-color这样有短横线连接的一律用小驼峰
// 把短横线后的首字母大写后去掉横线表示

元素.classname='类名'
// 替换属性,将另一个属性名添加进来,并把重复的属性替代

function update(){
    let s=document.querySelector('img');
    console.log(s.src);
    // 获取标签属性
}

对象.innerText=文本内容;
// 当成文字执行,不会被渲染
对象.innerHTML=HTML内容;
//当成前端元素执行,标签代码会被执行

function update1(){
    let s=document.querySelector('h1');
    const a=s.id;
  // 获取截取对象的指定属性
    const a=s.innerText//获取文本内容
    const a=s.innerHTML//获取内部文本和标签
    console.log(s.innerHTML);
    // 获取内部文字 + 内嵌 HTML 标签
}


