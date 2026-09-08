from sklearn.preprocessing import StandardScaler
from sklearn import neighbors
import numpy as np
#StandardScaler标准化公式为标准化结果=(当前数据-平均数)÷标准差
# 适用场景	数据近似正态分布,受异常值影响小

x_train=np.array([
    [170, 65],   # 男
    [160, 55],   # 女
    [180, 75],   # 男
    [165, 50],   # 女
    [175, 70],   # 男
    [155, 45]    # 女 
])
# 创建原始数据

y_train=np.array(['男','女','男','女','男','女'])
# 创建对应标签

scaler=StandardScaler()
# 创建标准化工具
x_newtrain=scaler.fit_transform(x_train)
# 将原始数据标准化并得到平均数和标准差

knn=neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(x_newtrain,y_train)
# 创建容器并存入数据

new_train=np.array([
    [168,60],
    [170,80]
])#训练数据
newtrain=scaler.transform(new_train)
# 用已经得到的平均数和标准差去标准化

new=knn.predict(newtrain)
i=len(new_train)
while i>0:
    if new[i-1]=='男':
            print("性别为男")
    else:
        print("性别为女")
    i-=1
