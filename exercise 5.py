print('exercise 5')
li=  [1,2,3,4,5,6]
sum = 0
def even(li):
    global sum
    for i in li:
        if i % 2 != 0:
            li.remove(i)
    print(li)
    return
print(f'the list with odd numbers removed: {even(li)}')