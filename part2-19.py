your_weight = int(input('How much do you weight?\n '))
w_on_moon = your_weight * 0.165

def your_weight_for_15_years():
	x = 0
	while x <= 15:
		yearly = w_on_moon + x
		date = 2019 + x
		x = x + 1
		print(f'Your weight on the moon in {date} will be: {yearly}')

your_weight_for_15_years()