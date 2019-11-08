numbers_list  = list(map(int, input("Введите любые числа через пробелы: ").split()))
for number in list(numbers_list):
    if number % 2 == 0:
        print(f"Выведены только четные числа:\t {number}")