#python challenge day18
# Day 18: Any Number of Arguments  
# Write  a  function  called  any_number  that  can  receive  any 
# number of arguments (integers and floats) and return the 
# average of those integers. If you pass 12, 90, 12, 34 as 
# arguments your function should return 37.0 as average. If you 
# pass 12, 90 your function should return 51.0 as average. 
 
# Extra Challenge: Add and Reverse  
# Write a function called add_reverse. This function takes two 
# lists  as  argument  and  adds  each  corresponding  number,  and 
# reverses  the  outcome.  For  example,  if  you  pass  [10,  12,  34] 
# and [12, 56, 78]. Your code should return [112, 22, 68]. If the 
# two  lists  are  not  of  equal  lengths,  the  code  should  return  a 
# message that "the lists are not of equal lengths".


import sys, math, statistics

# execute when the module is not initialized from an import statement.
if __name__ == '__main__':
    
    # type: ignore 
    def any_number(list_sum: list) -> None:
        from operator import iadd
        # sum_list = iadd(*list_sum)
        sum_avg = float(math.fsum(list_sum)/len(list_sum))
        sum_mean = float(statistics.mean(list_sum))
        print("The Average is: ", sum_avg)
        print("The Mean is: ", sum_mean)
        
        
        
        
    def add_reverse(thing1: list, thing2: list) -> None:
        from itertools import accumulate, chain
        from operator import add
        
        iterate = 0
        counter = True
        the_thing = []
        if len(thing1) == len(thing2):
            while counter:
                if iterate != len(thing1):
                    the_thing.append(thing1[iterate] + thing2[iterate])
                    the_thing.reverse()
                    iterate += 1
                if iterate == len(thing2):
                    counter = False
                    
        else:
            print("The lists are not of equal lengths")
                
        reverse_the_thing = the_thing[::-1]
        reverse_the_thing2 = the_thing.reverse()
        print(reverse_the_thing)

        the_thing2 = []
        if len(thing1) == len(thing2):
            for idx in range(0, len(thing1)):
                the_thing2.append(thing1[idx] + thing2[idx])
        
        the_thing2.reverse()
        the_thing2[::-1]
        
    
        print("Accumulate: ", list(accumulate(chain(thing1, thing2), func=add)).reverse())
        
    
    list1 = [12, 90, 12, 34]
    list2 = [12, 90]        
    any_number(list1) 
    
    
    thing1 = [10,  12,  34] 
    thing2 = [12, 56, 78]
    add_reverse(thing1, thing2)
        
