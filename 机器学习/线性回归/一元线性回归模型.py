# y= kx + b
#    |    |
# k=权重  b=偏置
from sklearn.linear_model import LinearRegression
import numpy as np
# numpy也可用列表代替,但速度更慢
x_train=np.array([
    [170],
    [187],
    [165],
    [177],
    [161]
])
y_train=np.array([56.3,75,65.1,68.5,60.6])

model=LinearRegression()
# 创建实例化模型

model.fit(x_train,y_train)
# 将数据与特征放入,算出损失函数最小的权重和偏置
new=[[155]]
pred=model.predict(new)
# 预测数据
print(f"预测数值为{pred[0]},权重为{model.coef_[0]},偏置为{model.intercept_}")
