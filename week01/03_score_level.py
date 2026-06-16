score=input("输入你的分数：")
#在input（）中保存的是字符串，假设我输入88，所得到的并不是数字88而是字符串“88”
print("转换前：",score,type(score))
score=float(score)
#右边的score是上一行中有的score，左边的score是用来接受新结果的score，这个左边的score才是进入下一行进行判断的score，执行顺序是先看右边，再赋值给左边
print("转换后：",score,type(score))
if score>=98:#注意此处是：不是；表示的意思是如果这个条件成立，即执行下面缩进的代码
    print("优秀")
elif score>=60:#表“否则”，“如果又...”
    print("合格")
else:
    print("不合格")
