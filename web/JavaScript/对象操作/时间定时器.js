function one(){
    执行语句
}
setTimeout(one, 延迟时间);// 只执行一次
//延迟多少秒后再执行函数

let n=setInterval(one,间隔时间)
// 每隔多少秒执行一次函数
clearInterval(n)
// 关闭定时器

let n=setInterval(function(){
    执行语句
    if(条件){
        clearInterval(定时器对象)
    }
},间隔时间)//执行完毕后关闭对象

这里调用函数不需要加括号,直接写函数名