name = str(input('Введите Ваше имя:'))
sur_name = str(input('Введите Вашу фамилию:'))
name = name.strip()
sur_name = sur_name.strip()
full_name = name + " " + sur_name
print("Привет,", full_name.title() + "!",)