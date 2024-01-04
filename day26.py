#python challenge day26
# Day 26: Sort Words  
# Write a function called sort_words that takes a string of words 
# as  an  argument,  removes  the  whitespaces,  and  returns  a  list  of 
# letters sorted in alphabetical order. Letters will be separated by 
# commas.  All  letters  should  appear  once  in  the  list.  This  means 
# that  you  sort  and  remove  duplicates.  For  example  ‘love life’ 
# should return as ['e,f,i,l,o,v']. 
 
# Extra Challenge: Length of Words  
# s = 'Hi my name is Richard' 
 
# Write  a  function  called  string_length  that  takes  a  string  of 
# words  (words  and  spaces)  as  argument.  This  function  should 
# return the length of all the words in the string. Return the results 
# in a form of a dictionary. The string above should return: 
 
# {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7} 


import string, sys


def sort_words(str_input):
    new_string = list(sorted(set(str_input.replace(" ", "" ))))
    
    new_string2 = []
    str_input = str_input.replace(" ", "").strip()
    for letter in str_input:
        if letter not in new_string2:
            new_string2.append(letter)
            new_string2.sort()
    
    print(new_string)
    
str_input = "love life"
sort_words(str_input)

   
def string_length(str_input_len):
    lambda x: str_input_len.split(x)
    length_dict = {word : len(word) for word in str_input_len.split()}
    print(length_dict)
    
 
 
str_input_len = 'Hi my name is Richard'  
string_length(str_input_len)
 
 
 
 
print(sys.getprofile())
print(sys.implementation)
