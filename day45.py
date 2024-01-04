#python challenge day45
# Day 45: Words & Special Characters  
# Write a function called analyse_string that returns the number of 
# special  characters  (#$%&'()*+,-./:;<=>?@[\]^_`{|}~),  words, 
# and,  total  characters  (all  letters  and  special  characters  minus 
# whitespaces) in a string. Return everything in a dictionary format: 
 
# {“special character”: “number”, “words”: “number”, “total 
# characters”: “number”} 
 
# Use the string below as an argument: 
 
# “Python  has  a  string  format  operator %. This functions 
# analogously to printf format strings in C, e.g. "spam=%s 
# eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2". 
 
# Source Wikipedia. 
 
  






def analyse_string(arg: str) -> dict|None:
    import string, collections
    test = filter(lambda x: x in string.punctuation, arg.replace(" ", ""))
    test2 =  collections.Counter(test).total()
    
    result_dict = {"Special Character":collections.Counter(filter(lambda x: x in string.punctuation, arg.replace(" ", ""))).total(), 
                   "Words":collections.Counter(filter(lambda x: x in string.ascii_letters, arg.replace(" ", ""))).total(),
                   "Total":collections.Counter(arg).total()
     }
    print(result_dict)
    
    
    key = ["Special Character", "Words", "Total"]
    const = [string.punctuation, string.ascii_letters, arg.replace(" ", "")]
    result_dict2 = {}
    count = 0
    
    for c in const:
        for symbol in arg.replace(" ", ""):
            if symbol in c:
                count += 1 
    for k in key:
        result_dict2.update({k:count})
    print(result_dict)
    

    punct= [] 
    numero_letter = []
    dict_count = {"Special Character" : "", "Words" : "", "Total" : ""} 
 
    for char in arg.replace(" ", ""): 
        if char in string.punctuation: 
            if char not in punct: 
                punct.append(char) 
            dict_count["Special Character"] = str(len(punct))
        if char in string.ascii_lowercase: 
            if char not in numero_letter: 
                numero_letter.append(char) 
            dict_count["Words"] = str(len(numero_letter))
        else: 
            dict_count["Total"] = str(len(arg.replace(" ", "")))
    print(dict_count)

arg = "Python  has  a  string  format  operator %. This functions analogously to printf format strings in C, e.g. \"spam=%s eggs=%d\" % (\"blah\", 2)\" evaluates to \"spam=blah eggs=2"
analyse_string(arg)