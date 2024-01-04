#python challenge day28
# Day 28: Return Indexes  
# Write a function called index_position. This function takes a 
# string as a parameter and returns the positions or indexes of all 
# lower  letters  in  the  string.  For  example,  ‘LovE’  should  return 
# [1,2]. 
 
# Extra Challenge: Largest Number  
# Write  a  function  called  largest_number  that  takes  a  list  of 
# integers and re-arrange the individual digits to create the largest 
# number  possible.  For  example,  if  you  pass  the  following  as  an 
# argument: list1 = [3, 67, 87, 9, 2]. Your code should return the 
# number in this exact format: 9,877,632 as the largest number.





def index_position(str_eval: str) -> None:
    new_list = [str_eval.index(letter) for letter in str_eval if letter.islower()]
    new_list2 = [letter for idx, letter in enumerate(str_eval) if letter.islower()]
    
    indez = []
    indey = []
    for idx, letter in enumerate(str_eval):
        if letter.islower():
            indez.append(idx)
            indey.append(str_eval.index(letter))
    # result = str_eval.index(str_eval.islower())
    # print(result)
    
    
    
str_eval = "LovE"   
# index_position(str_eval)

def largest_number(num_input: list) -> None:
    result = [num for num in num_input for digit in str(num)]
    
    result_list = []
    for num in num_input:
        for digit in str(num):
            result_list.append(digit[0])
            result_list.sort(reverse=True)
    result2 = sorted(num_input, reverse=True)
    
    
    result_list2 = []
    for num in num_input:
        result_list2.append(int(num[0]))
        result_list2.sort(reverse=True)
    pass
   
   
   
num_input = [3, 67, 87, 9, 2] 
largest_number(num_input)