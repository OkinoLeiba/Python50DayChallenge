#python challenge day32
# Day 32: Password Validator  
# Write  a  function  called  password_validator.  The  function 
# asks the user to enter a password. A valid password should have 
# at least one upper letter, one lower letter, and one 
# number. It should not be less than 8 characters long. When 
# the  user  enters  a  password,  the  function  should  check  if  the 
# password is valid. If the password is valid, the function should 
# return  the  valid  password.  If  the  password  is  not  valid,  the 
# function  should  tell  the  users  the  errors  in  the  password  and 
# prompt the user to enter another password. The code should 
# only stop once the user enters a valid password. (use while loop).   
# Extra Challenge: Valid Email  
 
# emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com' ] 
  
# Write  a  function  called  email_validator  that  takes  a  list  of 
# emails and checks if the emails are valid. The function returns a 
# list  of  only  valid  emails.  A  valid  email  address  will  have  the 
# following - @  symbol  (if the @ sign is at the beginning of the 
# name,  the  email  is  invalid.  If  there  are  more  than  one  @signs, 
# the email is invalid. All valid emails must have a dot com at the 
# end (.com), if not, the email is invalid.  For example, the list of 
# emails above should output the following as valid emails:   
# ['ben@mail.com', 'kenny@gmail.com']   
# If no emails in the list are valid, the function should return ‘all emails are 
# invalid’ 
  
import sys


def password_validator() -> None:
    from collections import Counter
    import string
    
    
    while True:
        password = input("Enter Password: ")
        for letter in password:
            if  letter not in string.ascii_uppercase:
                print("I pity the fool whose password doesn't have at least one uppercase letter.")
                continue
            elif letter not in string.ascii_lowercase:
                print("Password doesn't have as least one uppercase letter, knowing is half the battle - G.I. Joe.")
                continue
            elif letter not in string.digits:
                print("Does not compute, password doesn't have as least one number.")
                continue
            elif letter not in string.punctuation:
                print("No punky, punctuation.")
                continue
            elif (len(password) < 8):
                print("Unlucky number eight, password must have at least 8 characters.")
                continue
            else:
                print("Safe Pass")
            
        pass_count = repr(Counter(password))
        
    # counter = True
    # while counter:
    #     password = input("Enter Password: ")
         
    # if not(password == string.ascii_uppercase):
    # # for letter in password:))):
    #     print("I pity the fool whose password doesn't have at least one uppercase letter.")
    #     continue
                
pass_check = [] 
while True: 
    password = input('Enter your password: ') 
    if not any(letter.isupper() for letter in password): 
        pass_check.append("Please add at least one upper class letter to your password") 
        continue
    elif not any(letter.islower() for letter in password): 
        pass_check.append("Please add at least one lower class letter to your password") 
        continue
    elif not any(letter.isdigit() for letter in password): 
        pass_check.append("Please add at least one numero to your password") 
        continue
    elif len(password) < 8: 
        pass_check.append("8 characters is the magic number.") 
    if len(pass_check) > 0: 
        print('Check the following errors:') 
        print(str(pass_check)) 
        del pass_check[0:] 
    else: 
        print('Your password is {password}'.format(password))              
                
    
    
# class Letter:
#     for letter in password:
#         match letter:
#             case not letter.isupper():
#                 print("I pity the fool whose password doesn't have at least one uppercase letter.")
#             case not(password.islower() == letter):
#                 print("Password doesn't have as least one uppercase letter, knowing is half the battle - G.I. Joe.")
#             case not(password.isdigit() == letter):
#                 print("Does not compute, password doesn't have as least one number.")
#     while not(len(password) < 8):
#         print("Unlucky number eight, password must have at least 8 characters.")


password_validator()



def email_validator(input_array: list) -> None:
    from re import findall, search
    email_array = []
    for email in input_array:
        if search("\w+@\S+.com", email):
            email_array.append(email)
    print(email_array)
    if len(email_array) == 0:
        print("all emails are invalid")
    
 
 
    
input_array = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
email_validator(input_array)



print(sys.builtin_module_names)