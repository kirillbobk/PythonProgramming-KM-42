print('Hello!')
list1 = []

while True:

    #Element input line. 
    item = str(input('Enter the items to complete the entry, press "0": '))
    
    if (item == '0'):
        break
    else:
        list1.append(item)
        continue

#Element output line.
for i, elem in enumerate(list1):
    
    if ((i + 1) < len(list1)): 
        print(f'{elem}, ', end='')
    else:
        print(f'and {elem}')
    
print('Goodbye!') 