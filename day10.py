#python challenge 10
# Day 10: Hide my Password  
# Write a function called hide_password that takes no 
# parameters.  The  function  takes  an  input  (a  password)  from  a 
# user  and  returns  a  hidden  password.  For  example,  if  the  user 
# enters ‘hello’ as a password the function should return ‘****’ as 
# a password and tell the user that the password is 4 characters 
# long.  
# Extra Challenge:  A Thousand Separator  
# Your new company has a list of figures saved in a list. The issue 
# is  that  these  numbers  have  no  separator.  The  numbers  are 
# saved in the following format: 
# [1000000, 2356989, 2354672, 9878098]. 
  
# You have been asked to write a code that will convert each of the 
# numbers in the list into a string. Your code should then add a 
# comma on each number as a thousand separator for 
# readability.  When  you  run  your  code  on  the  above  list,  your 
# output should be: 
 
# [ '1,000,000', '2,356,989', '2,354,672', '9,878,098’] 
 
# Write a function called convert_numbers that will take one 
# argument, a list of numbers above. 
  

import sys




def hide_password():
    password = input("Password: ")
    obfuscate_pass  = []
    for item in range(len(password)):
        obfuscate_pass.append("*")


    str_pass = "".join(obfuscate_pass)
    #str_pass2 = "*".join([str(item) for item in password])
    
    
    str_pass2 =  len(password) * "*"

    print(str_pass, len(password))

    


#hide_password()


def convet_numbers(num):
    num_seperate = ["{:,.3f}".format(item) for item in num]

    num_seperate2 = [f"{item:,.3f}" for item in num]
    
    
    num_seperate3 = []
    for item in num:
        num_seperate3.append("{:,.3f}".format(item))
        
        
    offset = 3
    for item in num:
        for next_item in item:
            next_item.insert(",", offset)

    for item in num_seperate:
        print(item)


num_list = [1000000, 2343424, 2657827, 4882357]
convet_numbers(num_list)


print(sys.int_info)