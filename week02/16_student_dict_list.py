students=[
    {"name":"katrina","score":88},
    {"name":"nier","score":44},
    {"name":"onyx","score":99},
    {"name":"gaby","score":57}
]
#意为students这个列表里每一个{}里的元素都是一个字典

print("所有学生信息:")
print(students)

print("逐个输出学生成绩:")

for student in students:
    name=student["name"]
    score=student["score"]

    if score>=60:
        result="及格"
    else:
        result="不及格"

    print(name,"的分数是",score,"结果是：",result)
