const isConfirmed = confirm("你确定要删除这条数据吗？");
if (isConfirmed) {
    window.location.href = "网址";//通过选择来跳转网页,触发后跳转到指定网页
}else{
    alert("quexiao");
}
window.location.href = "网址";//也可在code执行完后直接跳转网页
