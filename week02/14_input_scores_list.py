scores=[]
#scores是一个空表

for i in range(5):
    score=input("请输入一个数：")
    score=int(score)
    scores.append(score)
    #这句的意思是将用户输入的score全都添加到scores这个表里

print("你所输入的所有分数是:",scores)

total = 0

for score in scores:
    total = total + score

average = total / len(scores)

print("总分:", total)
print("平均分:", average)