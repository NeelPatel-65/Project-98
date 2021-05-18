PetrolPrice= input('Enter Price of Petrol : ')  
DieselPrice = input('Enter Price of Diesel : ')  
 
temp = PetrolPrice 
PetrolPrice = DieselPrice  
DieselPrice = temp  
  
print('The Price of Petrol after swapping: {}'.format(PetrolPrice))  
print('The price of Petrol after swapping: {}'.format(DieselPrice))  