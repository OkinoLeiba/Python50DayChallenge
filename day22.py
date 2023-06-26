#python challenge day22
# Day 22: Add Under_Score  
# Create three functions. The first called add_hash takes a string and 
# adds a hash # between the words. The second function called 
# add_underscore  removes  the  hash  (#)  and  replaces  it  with  an 
# underscore  "_"  The  third  function  called  remove_underscore, 
# removes  the  underscore  and  replaces  it  with  nothing.  if  you  pass 
# ‘Python’ as an argument for the three functions, and you call them at 
# the same time like: 
# print(remove_underscore(add_underscore(add_hash('Python'))))  
# it should return ‘Python’. 
  


def add_hash(input_str: str) -> None:
    # input_str = list(input_str)
    # iterate = 0
    # while iterate < len(input_str):
    #     input_str[iterate]
    hash_str = "#" + input_str
    # hash_str2 = "#".join(input_str)
    add_underscore(hash_str)
        
def add_underscore(hash_str: str) -> None:
    # hash_str = list(hash_str)
    # hash_str[0] = '_'
    for symbol in hash_str:
        if symbol == "#":
            hash_str = "".join("_")
        else:
            hash_str = "".join(symbol)
            
    underscore = hash_str.replace('#', '_')
    remove_underscore(underscore)
    
def remove_underscore(no_score: str) -> None:
    # no_score[0] = ' '
    no_score = no_score.replace('_', "")
    print(no_score)
    
    


    
input_str = "Python"
add_hash(input_str)
# print(remove_underscore(add_underscore(add_hash(input_str)))) 