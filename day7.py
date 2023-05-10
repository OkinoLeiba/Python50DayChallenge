#python challenge day7
# Day 7: A String Range  
# Write a function called string_range that takes a single 
# number and returns a string of its range. The string characters 
# should be separated by dots(.) For example, if you pass 6 as 
# an argument, your function should return ‘0.1.2.3.4.5’. 
 
# Extra Challenge: Dictionary of names  
# You are given a list of names, and you are asked to write a code 
# that returns all the  names that  start with ‘S’. Your code should 
# return  a  dictionary  of  all  the  names  that  start  with  S  and  how 
# many times they appear in the dictionary. Here is a list below: 
 
# names = ["Joseph","Nathan", "Sasha", "Kelly", 
#          "Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]  
# Your code should return: {“Sasha”: 1, “Sera”: 2}

import sys




def string_range(num_list: list, num: int) -> None:
    str_list = str(num_list)
    split_list = str_list.replace(",", ".")
    print(split_list)
    
    i = 0
    num_str = []
    num_str2 = ""
    while i < num: 
        # num_str2 += i
        num_str.append(str(i) + '.')
        i += 1
        
    str_list3 = ".".join(map(str, range(num)))     
    str_list2 = ".".join([str(number) for number in range(num)])
    
    
    


num_list = [1, 4, 5, 6, 7]

string_range(num_list, 6)


def dict_name(name_list: list) -> None:
    # name_list = str(name_list)
    s_list = [str(item) for item in name_list if item[0].lower() == "s"]
    dict_list = dict()
    i = 1
    while i < len(s_list):
        dict_list = {i : s_list[i-1]}
        i += 1

    dict_list2 = {}
    for name in name_list:
        if name.lower().startswith("s"):
            dict_list2.update({name:name.count(name)})
    # dict_list = dict(s_list)
    print(dict_list)

    dict_list3 = {name : name.count(name) for name in name_list if name.lower().startswith("s")}

names = ["Jonathon", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patei", "Sera", "Sera"]
dict_name(names)


print(sys.call_tracing)