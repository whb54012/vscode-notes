from sklearn.preprocessing import MinMaxScaler
from sklearn import neighbors
import numpy as np
# MinMaxScaler归一化公式为(当前值-最小值)/(最大值-最小值)
# 范围设置到[0,1]之内
# 适用场景,受异常值影响大	

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

scaler=MinMaxScaler()
# 创建归一化工具，选择MinMaxScaler或StandardScaler归一化

x_newtrain=scaler.fit_transform(x_train)
# 将原始数据归一化并得到最大最小值

knn=neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(x_newtrain,y_train)
# 创建容器并存入数据

new_train=np.array([
    [168,60],
    [170,80]
])#训练数据
newtrain=scaler.transform(new_train)
# 用已经得到的最大值和最小值去归一化

new=knn.predict(newtrain)
i=len(new_train)
while i>0:
    if new[i-1]=='男':
            print("性别为男")
    else:
        print("性别为女")
    i-=1
