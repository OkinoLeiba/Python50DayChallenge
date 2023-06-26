#python challenge day17
# Day 17: User Name Generator  
# Write  a  function  called  user_name,  that  creates  a  username 
# for the user. The function should ask a user to input their name. 
# The function should then reverse the name and attach a 
# randomly issued number between 0 – 9 at the end of the name. 
# The function should return the username. 
 
# Extra Challenge: Sort by Length  
# names = [ "Peter", "Jon", "Andrew"] 
# Write a function called sort_length that takes a list of strings 
# as an argument, and sorts the strings in ascending order 
# according  to  their  length.  For  example,  the  list  above  should 
# return: 
# ['Jon', 'Peter', 'Andrew'] 
# Do not use the built-in sort functions

import sys, random


class NameGenerator:
    def __init__(self) -> None:
        pass
    
    
    
    def user_name(self) -> None:
        input_name = input("Enter User Name: ")
        new_name = input_name[::-1]+str(random.randrange(0,9))
        print(new_name)
        print(input_name)
        
        
name_generator = NameGenerator()
#name_generator.user_name()



def sort_length(input_len: list) -> None:
    
    sort_length = sorted(input_len, key=max, reverse=False)
    #sort_list = [iterable.sort() for iterable in input_len lambda x: len(input_len)]
    dict_list = {}
    for iterable in input_len:
        dict_list[len(iterable)]=iterable
        
   
      
    #new_list = dict_list.values(list(int(dict_list.keys())).sort())
    key_list = list(dict_list.keys())
    key_list.sort()
    new_names = []
    for iterable in key_list:
        new_names.append(dict_list[iterable])
        
        
    # for iterable in range(len(input_len)):
    for idx in range(len(input_len)-1):   
        if len(input_len[idx]) > len(input_len[idx+1]):
            input_len[idx], input_len[idx+1] = input_len[idx+1], input_len[idx]    
        
        

    
    
names = [ "Peter", "Jon", "Jen", "Andrew"] 
sort_length(names)