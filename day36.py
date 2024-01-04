#python challenge day36
# Day 36: Count String  
# Write a function called count that takes one argument a string, 
# and  returns  a  dictionary  of  how  many  times  each  element 
# appears in the string. For example, ‘hello’ should return: 
#  {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.



import sys

def count_string(str_input: str) -> dict:
    from collections import Counter
    
    test = Counter(str_input)
    print(test)
    
    
    
    
    count2 = {}
   
    for x in str_input:
        i = 0
        c = 0
        while i < (len(str_input)):
            if x == str_input[i]:
                c += 1
            count2.update({x:c})
            i += 1
    print(count2)                
                
    count1 = {x : int for x in str_input}
    
    test2 = {i: i * i for i in range(10)}
    
    count2 = {} 
    for idx in range(len(str_input)): 
        x = str_input[idx] 
        c2 = 0 
        for idy in range(idx, len(str_input)): 
            if str_input[idy] == str_input[idx]: 
                c2 += 1 
        countz = dict({x: c2})  
        if x not in count2.keys(): 
            count2.update(countz) 
    
    
    return count2
    
str_input = "hello"   
count_string(str_input)



print(sys.audit("builtins.id", id))
print(sys.audit("import"))
print(sys.audit("os.chdir"))
