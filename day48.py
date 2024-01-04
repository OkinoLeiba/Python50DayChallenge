#python challenge day48
# Day 48: Binary Search 
 
# Write  a  function  called  search_binary  that  searches  for  the 
# number  22  in  the  following  list  and  returns  its  index.  The 
# function should take two parameters, the list and the item that 
# is being searched for. Use binary search (iterative Method). 
 
# list1 = [12, 34, 56, 78, 98, 22, 45, 13] 
 
  

import sys

def search_binary(list1: list, arg: int) -> None|int: 
    from math import floor
    
    sort_list = sorted(list1)
    
    
    counter = True
    while counter:
        mid = floor(len(sort_list)/2)
        mid_list = sort_list[mid]
        low_list = sort_list[0:mid-1]
        high_list = sort_list[mid-1:]
    
        if arg == mid_list:
            print(sort_list.index(mid_list))
            counter = False
        elif arg < mid_list:
            sort_list = low_list
        else:
            sort_list = high_list
        
    low_idx = 0
    high_idx = len(sort_list)     
    mid_idx = high_idx - 1
    
    low_index = 0 
    high_index = len(list1) - 1 
    mid_index = 0 
 
    while low_index <= high_index: 
        mid_index = (high_index + low_index) // 2 
 
        if list1[mid_index] == arg: 
            print(mid_index)
        elif list1[mid_index] > arg: 
            high_index = mid_index - 1 
        elif list1[mid_index] < arg: 
            low_index = mid_index + 1 

    
 
 




list1 = [12, 34, 56, 78, 98, 22, 45, 13] 
arg = 45
search_binary(list1, arg)



print(sys.getfilesystemencodeerrors())