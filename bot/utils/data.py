# DB allows us to save and access information from replits database
from replit import db

# All the program configuration settings
class DATA:
   def __init__(self): 
     pass

   # function to get value of _age 
   def get_age(self): 
       return db['age']

   # function to set value of _age 
   def set_age(self, a): 
       db['age'] = a 

   # function to delete _age attribute 
   def del_age(self): 
       del db['age']

   age = property(get_age, set_age, del_age)  
