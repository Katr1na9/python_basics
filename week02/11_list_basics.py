names=["katrina","nier","gaby"]
#是否是string要看有没有加引号
print("完整列表:",names)

print("第一个名字:",names[0])
#索引从0开始，即从第0个开始储存数组
print("第二个名字:",names[1])
print("第三个名字:",names[2])

print("列表里一共有多少个名字:",len(names))

names.append("onyx")
print("添加onyx之后的列表:",names)
print("添加之后的列表长度:",len(names))

print("逐个输出列表里的名字:")
for name in names:
    #name是临时创建的变量所以不用特别定义
    print(name)

#[]：列表，装多个数据
#()：函数调用，比如 print()、input()
#""：字符串
#input()：用户输入的内容默认是 str
#print()：负责输出，什么类型都能打印