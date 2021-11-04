# Students in deptwise
std_lists = [
    ('EEE', 50),
    ('CSE', 60),
    ('Civil', 45),
    ('Mechanical', 40),
    ('Architecture', 30)
]

students = list(map(lambda student: student[1], std_lists))

# for student in students:
print(students)

