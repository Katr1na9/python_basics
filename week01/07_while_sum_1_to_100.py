#写在最前：if适用于：遍历一组固定的范围
# 而while适用于满足条件就一直循环
number=0
total=0
while number<=100:
    total=total+number
    number=number+1
print("while循环计算1到100的和",total)