#pyton challenge day9
# Day 9: Biggest Odd Number  
# Create  a  function  called  biggest_odd  that  takes  a  string  of 
# numbers  and  returns  the  biggest  odd  number  in  the  list.  For 
# example,  if  you  pass  ‘23569’  as  an  argument,  your  function 
# should return 9. Use list comprehension. 
 
# Extra Challenge: Zeros to the End  
# Write a function called zeros_last. This function takes a list as 
# argument. If a list has zeros (0), it will move them to the front of 
# the list and maintain the order of the other numbers in the list. 
# If  there  are  no Zeros  in  the  list,  the  function  should  return  the 
# original list sorted in ascending order. For example, if you pass 
# [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1, 
# 4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument, 
# your code should return [1, 2, 4, 6, 7].

import sys, ast, json





def biggest_odd(split_list: str, num_list: list) -> str:  
    #new_list = [str(split_list).split('')]
    test_list2 = []
    test_list2[:0] = split_list
    

    test_list3 = list(split_list)

    test_list = [int(item) for item in split_list]

    test_list4 = ast.literal_eval(split_list)

    test_list6 = [int(item) for item, key in enumerate(split_list)]

    test_list7 = list(map(int,split_list))

    test_list8 = [json.loads(split_list)]


    #new_list = [int(split_list)]
    test_list5 = [lambda item: item in split_list]
    
    fairly_odd_list = max([item for item in split_list if int(item) % 2 != 0])
    
    addams_family = [item for item in split_list if int(item) % 2 != 0][-1]
   
    odd_list = max([item for item in num_list if item % 2 != 0])

    return fairly_odd_list
    


split_list = "125678901316"
num_list = [1,2,5,6,7,8,9,0,13,16]
# biggest_odd(split_list, num_list)



def zero_list(num_list: list) -> None:
    for num in range(0,len(num_list)):
        if num_list[num] == 0:
            num_list.remove(0)
            num_list.append(0)
        else:
            num_list

    #new_list = [num for num in num_list if num_list == 0]
    
    
    i = 0  
    for num in num_list:  
        if num != 0:     
            num_list[i] = num 
            i += 1 
            
    heros= []
    zero = []
    for num in num_list:
        if num == 0:
            zero.append(num)
        else:
            heros.append(num)
            
    sorted(heros).extend(zero)
            
 
     
   

    
num_list2 = [1, 4, 6, 0, 7, 0]
zero_list(num_list2)