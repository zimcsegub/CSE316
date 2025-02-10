students = (
    ("Alice", 20, 3.75),
    ("Bob", 22, 3.90),
    ("Charlie", 21, 3.50),
    ("David", 23, 3.95),
    ("Eve", 19, 3.80)
)

sorted_students = tuple (sorted (students, key=lambda x: x [2]))

print(sorted_students)
