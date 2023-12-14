import pandas as pd

date = '20231127'

# 从txt文件里读取参会人员的名字
f2 = open('./input/'+date+'.txt',"r", encoding='utf-8')
lines = f2.readlines()

names = []
for line3 in lines:
    name = line3.split(' ')
    names +=name
    # print(names)


# 读取csv文件
files = './test.csv'
data = pd.read_csv(files , encoding='gbk')

# 在新的日期列里初始化
data['20231127'] = '未参会'


# 如果名字有出现就标记为参会
for name in names:
    data.loc[data['名字'] == name, '20231127'] = '参会'

data.to_csv('./output/'+ date +'.csv')

# print(list(data))