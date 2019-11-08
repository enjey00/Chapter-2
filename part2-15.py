number = int(input('Введите Ваше число: '))

for nums in range(number+1):
    square = nums * nums
    if square >= number:
        print(f'{nums} * {nums} = {square}')