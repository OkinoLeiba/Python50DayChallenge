#python challenge day37
# Day 37: Count the Vowels  
# Create  a  function  called  count_the_vowels.  The  function 
# takes one argument, a string, and returns the number of vowels 
# in  the  string.  For  example,  ‘hello’ should return 2  vowels. If  a 
# vowel appears in a string more than once it should be counted 
# as  one.  For  example,  ‘saas’  should  return  1  vowel.  Your code 
# should count lowercase and uppercase vowels





def count_the_vowels(the_string: str) -> int:
    
    # the_string.lowercase() == ["aeiou"]
    test = the_string.lower().count("aeiou")
    test2 = sum(the_string.lower().count(vowel) for vowel in "aeiou")

    c = 0
    for letter in the_string.lower():
        for vowel in "aeiou":
            if letter == vowel:
                c += 1
                
    vowels = [] 
    c2 = 0
    for letter in the_string.lower(): 
        if letter in "aeiou": 
            if letter not in vowels: 
                vowels.append(letter)
                c2 += 1
    len(vowels)
    
    return c2





the_string = "hello"
count_the_vowels(the_string)
