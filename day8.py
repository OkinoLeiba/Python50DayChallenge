#python challenge day8
# Day 8: Odd and Even  
# Write a function called odd_even that has one parameter and 
# takes a list of numbers as an argument. The function returns the 
# difference between the largest even number in the list and the 
# smallest  odd  number  in  the  list.  For  example,  if  you  pass 
# [1,2,4,6] as an argument the function should return 6 -1= 5. 
 
# Extra Challenge: List of Prime Numbers  
# Write a function called prime_numbers. This function asks a 
# user  to  enter  a  number  (integer)  as  an  argument  and  returns  a 
# list of all the prime numbers within its range. For example, if user 
# enters 10, your code should return [2, 3, 5, 7] as prime numbers.


import sys



def odd_even(num_list):
    from functools import reduce
    
    num_even_list = []
    num_odd_list = []
    unknown_list = []
    
    for num in num_list:
        if num % 2 == 0:
            num_even_list.append(num)
        elif num % 2 != 0:   
            num_odd_list.append(num)
        else:
            unknown_list.append(num)
            
    num_list_result = max(num_even_list) - min(num_odd_list)
            
    
    # determine odd or even 
    # max([num_item for num_item in num_list if num_item % 2 != 0])
    num_even = [num_item for num_item in num_list if num_item % 2 == 0]
    num_odd = [num_item for num_item in num_list if num_item % 2 != 0]

    test = reduce(lambda _, num_even: max(num_even), num_even)
    

    # determine largest number...by sorting 
    """iterator_counter = 0
    max_even = {}
    while iterator_counter > len(num_even):
        max_even = num_even[iterator_counter] > num_even[iterator_counter+1]
        iterator_counter += 1 """
    num_even.sort(reverse = True, key=max)
    num_odd.sort(key=max)


    # calculate results
    result = num_even[0] - num_odd[0]
    print(result)
    



num_list = [1,2,5,6,7,8,9,13,16]
# odd_even(num_list)


def prime_check(num: int) -> int|None:
     test2 = [num for num in range(2, num+1) for next in range(2, num) if num % next != 0]
     
     
     """one line answer - not my code"""
    # return [i for i in range(2, number+1) if all(i % j != 0 for j in range(2, i))]
     
     
     
     
     
     
prime_check(10)