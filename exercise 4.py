print('exercise 4')
li=  [1,2,3,4,5,6]
sum = 0
def calc(li):
    global sum
    for i in li:
        sum = sum + i
    print(sum)
    return
print(f'the sum of the numbers are {calc(li)}')