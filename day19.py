#python challenge day19
# Day 19: Words and Elements  
# Write two functions. The first function is called count_words 
# which takes a string of words and counts how many words are in 
# the string.  
 
# The second function called  count_elements takes a string of 
# words and counts how many elements are in the string. Do not 
# count the whitespaces. The first function will return the number 
# of words in a string and the second one will return the number 
# of  elements  (less  whitespace).  If  you  pass  ‘I love learning’, 
# the count_words function should return 3 words and 
# count_elements should return 13 elements.

# import array
import string, re

# execute when the module is not initialized from an import statement.
if __name__ == "__main__":

    class Words_Elements:
        # type: ignore 
        def __init__(self, string_input: str) -> None:
            # self.string_input = string_input
            pass
            
        
        # type: ignore 
        def count_words(self) -> None:
            from itertools import count
            from collections import Counter
            
            split_input = string_input.rsplit(" ")
            count_words = 0
            for item in split_input:
                if item != " ":
                    count_words += 1
            print(f"The Sesame Street Count Says, {count_words} words ahh ahh ahh")
            # result = [item for item in split_input lambda item: if item: count += 1]
            
            test = sum(1 for word in string_input.rsplit(" "))
            
            print(sum(Counter(string_input.split(" ")).values()))
            
          
        def count_elements(self) -> int|None:
            from collections import Counter
            concat_input = string_input.replace(" ","")
            concat_input2 = string_input.translate({ord(c): None for c in string.whitespace})
            concat_input3 = re.sub(r"\s+","",string_input)
            count_elemt = 0
            for item in concat_input:
                if item != " ":
                    count_elemt += 1 
            print(count_elemt)
            count_elemt2 = len(concat_input2)
        
            print("The Sesame Street Count Says, {} elements ahh ahh ahh" .format(count_elemt))
            
            
            test2 = sum(1 for letter in string_input.replace(" ",""))
            
            print(sum(Counter(string_input.replace(" ","")).values()))

        
    
    string_input = "I love learning"
    words_elements  = Words_Elements(string_input)
    words_elements.count_words()
    words_elements.count_elements()
    