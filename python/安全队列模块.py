import queue
#启用队列模块
q = queue.Queue()
#创建队列
for i in range(100):
    q.put(i)#往队列添加数据
for i in range(100):#循环取出
    data = q.get()
    print(data)

#print(q.get())
#在没有外界条件阻止下即使队列为空也不会停止进程，而是保持程序运行但不输出任何值
#当队列为空时会q,empty返回True，否则就是False，可以用判断语句使其停止
if q.empty():
    print("结束")
else:
    print(q.get())