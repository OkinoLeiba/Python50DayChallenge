#python challenge day35
# Day 35: Pangram  
# Write  a  function  called  check_pangram  that  takes  a  string 
# and checks if it is a pangram. A pangram is a sentence that 
# contains all the letters of the alphabet. If it is a pangram, 
# the function should return True, otherwise, return False. The 
# following sentence is a pangram so it should return True: 
 
# 'the quick brown fox jumps over a lazy dog' 
 
# Extra Challenge: Find my Position  
 
# Write a function called find_index that takes two arguments; 
# a list of integers, and an integer. The function should return the 
# indexes of the integer in the list. If the integer is not in the list, 
# the function should convert all the numbers in the list into the 
# given integer.  
 
# For example, if the list is: [1, 2, 4, 6, 7, 7] and the integer is 7, 
# your code should return [4, 5] as the indexes of 7 in the list. If 
# the list is [1, 2, 4, 6, 7, 7] and the integer is 8, your code should 
# return [8, 8, 8, 8, 8, 8] because 8 is not in the list. 
  




def check_pangram(pan_string: str) -> bool:
    import string
    reverse_string = pan_string[::-1]
    pan_string = pan_string.lower().replace(" ", "")
    
    
    test = set(pan_string.lower().replace(" ", "")).difference_update(string.ascii_lowercase)
    
    test2 = set(string.ascii_lowercase).difference_update(pan_string.lower().replace(" ", ""))
    
    test3 = set(pan_string.lower().replace(" ", "")).symmetric_difference(string.ascii_lowercase)
    
    test4 = set(string.ascii_lowercase).symmetric_difference(pan_string.lower().replace(" ", ""))
    
    check = [all(sletter) for letter in string.ascii_lowercase for sletter in pan_string.lower().replace(" ", "") if letter == sletter]
    check2 = all(pan_string.lower()) == all(string.ascii_lowercase)
    
    if not test4:
        print(True)
    else:
        print(False)
        
    
    check_str = []
    for letter in pan_string.lower().replace(" ", ""):
        if letter not in pan_string.lower().replace(" ", ""):
            check_str.append(letter)
        
    check_str.sort()
    
    check_str = "".join(check_str)
    
    if check_str == string.ascii_lowercase:
        return True
    else:
        return False
    
        
    


pan_string = 'the quick brown fox jumps over a lazy do' 
check_pangram(pan_string)



def find_index(list_index: list, num_index: int) -> None:
    try:
        start = 0  
        index_num = []
        while start != len(list_index):
            index_num.append(list_index.index(num_index, start))
            start = (list_index.index(num_index, start) + 1)
        print(index_num)
    except ValueError:
        num_index = int(input("Input Number to Check in the Index: "))
    
    
    index_num2 = [i for i in list_index ]
    
    index_num3 = []
    for idx, num in enumerate(list_index):
        if num == num_index:
            index_num3.append(idx)
        if num not in list_index:
            for num in list_index:
                index_num3.append(num)
    print(index_num3)
                
            
    
    
   
    
    
# num_index = int(input("Input Number to Check in the Index: "))
# list_index = [1, 2, 4, 6, 7, 7]
# find_index(list_index, num_index)
