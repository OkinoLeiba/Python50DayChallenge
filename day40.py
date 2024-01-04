#python challenge day40
# Day 40: Pig Latin  
# Write  a  function  called  translate  that  takes  the  following 
# words and translates them into pig Latin. 
# a = 'i love python' 
 
#  Here are the rules: 
# 1.  If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the 
# end. For example, ‘eat’ will become ‘eatyay’ 
# 2.  If a word starts with anything other than a vowel, move 
# the first letter to the end and add ‘ay’ to the end. For 
# example, ‘day’ will become ‘ayday’. 
# Your code should return: 
# iyay ovelay ythonpay




def pig_latin(str_input: str) -> str:
    
    
    if str_input[0] in ("a", "e", "i", "o", "u"):
        the_pig = [(word[1:] + "yay") for word in str_input.split()]
        test = the_pig[0] 
    else:
        the_pig = [(word[1:] +  word[0] + "ay") for word in str_input.split()]
        
    the_pig = " ".join(the_pig)
        
        
    oscar = [] 
    for idx, word in enumerate(str_input.split()): 
        if word[0] in ("a", "e", "i", "o", "u"): 
            oscar.append(word[idx] + "yay") 
        else: 
            oscar.append(word[1:] + word[0] + "ay") 
    latin_pig = " ".join(oscar) 
    
    return the_pig
    
    

a = 'i love python'    
pig_latin(a)