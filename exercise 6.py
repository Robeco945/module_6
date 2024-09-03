print('exercise 6')

size1 = float(input("enter the first pizza's diameters: "))
price1 = float(input("enter the first pizza's price in euros: "))
size2 = float(input("enter the second pizza's diameters in cm: "))
price2 = float(input("enter the second pizza's price in euros: "))

def unit(price1, size1):
    unitprice1 = price1/(size1/100 * size2/100 * 1/4 * 3.1415)
    return unitprice1
def unit(price2, size2):
    unitprice2 = price2/(size2/100 * size2/100 * 1/4 * 3.1415)
    return unitprice2
if unit(price1, size1) < unit(price2, size2):
    print('the first pizza is a better deal than the second pizza')
elif unit(price1, size1) > unit(price2, size2):
    print('the second pizza is a better deal than the first pizza')
else: print('both pizzas are the same in value')