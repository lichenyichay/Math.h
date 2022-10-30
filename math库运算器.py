# -*- coding:UTF-8 -*-
# @Author:Chay
# @TIME:2022/10/25 20:44
# @FILE:math库运算器.py
# @Software:IntelliJ IDEA Community Edition 2022.2.1
import math


def z():
    while True:
        a = input("请输入功能（exit退出）：")
        if a == "取大于等于x的最小的整数值":
            b = input("请输入数据：")
            b = math.ceil(float(b))
            print(b)
        elif a == "把y的正负号加到x的前面":
            b = float(input("请输入第一个数据："))
            c = float(input("请输入第二个数据："))
            d = math.copysign(b, c)
            print(d)
        elif a == "求x的余弦":
            b = input("请输入数据：")
            b = math.cos(float(b))
            print(b)
        elif a == "把x从弧度转换成角度":
            b = float(input("请输入数据："))
            b = math.degrees(b)
            print(b)
        elif a == "求数学常量e":
            b = math.e
            print(b)
        elif a == "求数学常量pi":
            b = math.pi
            print(b)
        elif a == "求x的整数部分":
            b = input("请输入数据：")
            b = math.trunc(float(b))
            print(b)
        elif a == "求x的正切值":
            b = input("请输入数据：")
            b = math.tan(float(b))
            print(b)
        elif a == "求x的平方根":
            b = float(input("请输入数据："))
            b = math.sqrt(b)
            print(b)
        elif a == "求x的正弦值":
            b = input("请输入数据：")
            b = math.sin(float(b))
            print(b)
        elif a == "角度x转换成弧度":
            b = input("请输入数据：")
            b = math.radians(float(b))
            print(b)
        elif a == "求x的y次方":
            b = float(input("请输入第一个数据："))
            c = float(input("请输入第二个数据："))
            d = math.pow(b, c)
            print(d)
        elif a == "输出由x的小数部分和整数部分组成的元组":
            b = float(input("请输入数据："))
            b = math.modf(b)
            print(b)
        elif a == "求x以a为底的对数":
            b = int(input("请输入第一个数据："))
            c = int(input("请输入第二个数据："))
            d = math.log(b, c)
            print(d)
        elif a == "求x*（2**i）的值" or a == "求x*(2**i)的值":
            while True:
                try:
                    b = float(input("请输入第一个数据："))
                except ValueError:
                    print("数字无效！")
                else:
                    break
            while True:
                try:
                    c = int(input("请输入第二个数据："))
                except ValueError:
                    print("数字无效！")
                else:
                    break
            d = math.ldexp(b, c)
            print(d)
        elif a == "求x是不是数字":
            b = float(input("请输入数据:"))
            c = math.isnan(b)
            if c:
                print("不是数字")
            else:
                print("是数字")
        elif a == "求x是不是正无穷大或负无穷大":
            b = int(input("请输入数据："))
            b = math.isinf(b)
            if b:
                print("是正无穷大或负无穷大")
            else:
                print("不是正无穷大或负无穷大")
        elif a == "求(x的平方+y的平方)的值":
            b = float(input("请输入第一个数据："))
            c = float(input("请输入第二个数据："))
            d = math.hypot(b, c)
            print(d)
        elif a == "求x和y的最大公约数":
            b = int(input("请输入第一个数据："))
            c = int(input("请输入第二个数据："))
            d = math.gcd(b, c)
            print(d)
        elif a == "对多个元素进行求和":
            b = []
            c = int(input("请输入元素个数："))
            for i in range(c):
                d = int(input("请输入元素"))
                b.append(d)
            b = tuple(b)
            b = math.fsum(b)
            print(b)
        elif a == "求x/y的余数":
            b = float(input("请输入第一个数据："))
            c = float(input("请输入第二个数据："))
            d = math.fmod(b, c)
            print(d)
        elif a == "求小于等于x的最大的整数值":
            b = float(input("请输入数据："))
            b = math.floor(b)
            print(b)
        elif a == "求x的阶乘的值":
            b = int(input("请输入数据："))
            b = math.factorial(b)
            print(b)
        elif a == "求x的绝对值":
            b = float(input("请输入数据："))
            b = math.fabs(b)
            print(b)
        # elif a == "求math.e的x次方减1":
        #     b = float(input("请输入数据："))
        #     b = math.exp1(b)
        #     print(b)
        elif a == "求math.e的x次方":
            b = float(input("请输入数据："))
            b = math.exp(b)
            print(b)
        elif a == "exit":
            print("感谢您的使用！")
            break
        else:
            print("暂不支持此功能！")


z()
