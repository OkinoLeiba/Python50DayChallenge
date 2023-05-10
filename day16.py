#python challenge day16
# Day 16: Sum the List
# Write a function called sum_list with one parameter that takes
# a nested list of integers as an argument and returns the sum of
# the integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]]
# as an argument your function should return a sum of 33.

# Extra Challenge: Unpack A Nest
# Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
# Write a code that generates a list of the following numbers from
# the nested list above – 34, 67, 78. Your output should be another
# list:
# [34, 67, 78]. The list output should not have duplicates.



import sys
from memory_profiler import profile

# @profile
def sum_list(list_sum: list) -> None: 
    from functools import reduce
    from itertools import chain
    new_list2 = []
    for iterable in list_sum:
       for jterable in iterable:
              new_list2.append(jterable)
    print(sum(new_list2))

    new_list = [iterable for iterable in list_sum for jterable in iterable]
    # new_list = eval(new_list)
    #result = sum(new_list)
    
    print(reduce(lambda x, y: sum(chain(x, y)), list_sum))

# @profile
def unpack_nest(nested_list: list) -> None:
    from itertools import chain
    from functools import reduce
    from operator import iconcat
    
    
    param_list = [34, 67, 78]
    result_list = []
    result_list2 = []
    result_list2 = [jterable for iterable in nested_list for jterable in iterable if jterable in param_list]
    # result_list2 = unpack_list.append(param_list)
     
    for arr in nested_list:
        for num in arr:
            if num == param_list:
                if num != result_list:
                    result_list.append(num)
                
    for arr in nested_list:
        for num in arr:
            if num in param_list:
                if num not in param_list:
                    result_list.append(num)
                    
    
    test2 = chain(nested_list)
       
    test1 = list(chain.from_iterable(nested_list))
    
    test3 = reduce(iconcat, nested_list, [])
    
    test4 = [[list1, list2] for list1, list2 in zip(input_list[1], input_list[0])] 
    
    
    print(result_list)
    print(result_list2)
                
                
        





input_list = [[2, 4, 5, 6], [2, 3, 5, 6]]
# sum_list(input_list)

nested_list = [[12, 34, 56, 67], [34, 68, 78]]
unpack_nest(nested_list)