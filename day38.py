#python challenge day38
# Day 38: Guess a Number  
# Write a function called guess_a_number. The function 
# should ask a user to guess a randomly generated number. If the 
# user guesses a higher number, the code should tell them that the 
# guess  is  too  high,  if  the  user  guesses  low,  the  code  should  tell 
# them that their guess is too low. The user should get a maximum 
# of  three guesses.  When  the  user guesses right,  the  code  should 
# declare  them  a  winner.  After  three  wrong  guesses,  the  code 
# should declare them a loser. 
 
# Extra Challenge: Find Missing Numbers  
# list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,  
#         18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31] 
 
# Write a function called missing_numbers that takes a list of 
# sequence  of  numbers  and  finds  the  missing  numbers  in  the 
# sequence. The list above should return: 
 
# [4, 8, 10, 13, 16, 29, 30] 


def guess_a_number() -> None:
    import random
    
    rand_num = random.randrange(1,20)
    
   
    guess_stop = 1
    while guess_stop <= 3:
        user_num = int(input("Guess that randomly generated number: "))
        if user_num == rand_num:
            print("Winner, winner, chicken dinner!")
        elif user_num > rand_num:
            print("The guess is too high")
        elif user_num > rand_num:
            print("The guess is too low")
        else:
            print("No More Guess!")
        guess_stop += 1
    
 
 
# print(guess_number()) 
 

 
def missing_numbers(list_num: list) -> None:
    
    i = 0
    result_list = []
    
    while i < len(list_num):
        for num in list_num:
            if i != num:
                result_list.append(i)
                i += 1
    
    
    
    result_list2 = []
    for num in range(list_num[0], list_num[-1]):
        if num not in list_num:
            result_list2.append(num)
            
    
    



list1 = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31] 
list2 = [4, 8, 10, 13, 16, 29, 30] 
# guess_a_number()
missing_numbers(list1)
  
