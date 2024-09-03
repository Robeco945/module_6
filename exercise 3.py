print('exercise 3')

gal = float(input('enter your gasoline amount in gallons: '))
def convert():
    li = gal * 3.78541
    return li
print(f'{gal} gallons = {convert():.3f} liters')