num1=input("请你输入第一个数字:")
operator=input("请你输入运算符号（+、-、*、/):")
num2=input("请你输入第二个数字:")
num1=float(num1)
num2=float(num2)

if operator=="+":
    result=num1+num2
    print("计算结果是：",result)
elif operator=="-":
    result=num1-num2
    print("计算结果是：",result)
elif operator=="*":
    result=num1*num2
    print("计算结果是：",result)
elif operator=="/":
    if num2==0:
        #判断除数不为0
        print("错误:除数不能为0")
    else:
        result=num1/num2
    print("计算结果是：",result)
else:
    print("错误:不支持该运算符")