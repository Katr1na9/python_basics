scores=[88,29,68,28,100,71]
print("所有分数:", scores)

max=scores[0]
min=scores[0]
#先把列表里的第一个分数，当作“暂时的最高分”和“暂时的最低分”。

pass_count=0
fail_count=0

for score in scores:
    if score>=max:
        max=score
    if score<=min:
        min=score
    if score>=60:
        pass_count=pass_count+1
    else:
        fail_count=fail_count+1

print("最高分:",max)
print("最低分:",min)
print("及格的人数:",pass_count)
print("不及格的人数:",fail_count)

