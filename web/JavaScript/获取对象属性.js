let a=document.getElementsByClassName('.class属性名');
let b=document.getElementById('#id属性名');
let c=document.querySelector('标签/.属性/#id名');
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