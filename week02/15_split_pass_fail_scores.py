scores=[78,28,100,47,99]

pass_list=[]
fail_list=[]

for score in scores:
#range()中需要存放整数，而不能存放列表
    if score>=60:
        pass_list.append(score)
    if score<60:
        fail_list.append(score)

print("所有分数:",scores)
print("及格分数:",pass_list)
print("不及格分数:",fail_list)
print("及格人数:",len(pass_list))
print("不及格人数:",len(fail_list))

