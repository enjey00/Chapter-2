# D = Down вниз; U = Up вверх
sum_of_steps = ['U','D','D','D','U','D','U','U']
def counting(steps):
    step = 0
    valley = 0

    for i in steps:
        if i == 'U':
            step = step + 1
            if step == 0:
                valley = valley + 1
        elif i == 'D':
            step = step - 1
    return(valley)
print(counting(sum_of_steps))