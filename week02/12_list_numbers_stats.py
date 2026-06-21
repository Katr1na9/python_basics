scores=[88,29,89,28,71,100]
print("所有分数:",scores)
print("分数数量:",len(scores))

total=0
for score in scores:
    total=total+score
print("总分数是:",total)

average=total/len(scores)
print("平均分是:",average)

max=0
for score in scores:
    if score>=max:
        max=score
print("最高分是:",max)



