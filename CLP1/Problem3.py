addition = 0
for i in range(50,101):
    if i % 3 == 0 and i % 5 != 0:
        addition += i
print("Total Sum: ", addition)
