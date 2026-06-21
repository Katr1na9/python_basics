def check_pass(score):
    if score>=60:
        return "及格"
    else:
        return "不及格"
#如果只是想看一下结果：可以 print
#如果后面还要继续用这个结果：用 return
score1=88
score2=28
score3=99

result1=check_pass(score1)
result2=check_pass(score2)
result3=check_pass(score3)

print(score1, "的结果是:", result1)
print(score2, "的结果是:", result2)
print(score3, "的结果是:", result3)