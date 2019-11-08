a = int(input('Введите целое число: '))
b = int(input('Введите число побольше: '))
print("Выведены все числа от", a, "до", b, ":")
for i in range(a-1, b):
    print(i+1)