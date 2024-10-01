print('Hello!')

try:
    time = float(input('Enter the number of minutes: '))

    if (time < 0):
        print('Your number is negative.')
    
    elif (time <= 50): 
        print('100 hryvnia')
    
    elif (time > 50 and time <= 100):
        print('150 hryvnia')

    else: 
        print((((time - 100) * 2) + 150),'hryvnia')   


except ValueError:
    print('You can only enter positive numbers.')