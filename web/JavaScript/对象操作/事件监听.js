第一种
// 元素对象.on+事件=函数
const btn=document.getElementById("id")
btn.onclick=function(){}

第二种
// 元素对象.addeventlistener('事件类型',执行函数)
const btn=document.getElementById("id")
btn.addEventListener('click',function(){})

事件类型:
点击:click
