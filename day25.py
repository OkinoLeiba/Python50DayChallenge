#python challenge day25
# Day 25: All the Same 
 
# Create a function called all_the_same that takes one 
# argument,  a  string,  a  list,  or  a  tuple  and  checks  if  all  the 
# elements are the same. If the elements are the same, the function 
# should return True. If not, it should return False. For example, 
# [‘Mary’, ‘Mary’, ‘Mary’] should return True. 
 
# Extra Challenge: Reverse a String  
 
# str1 = "the love is real" 
 
# Write a function called read_backwards that takes a string as 
# an  argument  and  reverses  it.    For  example,  the  string  above 
# should return: "real is love the" 
from typing import Any



def all_the_same(input_string: Any) -> None:
    test_case = {word for word in input_string if word in input_string}
    test_case3 = set(input_string)
    if len(test_case) == 1:
        print("True")
    else:
        print("False")
        
    test_case1 = all(word for word in input_string if word in input_string)
    
    test_case4 = all(word == input_string[0] for word in input_string)
    
    test_case5 = all(Any for word in input_string if word == input_string[0])
    
    test_case6 = [bool for word in input_string if word == input_string[0]]
    
    for idx, word in enumerate(input_string):
        if word[idx] == word[0]:
            print(bool(1)) 
        else:
            print(bool(0))

        
    i = 0
    check = []
    temp_word = " "
    for word in input_string:
        if (word == temp_word):
            check.append(True)
        temp_word.replace(" ", word)    
    print(bool(check))
        
        
input_string = ["Mary", "Mary", "Mary"]
input_string2 = ("Mary", "Mary", "Mary")
all_the_same(input_string)
        


def read_backwards(str1: str) -> None:
    backwards_str = str1.split(" ")[::-1]
    backwards_str3 = [backwards_str.reverse() for word in backwards_str]
    backwards_str2 = list(map(lambda x: x.split(" ")[::-1], str1))
    
    print(backwards_str)
    
    
    
str1 = "the love is real" 
read_backwards(str1)