students=[]

for i in range(3):
    name = input("请输入学生姓名:")
    score = input("请输入学生分数:")
    score=int(score)

    student={
        "name":name,
        "score":score
    }
    #将name和score打包成一个完整的student放到列表中，即定义字典
    students.append(student)

print("所有学生信息:")
print(students)

print("逐个输出学生成绩:")

for student in students:
    #已经将students里面的每一个元素取出来放在了student里面储存
    name = student["name"]
    score = student["score"]

    if score>=60:
        result="及格"
    else:
        result="不及格"
    
    print(name,"的分数是",score,"结果是:",result)
