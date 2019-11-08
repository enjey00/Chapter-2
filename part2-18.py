your_age = int(input("Введите Ваш возраст: "))

if your_age % 2 == 0:
  for even_numbers in range(2,your_age,2):
      print(even_numbers)
else:
    for odd_numbers in range(1,your_age,2):
        print(odd_numbers)