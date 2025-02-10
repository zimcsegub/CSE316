lst = [2,3,4,5,22,34,45,55,6,12,11,15,13]
even_sum = 0
odd_sum = 0
for i in lst:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(even_sum)
print(odd_sum)
