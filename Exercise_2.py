print('Hello!')
try:
    rating = int(input('Enter your rating:'))

    if (rating >= 0) and (rating < 60):
        print('Unsatisfactory')     
        print('Goodbye!') 
    
    elif (rating >= 60) and (rating < 65):          
        print('Marginal')
        print('Goodbye!')
    
    elif ( rating>= 65) and (rating < 75):
        print('Satisfactory')
        print('Goodbye!')  
    
    elif (rating >= 75) and (rating < 85):          
        print('Good')
        print('Goodbye!')    
    
    elif (rating >= 85) and (rating < 95):          
        print('Very good')
        print('Goodbye!')   
    
    elif (rating >= 95) and (rating <= 100):          
        print('Excellent')
        print('Goodbye!')
    
    #Executed if the number is negative.    
    elif (rating > 100) or (rating < 0):          
        print("Error. I can't determine your rating. Invalid input.")        
        print('Goodbye!')

except ValueError:
    print('You can only enter positive numbers.')