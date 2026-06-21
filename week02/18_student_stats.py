students=[]

for i in range(3):
    name = input("请输入学生姓名:")
    score = input("请输入学生分数:")
    score = float(score)

    student = {

        "name" : name,
        "score" : score
    #选择：而不是=
    }

    students.append(student)

print("所有学生信息:")
print(students)

total=0
max=students[0]["score"]
min=students[0]["score"]
    #这一句是在循环之前写的，所有还没有student这个临时变量
    #先拿第一个学生的分数当作临时最高分和最低分

for student in students:
        score=student["score"]
        total=total+score

        if score>=max:
            max=score
        
        if score<min:
            min=score

average=total/len(students)

print("总分:", total)
print("平均分:", average)
print("最高分:", max)
print("最低分:", min)