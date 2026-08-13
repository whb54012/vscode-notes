第一种
// 元素对象.on+事件=函数
const btn=document.getElementById("id")
btn.onclick=function(){}
// 第一种给同一个元素赋多种监听事件会被覆盖,只保留最后一个

第二种
// 元素对象.addeventlistener('事件类型',执行函数)
const btn=document.getElementById("id")
btn.addEventListener('click',function(){})
// 第二种同一个元素赋多种监听事件会依次执行,不会覆盖

事件类型:
点击:click
MouseEvent
