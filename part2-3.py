num = float(input('Введите целое число: '))

if num %1 == 0:
    num = round(num)
    print("\n", (num-1), (num), (num+1))
else:
    print("Только целые числа!!!")
