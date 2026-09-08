from sklearn import neighbors
#导入knn算法框架
import numpy as np
#导入numpy数组列表,支持向量化运算,比列表更好用

x_train=np.array([
    [170, 65],   # 男
    [160, 55],   # 女
    [180, 75],   # 男
    [165, 50],   # 女
    [175, 70],   # 男
    [155, 45]    # 女    
])
# 创建训练数据

y_train=np.array(['男','女','男','女','男','女'])
# 创建对应数据标签

knn=neighbors.KNeighborsClassifier(n_neighbors=3)
# 创建预测模型并设置邻居数(进行参考的最近数据数量)

knn.fit(x_train,y_train)
# 存入数据和对应数据的标签

new_train=np.array([
    [168,60],
    [170,80]
])
# 创建需要训练的目标

new=knn.predict(new_train)
# 将样本放进打包好的预测模型预测并返回预测的一维数组标签
i=len(new_train)
while i>0:
    if new[i-1]=='男':
            print("性别为男")
    else:
        print("性别为女")
    i-=1
    