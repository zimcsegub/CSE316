n = int(input("Enter a number: "))
lst = []
num1 = 0
num2 = 1
lst.append(num1)
lst.append(num2)
for i in range(n):
    num3 = num1 + num2
    lst.append(num3)
    num1 = num2
    num2 = num3
print(lst)
