#python challenge day11
# Day 11: Are They Equal?  
# Write a function called equal_strings. The function takes two 
# strings as arguments and compares them. If the strings are equal 
# (if  they  have  the  same  characters  and  have  equal  length),  it 
# should return True, if they are not, it should return False. For 
# example, ‘love’ and ‘evol’ should return True. 
 
# Extra Challenge: Swap Values  
# Write a function called swap_values. This function takes a list 
# of  numbers  and  swaps  the  first  element  with  the  last  element. 
# For  example,  if  you  pass  [2,  4,67,  7]  as  a  parameter,  your 
# function should return 
#  [7, 4, 67, 2]. 
  

import sys




def equal_strings(thing1: str ,thing2: str) -> bool:
      
    test1 = sorted(thing1) 
    test2 = sorted(thing2)
    
    
    if thing1 == thing2 and len(thing1) == len(thing2):
        print(True)
        return True
    else:
        print(False)
        return False
   


equal_strings("thing1", "thing2")



def swap_values(num_list: list) -> list|None:

    #num_list[0], num_list[len(num_list)-1] = num_list[len(num_list)-1], num_list[0]

    first_num = num_list.pop(0)
    last_num = num_list.pop(len(num_list)-1)

    num_list.insert(len(num_list), first_num)
    num_list.insert(0, last_num)

    """num_list.insert(num_list[0],num_list[len(num_list)-1])
    num_list.pop(len(num_list)-2)
    num_list.insert(num_list[len(num_list)-2], num_list[0])
    num_list.pop(2)"""
    print(num_list)

    first_num = num_list[0]
    last_num = num_list[len(num_list)-1]
    
    num_list[0] = last_num
    num_list[len(num_list)-1] = first_num
    
    
    num_result = num_list[-1:] + num_list[1:-1] + num_list[0:1]
    
    


num_list = [134, 45, 45, 3, 7]
swap_values(num_list)



print(sys.flags)