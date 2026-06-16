even_count=0
odd_count=0
for number in range(1,101):
    if number%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1

print("1到100中偶数的数量:",even_count)
print("1到100中奇数的数量:",odd_count)