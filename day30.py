#python challenge day30
# Day 30: Most Repeated Name 
# Write  a  function  called  repeated_name  that  finds  the  most 
# repeated name in the following list. 
# name = ["John", "Peter", "John", "Peter", "Jones", "Peter"] 
      
# Extra Challenge: Sort by Last Name  
# You work for a local school in your area. The school has a list of 
# names of students saved in a list. The school has asked you to 
# write  a  program  that  takes  a  list  of  names  and  sorts  them 
# alphabetically. The names should be sorted by last names. Here 
# is a list of names: 
# [‘Beyonce Knowles, ‘Alicia Keys’, ‘Katie Perry’,  ‘Chris 
# Brown’,’ Tom Cruise’] 
# Your code should not just sort them alphabetically, but it should 
# also switch the names (the last name must be the first). Here is 
# how your code output should look: 
# ['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie', 
# 'Knowles Beyonce'] 
# Write a function called sorted_names.  


def init(name_input: list) -> None:
    from collections import Counter
    print(max(Counter(name_input)))
    print(max(Counter(name_input).most_common()))
    
    # init.repeated_name.name_input
    
   
        
    def repeated_name() -> None:
        
        name_count = {}
        count_list = []
        name_list = []
        for name in name_input:
            count = 0
            i = 0
            while i < len(name_input):
                if name != any(name_list):
                    if name == name_input[i]:
                        count += 1 
                i += 1
            count_list.append(count)
            name_list.append(name)  
            
        result = name_input[max(count_list)]
        
        
        for word in name_input:
            Counter(name_input)
        
    repeated_name()

name_input = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
# init(name_input)


def sort_lastName(list_name) -> None:
    split_names = [name.split(" ") for name in list_name]
    split_names.reverse()
    result = [row for row in split_names]    



    split_list = [] 
 
    for name in list_name: 
        split_list.append(name.split()) 
 
    sort_list = [] 
    for sort_name in sorted(split_list, key= lambda x: x[-1]): 
        sort_list.append(' '.join([sort_name[-1], sort_name[0]])) 
 
    print(result)
    pass
    
    
    
list_name = ['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie', 'Knowles Beyonce'] 
sort_lastName(list_name)