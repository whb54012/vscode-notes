let arr=[1,2,3];
arr.push(1,2)
// 末尾添加指定元素
arr.unshift(1,2)
// 头部添加指定元素

let a=arr.pop()
// 删除最后一个元素并返回
let b=arr.shift()
// 删除第一个元素并返回
arr.splice(起始索引,删除个数)
// 从起始索引删除后面n个个数,删除个数不写就直接删完
