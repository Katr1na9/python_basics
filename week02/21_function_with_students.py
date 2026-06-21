def check_pass(score):
    if score>=60:
        return "及格"
    else:
        return"不及格"
    
students = [
    {"name": "katrina", "score": 88},
    {"name": "onyx", "score": 10},
    {"name": "nier", "score": 99}
]

for student in students:
    name=student["name"]
    score=student["score"]
    result=check_pass(score)

    print(name,"的成绩是:",score,"结果是:",result)