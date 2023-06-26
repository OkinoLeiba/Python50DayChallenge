#python challenge day20
# Day 20: Capitalize First Letter  
# Write a function called capitalize. This function takes a string 
# as an argument and capitalizes the first letter of each word. For 
# example, ‘i like learning’ becomes ‘I Like Learning’. 
 
# Extra Challenge: Reversed List  
# str1 = 'leArning is hard, bUt if You appLy youRself ' \ 
#        'you can achieVe success' 
 
# You are given a string of words. Some of the words in the string 
# contain  uppercase  letters.  Write  a  code  that  will  return  all  the 
# words that have an uppercase letter. Your code should return a 
# list of the words. Each word in the list should be reversed. Here 
# is how your output should look: 
 
# ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca'] 
 
import sys, string
 
 
class Letters: 
    def __init__(self, string_input, string_words) -> None:
        self.string_input = string_input
        self.string_words = string_words
        
        
    def cap_title(self) -> None:
        string_upper = []
        for word in string_input.split(" "):
            if word[0].islower(): 
                string_upper.append(word.replace(word[0], word[0].upper()))
        
        upper_string = " ".join(string_upper)
            
            
        string_upper2 = [] 
        for idx, word in enumerate(string_input.split()): 
            if word[0].islower(): 
                string_upper2.append(word.capitalize()) 
            else: 
                string_upper2.append(word) 
        upper_string2 = " ".join(string_upper2)

        title_string = string_input.title()
        print("Capitalized String: %s" %title_string)
        
        
    def uppercase_search(self) -> None:  
        print("A" == string.ascii_uppercase)
        new_words =  [word[::-1] for word in string_words.rsplit(" ") for letter in word if letter in string.ascii_uppercase]
        new_words2 = []
        for word in string_words.rsplit():
            for letter in word:
                if letter in string.ascii_uppercase:
                    new_words2.append(word[::-1])
                 
        
        upper_words = []
        for word in string_words.split(): 
            for letter in word: 
                if letter in string.ascii_uppercase: 
                    upper_words.append("".join(word[::-1])) 
                    
        print("The Words on the Street is: {}".format(new_words))
        
  
  
    
    
string_input = "i like learning"
string_words =  "leArning is hard, bUt if You appLy youRself you can achieVe success" 
letters = Letters(string_input, string_words)
letters.cap_title()
letters.uppercase_search()


print(sys.__annotations__)
print(sys.__name__)
