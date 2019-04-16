'''
   Author:Guiping Liu
   Fucntion:Homework.
   Version；1.0
   Date:2019-04-16
'''
import matplotlib.pyplot as plt
import numpy as np
a=[]
c=[]
b=["安晓芳","陈德阳","陈骏然","陈奇华","陈文慧","陈展洛","邓俊熙",
"邓雯薇","方泽莉","何昕豫","洪英霓","胡礼浩","黄耀骏","黄玉兰",
"赖广楠","李百诚","连梦雨","梁泽邦","廖楚裕","林文健","林智铭",
"罗硕浩","吕俊荣","吕心怡","孙璐","唐嘉","涂似萍","王美","吴铱淳",
"谢志阳","许佳慧","许俊旭","杨楚凡","姚雅雯","叶满庭","俞倩滢",
"詹盛尧","张晓庆","郑丽婷","周丹婷","周宏宇","周榆","邹阳","唐明轩"]
for i in range(45):
    a.append(i)
for i in range(151608001,151608045):
    c.append(i)

for i in range(45):
    print("三8班")
    print(a[i+1],c[i],b[i])#列表a为学生所在成绩表中的顺序以及所在的列数，列表b为学生姓名，列表c为学生学号
    
    params = dict(
    fname = R"C:\Users\HUAWEI\Desktop\python\三81.csv",#打开文件三81.csv
    delimiter = ',',
    usecols = (0,a[i+1]),#取出文件三81.csv中的0列以及a[i+1]列

    unpack = True
    )
    date,score= np.loadtxt(**params)
    print(date)
    print(score)

    x=date
    y=score
    plt.plot(x,y)#画图
    plt.show()
#由于作者能力有限，此程序功能不完善，每次只能读出一位
# 学生的成绩图，且要关闭上一图时才能跳到下一个学生的成绩图。