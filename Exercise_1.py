#Data entry block 
try:
    name = str(input('Enter your name: '))

    surname = str(input('Enter last name: '))

    num_phone = int(input('Enter phone number: '))

    street = str(input('Enter the street name: '))

    nom_house = int(input('Enter the house number: '))

    ap = int(input('Enter the apartment number:'))

    city = str(input('Enter a city: '))

    ind = int(input('Enter index: '))

    country = str(input('Enter country: '))

    #Data output block. 

    print(f'{name}, {surname}') 
    print(num_phone)
    print(f'Str. {street}, {nom_house}, ap. {ap}, {city}')
    print(ind)
    print(country)

except ValueError:
    print('You can only enter positive numbers.')