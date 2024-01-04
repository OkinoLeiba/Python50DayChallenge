#python challenge day33
# Day 33: List Intersection  
# Write a function called inter_section that takes two lists and 
# finds  the  intersection  (the  elements  that  are  present  in  both 
# lists).  The  function  should  return  a  tuple  of  intersections.  Use 
# list  comprehension  in  your  solution.  Use  the  lists  below.  Your 
# function should return (30, 65, 80). 
# list1 = [20, 30, 60, 65, 75, 80, 85] 
# list2 = [ 42, 30, 80, 65, 68, 88, 95] 
 
# Extra Challenge: Set or list 
# You want to implement a code that will search for a number in 
# a range. You have a decision to make as to whether to store the 
# number in a set or a list. Your decision will be based on time. 
# You have to pick a data type that executes faster. 
# You have a range and you can either store it in a set or a list 
# depending on which one executes faster when you are searching 
# for a number in the range. See below: 
# a = range(10000000) 
# x = set(a) 
# y = list(a) 
# Let’s say you are looking for a number 9999999 in the range 
# above.  Search  for  this  number  in  the  list  and  the  set.  Your 
# challenge is to find which code executes faster. You will pick the 
# one that executes quicker, lists, or sets. Run the two searches 
# and time them.  




def inter_section(list1, list2) -> set:
    result = set(list1).intersection(set(list2))
    result2 = [intersection for intersection in set(list1).intersection(set(list2))]
    result3 = [intersection for intersection in list1 for inter_section in list2 if intersection == inter_section]
    return result
    

list1 = [20, 30, 60, 65, 75, 80, 85] 
list2 = [ 42, 30, 80, 65, 68, 88, 95] 
inter_section(list1, list2) 


class Decide_Time:
    
    
    @classmethod
    def decision_engine(cls) -> None:
        a = range(10000000) 
        x = set(a) 
        y = list(a)
        cls.finput()
        
    
    @classmethod    
    def finput(cls) -> None:
        n = input("Please enter a number: ")
        return cls.timer(n)

    @classmethod
    def timer(cls, n) -> None:
        import timeit
        
        set_time = timeit.timeit(" ".join({str(num) for num in range(10000000) if num == n}))
        list_time = timeit.timeit(" ".join([str(num) for num in range(10000000) if num == n]))
        tuple_time = timeit.timeit(" ".join((str(num) for num in range(10000000) if num == n)))
        map_time = timeit.timeit(" ".join(map(str, range(10000000))))
        return cls.fdecide(set_time, list_time, tuple_time, n)

    @classmethod
    def  fdecide(cls, set_time, list_time, tuple_time, n) -> None:
        if set_time < list_time:
            if set_time < tuple_time:
                set_dataStructure = set(n)
        elif list_time < tuple_time:
            list_dataStructure = list(n)
            
        else:
            tuple_dataStructure = tuple(n)
        
   


decide_time = Decide_Time
decide_time.decision_engine()