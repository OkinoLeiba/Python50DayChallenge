#python challenge day4
# Day 4: Only Floats  
# Write a function called only_floats, which takes two 
# parameters a and b, and returns 2 if both arguments are floats, 
# returns 1 if only one argument is a float, and returns 0 if neither 
# argument is a float. If you pass (12.1, 23) as an argument, your 
# function should return a 1. 
 
# Extra Challenge: Index of the Longest Word 
  
# Write a function called word_index that takes one argument, 
# a list of strings and returns the index of the longest word in the 
# list. If there is no longest word (if all the strings are of the same 
# length), the function should return zero (0). For example, the list 
# below should return 2. 
 
# words1 = ["Hate", "remorse", "vengeance"] 
#     And this list below, should return zero (0) 
# words2 = ["Love", "Hate"]  

import sys, math



def only_floats(num1: float, num2: float) -> int:

    test_num1 = num1 % int(num1)
    test_num2 = num2 % int(num2)

    test1 = bool(test_num1 == 0)  
    test2 = bool(test_num2 == 0)

   

    # if test_num1 != 0 and test_num2 != 0:
    #     return 2
    # elif test_num1 != 0 or test_num2 != 0:
    #     return 1
    # else:
    #     return 0

    #test = float.is_integer(test_num)
    
    if type(num1) == float and type(num2) == float:
        return 2
    if type(num1) == float or type(num2) == float:
        return 1
    else: 
        return 0
    
    return 2 if type(num1) == float and type(num2) == float else 1 if type(num1) == float or type(num2) == float else 0

only_floats(200.00, 201)


def word_index(the_list: list) -> list|None:
    
    result_max = max(the_list, key=len)
    
    result = the_list.index(max(the_list, key=len))
    
    for word in the_list:
        if word == max(the_list, key=len):
            print(f"The longest word is at index {the_list.index(word)}")
        

    #new_list = [x.length(the_list) for x in the_list]
    i = 0
    while i < len(the_list)-1:
        if len(the_list[i]) > len(the_list[i+1]):
            the_list[i]
        i += 1
    print(f"The longest word is {the_list[i]}")
    print(the_list[i])


the_words = ["Hate", "remorse","vengeance"]
the_words2 = ["hate", "love"]

word_index(the_words)