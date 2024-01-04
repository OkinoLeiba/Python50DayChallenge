#python challenge day27
# Day 27: Unique Numbers  
# Write  a  function  called  unique_numbers  that  takes  a  list  of 
# numbers as an argument. Your function is going to find all the 
# unique  numbers  in  the  list.  It  will  then  sum  up  the  unique 
# numbers. You will calculate the difference between the sum of 
# all the numbers in the original list and the sum of unique 
# numbers in the list. If the difference is an even number, your 
# function should return the original list. If the difference is an 
# odd number, your function should return a  list with unique 
# numbers  only.    For  example  [1,  2,  4,  5,  6,  7,  8,  8]  should 
# return [1, 2, 4, 5, 6, 7, 8, 8]. 
 
# Extra Challenge: Difference of two Lists 
 
# Write  a  function  called  difference  that  takes  two  lists  as 
# arguments. This function should return all the elements that are 
# in list a but not in list b and all the elements in list b not in list 
# a. For example: 
# list1 = [1, 2, 4, 5, 6] 
# list2 = [1, 2, 5, 7, 9] 
# should return: 
# [4, 6, 7, 9] 
# Use list comprehension in your function.




if __name__ == "__main__":
    
    
    class Unique:
        @classmethod
        def __init__(cls, unique_num: list) -> None:
            cls.unique_num = unique_num
            
        
        @classmethod
        def unique_number(cls) -> list|set:
            from operator import sub, add 
            
            unique_list = []
            for num in cls.unique_num:
                if num not in unique_list:
                    unique_list.append(num)
                    
            check_diff = abs(sub(sum(unique_list), sum(cls.unique_num)))
            
            if check_diff % 2 == 0:
                 print("The original list is %s" %cls.unique_num)
            else:
                print("The unique numbers are %s" %unique_list)
                 
            
            if (sum(set(cls.unique_num)) - (sum(cls.unique_num))) % 2 == 0:
                return cls.unique_num
            else:
                return set(cls.unique_num)
            
            
    
    
    
    class Symmetry_Difference:
        @staticmethod
        def difference(thing1: list, thing2: list) -> list:
            list_thing1 = []
            for num in thing1:
                if num not in thing2:
                    list_thing1.append(num)
                    
                    
            list_thing2 = []
            for num in thing2:
                if num not in thing1:
                    list_thing2.append(num)
                    
                    
            last_thing = list_thing1 + list_thing2
            list_thing1.extend(list_thing2)
            
            last_thing3 = [iter for iter in thing1 if iter not in thing2]
            
            last_thing4 = [iter for iter in thing2 if iter not in thing1]
            
                    
            return list(set(thing1).symmetric_difference(set(thing2)))
    
            
    
    
    
    
    unique_num = [1,  2,  4,  5,  6,  7,  8,  8]
    unique = Unique(unique_num)
    # unique.unique_number()
    
    
    
    thing1 = [1, 2, 4, 5, 6]
    thing2 = [1, 2, 5, 7, 9] 
    symmetry_difference = Symmetry_Difference
    print(symmetry_difference.difference(thing1, thing2))
    