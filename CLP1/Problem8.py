def sum_numbers(*args):
    addition = 0
    for i in args:
        addition += i
    return addition
print(sum_numbers(1,2,3,4,5,6,7,8,9,10))
