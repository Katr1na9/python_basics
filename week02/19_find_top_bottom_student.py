students=[]

for i in range(3):
#3次循环输入3个学生的信息
#还没收集数据时：用 range(3) 控制输入次数
#已经有数据之后：用 for student in students 遍历学生
    name=input("请输入学生的姓名:")
    score=input("请输入学生分数:")
    score=float(score)

    student={
        "name":name,
        "score":score
    }

    students.append(student)

top_student=students[0]
bottom_student=students[0]

for student in students:
    score=student["score"]
    if score>=top_student["score"]:
        top_student=student
    
    if score<bottom_student["score"]:
        bottom_student=student

print("所有学生信息:")
print(students)

print("最高分学生:", top_student["name"], "分数:", top_student["score"])
print("最低分学生:", bottom_student["name"], "分数:", bottom_student["score"])



