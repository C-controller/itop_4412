# #   print函数用法   #  
# print("\nxixi") #原样输出双引号中的内容，\n是转义字符，输出换行符。
# print("\u03c0") #输出π，\u转义序列可以显示Unicode字符，每个字符用16进制表示
  
# #  定义变量    #
# cup = 1;    #直接定义变量并赋值，不需要说明类型
# print(cup)
# print("hao","gege") #默认在两个字符串之间添加空格
# print("cup = " + str(cup))    # 字符串相加 
# type(cup)   #查看变量数据类型
# cup = input("how many cups? ")  #键盘输入，默认输入类型保存成字符串
# print(type(cup))    #此时cup是str类型
# cup = int(cup) #强制类型转换
# print(type(cup))

# #   算术    #
#   // 整除     ** 求幂      and， or， not 逻辑与 或 非    ~ 求二进制补码
# a = 0b0101
# print(bin(a)) # bin()函数将以二进制表示
# s = 5.3*9 
# print(s)    #默认采用浮点数表示
# print("answer: {0:.2f}".format(s))  #{}中0定义开始显示的数字，.2定义显示位数
# from fractions import Fraction  # fractions定义特殊对象 Fraction。Fraction对象包含分子分母
# #作为对象的独立属性， 所有Fraction对象均可进行算术运算
# test = Fraction(1,3)
# print(test)
# test2 = Fraction(3.3)  #可以将浮点数转换成Fraction对象
# print(test)
# fu = complex(1,3) #创建复数
# print(fu)
# import math #引入math模块，内涵高级数学功能
# print(math.factorial(5)) # 5！ = 120
# from math import factorial # 从math库中引入factorial函数，在多次使用时方便
# print(factorial(5))
# import numpy
# a = numpy.array(([1,2,3],[0,2,4],[3,5,1]))
# print(a) # numpy库有许多函数处理数组，需要用时再了解

#   控制语句    #
# x = 5
# if (x == 5):        #if_else 语句，:后接执行语句，执行代码部分不需要用括号，用缩进表示那一块属于if/else 
#     print("x = 5")
# else:               #if_else 必须在同一列，不能缩进
#     print("x != 5")

# if (x > 100 and x < 1000):    # 多种条件用 and or not (与或非)连接     
#     print("big")
# elif (x > 50):      #elif 相当于else if
#     print("medium")
# else:
#     print("small")

# #   字符串比较  #   从第一位开始比较，字符ASCII码大的字符串更大，除非相等，不然不再继续比较下一位
# str1 = "d"
# if (str1 == "bcd"):
#     print(str1)
# elif (str1 < "bcd"):
#     print("less")
# elif (str1 > "bcd"):
#     print("more")

#   循环    #   
# for number in [1,2,3]:      # for+循环变量+[数字或字符串都可以]，循环会依次为number赋值，循环次数取决于元素个数
#     print(number)
# for number in range(3):     # 依次将0~2赋值给number，range（x）只接受整数作为参数,从 0 到 x-1
#     print(number)
# for number in range(1,4):   # number从1~3, 只能是升序，从 1 到 4-1
#     print(number)
# for number in range(2,11,2):    # range(start,stop,step)，从2~10，步进为2
#     print(number)
# for number in range(10,2,-2):   # 10~3, 步进为-2
#     print(number)
##   for语句中可以使用break跳出循环   ##

# number = 1
# while number <= 5:      # while循环
#     print(number)
#     number += 1

# while True :
#     number += 1
#     if (number == 8):
#         print(number)
#         break

#   文件操作    #
# import os     # 更多os功能自行查找
# print(os.getcwd())   # 显示当前目录
# files = open('F:/py3/exp_1/my_test.txt','r') # a:从文件结尾追加内容，文件不存在就创建它 r:读取文件  
# #w:打开文件从头写入，如果不存在就创建文件 # a+, w+, r+ ：1、文件指针会指向开头 2、表示读取和追加、写入都可以
# print(files.tell())
# print(files.closed)      # 查看文件是否被关闭
# print(files.mode)      #查看文件使用模式
# print(files.name)      #查看文件名称    
# data = files.read() # 读取文件全部内容并以字符串形式返回，read函数可以添加参数，如 read(4)表示读四个字符
# print(data)
# data = files.readline() # 读文件一行 其实什么都没有读到，因为前面已经读完了，指针指向文件结尾
# print(data,end = '') # 因为print函数末尾自带换行，通过end=''抑制，否则会输出两个换行符（print自带+读取文件结尾换行符）
# # 注意：读取后文件指针会改变！！！
# print(files.tell())   # 返回文件指针位置  
# files.seek(0)       #.seek() 改变文件指针位置
# print(files.tell())
# data = files.read(1)  
# print(data)
# files.close()

# import os
# print(os.listdir('F:/py3/exp_1')) # 显示目录下文件
# file2 = open('F:/py3/exp_1/temp.txt','w') # 写模式会擦除文件全部内容, W+表示可以读写，但一样会擦除全部内容
# print(os.listdir('F:/py3/exp_1'))
# date = 'come on man' + '\n' + 'come on'
# file2.write(date)       # 写入函数的参数只能是字符串！！
# file2.close()
# file3 = open('F:/py3/exp_1/my_test.txt','a') # 在文件结尾追加
# file3.write(date)
# file3.close()

##      使用函数        ##
#       def name(num1,str = 'Hi!',arm = 10):
        #   statement
        #   return value
        # 缩进表示函数体， 调用函数时如果直接传递字符串str时必须用引号括起来：name(a,'Hello')
        # arm,str是默认参数值 如果想给第三个参数传值，第二个参数使用默认值可以 name(a,arm = 0)
##  字符串、整数、元组是不可变对象，采用值传递，列表、字典、集合是可变对象采用引用传递
# def name(x, str = 'Hi', arm = 10):
#     print(x,str,arm)
# name(2,arm = 5)  

## 求和函数 ##                               
# def add(*arg):      # arg是可变数量参数，类似数组使用
#     sides = len(arg)
#     total = 0
#     for i in range(0,sides):
#         total += arg[i]
#     return total
# add1 = add(1,5,6)
# print(add1)

##      列表和元组      ##
# tup = ()        # 空元组
# tuple1 = 1, 2, 3   # 定义元组，数据值可以是数字或字符串,但元组在定义后不可改变数据！！！
# print(tuple1)       # 元组只有一个数据时需加逗号，以区分整型和str类型
# tup = "a"
# print(type(tup))
# tup = "a",
# print(type(tup))
# tuple2 = ("mom","dad",3)    # 可以不加括号
# print(tuple2)
# tuple3 = tuple1[0:1]    # 切片访问元组数据，元组下标从0开始
# print(tuple3)           # 参数是单个数字是类似于数组，参数是范围时会比参数范围少一
# tup2 = tuple2[0:3:2]    # 下标 0~3,步进为2 取元组第一。第三个数据
# print(tup2)
# tup = tuple1[1:]        # 从下标一以后全取
# print(tup)
# if 2 in tuple1 :        # num in tuple 判断元组中是否含有某元素
#     print("tuple1含有1")
# print(len(tuple2))      # 求元组长度
# print(min(tuple1),max(tuple1))    # 求元组最值
# print(tuple1 + tuple2)  # 元组拼接

# list1 = []      # 空列表
# list1 = [1,2,3,4]   
# tup = 1,2,5
# list2 = list(tup)     # 元组和列表可以相互转换
# print(list2)
# tup = tuple(list1)
# print(tup)

# list2 = [1, 2, 3, 4, 5, 6, 7 ]
# print(list2[0])
# print(list2[0:2])   # 与元组一样，参数是范围时实际范围会比参数范围少一
# del list2[1]        # 删除列表元素,参数可以是范围如1:5
# print(list2)
# list2.append(8)
# print(list2)  # append()在列表末尾插值
# list2.insert(1,2)
# print(list2)    # insert() 在指定位置插值
# list2.pop()     # 根据索引值指定位置弹出一个值，后方元素向前移位，无参数弹出最后一个元素
# print(list2)
# # 其他如步进选取，判断是否包含某元素，拼接均和元组相同
# x = 1
# if x in list2:
#     print(list2,"含有", x)

# a = ['x','y','z']
# b = [1,5,3]
# x = [a,b]       # 嵌套列表
# print(x)
# print(x[0])
# print(x[1][1])  # 类似多维数组

##    模块引用    ##
# import printing # 相当于多文件结构，所有自建的py文件都要放在同一文件夹里
# printing.shows()    # 这样做并没有把直接定义在fibo中的函数名称写入到当前符号表里
# ## 只是把模块fibo的名字写到了那里 所以调用printing模块内的函数需要用点语法
# ## from...import*    将模块所有内容导入，不推荐使用
# import printing     # 什么都不会执行，因为不会引用模块两次
# from printing import inputs   # 从模块中引入你想要的函数
# x = inputs()  # 引入后可以直接使用函数
# print("You input:",x)  
# print(dir(printing))
def delay_us():
    k = 0
    while(k < 5000):
        k += 1

import time
import datetime
#print(dir(time))
start = datetime.datetime.now() 
# k = 0
# while(k < 2000):
#         k += 1
delay_us()
end = datetime.datetime.now() 
print(end-start)
