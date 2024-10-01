print('Hello!')

salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
list1 = []
list2 = []

for a in salary_list:    
    list1.append(((a / 100) * 30))

for a, b in zip(salary_list, list1):
    list2.append(a + b)    

print('Salary table:')

for a, b, c in zip(salary_list, list2, list1):
    print(a,'',round(b, 2),'', round(c, 2)) 

print('Goodbye!') 