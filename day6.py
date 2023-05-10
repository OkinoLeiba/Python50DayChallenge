#python challenge day6
# Day 6: User Name Generator 
 
# Write a function called user_name that generates a username 
# from the user’s email. The code should ask the user to input an 
# email and the code should return everything before the  @ sign 
# as their user name. For example, if someone enters 
# ben@gmail.com,  the  code  should  return  ben  as  their  user 
# name.  
# Extra Challenge: Zero Both ends  
# Write a function called zeroed code that takes a list of numbers 
# as an argument. The code should zero (0) the first and the last 
# number in the list. For  example, if the input is  [2,  5,  7, 8,  9], 
# your code should return [0, 5, 7, 8, 0]. 
  

import sys, math, re




def user_name(user: str) -> None:
    user_split = user.split("@")
    name = user_split[0].replace(".", " ").title()
    name2 = re.sub(r"\W", " ", str(user_split)).title()
    print(name)
    




# str_input1 = "okino.leiba@yahoo.com"
# str_input2 = input("Input E-mail:")
# user_name(str_input1)

def zeroed(input: list) -> None:
    # end_range = len(input)-1
    # input[0] = 0
    # input[end_range] = 0
    
    input.pop(0)
    input.pop(-1)
    input.insert(0,0)
    input.insert(len(input), 0)

    print([0, *input[1:-1], 0])

    print(input)
    
  



num_list = [2 , 4, 7, 7 , 8, 14]
zeroed(num_list)


print(sys.__stdin__)
print(sys.__stdout__)