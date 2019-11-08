class_A = int(input('Введите количество студентов в классе А: ').strip())
class_B = int(input('Введите количество студентов в классе В: ').strip())
class_C = int(input('Введите количество студентов в классе С: ').strip())

a = (class_A)
b = (class_B)
c = (class_C)

if a % 2 == 0:
    a = a//2
else: 
    a = a//2+1

if b % 2 == 0:
    b = b//2
else: 
    b = b//2+1

if c % 2 == 0:
    c = c//2
else: 
    c = c//2+1

stu_sum = (class_A + class_B + class_C)
desk_sum = (a + b + c)

print(
    "\nВ классе А", class_A, "студентов, которым нужны", a, "парт!",
    "\nВ классе В", class_B, "студентов, которым нужны", b, "парт!"
    "\nВ классе С", class_C, "студентов, которым нужны", c, "парт!"
    "\n\nВ трех классах всего у нас", stu_sum, "студентов и нам нужны", desk_sum, "парт!")
