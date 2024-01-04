#python challenge day31
# Day 31: Longest Word  
# Write a function that has one parameter and takes a list of words 
# as an argument. The function returns the longest word from the 
# list.  Name  the  function  longest_word.  The  function  should 
# return the longest word and the number of letters in that word. 
# For example, if you pass [‘Java, ‘JavaScript’, ‘Python’], your 
# function should return  
# [10, JavaScript] as the longest word. 
 
# Extra Challenge: Create User  
# Write  a  function  called  create_user.  This  function  asks  the 
# user  to  enter  their  name,  age,  and  password.  The  function 
# saves  this  information  in  a  dictionary.  For  example,  if  the  use 
# enters  name  as  Peter,  age  -  18  and  password  -  love.  The 
# function  should  save  the  information  as:  {'name':  'Peter', 
# 'age': 18, 'password': 'love'} 
# Once the information is saved. The function should print to the 
# user that - "User saved. Please login" 
# The function should then ask the user to  re-enter their name 
# and  password.  If  the  name  and  password  match  with  what  is 
# saved in the dictionary, the function should return "Logged in 
# successfully".  If  the  name  and  password  do  not  match  with 
# what is saved in the dictionary, the function should print 
# ('Wrong password or user name. Please try again'. The 
# function  should  keep  running  until  the  user  enters  correct 
# logging details. 
 
 
def longest_word(word_input: list) -> list|int:
    from collections import Counter

    test2 = lambda word_input: len(word_input)

    # result = [word for word in word_input lambda: len(word)]

    test = len(word_input[0])

    result2 = []
    for word in word_input:
        result2.append([Counter(word), word])
        
        
    result =[] 
    for word in word_input: 
        result.append([len(word), word])
    print(max(result))
        
    return max(result2)

 
word_input = ["Java", "JavaScript", "Python"]
longest_word(word_input)

sentence = 'the rocket came back from mars'
word = [test for test in sentence.split()]

class User:

    @classmethod
    def create_user(cls) -> None:
        name = input("Please Enter User Name: \n")
        age = int(input("Please Enter User Age: \n"))
        password = input("Please Enter User Password: \n")
        cls.name = name
        cls.age = age
        cls.password = password
        
        cls.store_data()
        
    @classmethod    
    def store_data(cls) -> dict:
        # file = open(user_info.txt, 'r', encoding="utf-8")
        # user_id = file.read(id)
        # id_count = 0
        # while user_id == id_count:
        #     if user_id == id_count:
        #         id_count += 1 
        #     else:
        #         id = id_count
        #         user_info = {id:{"name":name, "age":age, "password":password}}
                
        # file.close()
        id = 0
        cls.user_info =  {id:{"name":cls.name, "age":cls.age, "password":cls.password}}
        print("User saved. Please login")
        iname = input("Please Enter User Name: \n")
        ipassword = input("Please Enter User Password: \n")       
        if cls.user_info[0]["name"] == iname and cls.user_info[0]["password"] == ipassword:
            print("Logged in successfully")
        else:
            print("Wrong password or user name. Please try again")
        # cls.log_in()
        return cls.user_info

    @classmethod
    def log_in(cls) -> None:
        # file = open(user_info.txt, 'r', encoding="utf-8")
        # fid = file.read(id)
        # fname = file.read(name)
        # fpassword = file.read(password)
        print("***Log In***")
        name = input("Please Enter User Name: \n")
        password = input("Please Enter User Password: \n")
        # if cls.store_data.user_info["name"] == name and  cls.store_data.user_info["password"] == password:
        # if fname == name and  fpassword == password:
        for id in fid:
            if cls.user_info[fid]["name"] == name and cls.user_info[fid]["password"] == password:
                print("Logged in successfully")
            else:
                print("Wrong password or user name. Please try again")
                
                
def create_user2() -> None|str:   
    dict_user = {} 
    name = input("Please Enter your name: ") 
    age = int(input("Please Enter your age: ")) 
    password = input("Please Enter your password: ") 
     
    dict_user.update({'name': name}) 
    dict_user.update({'age': age}) 
    dict_user.update({'password': password}) 
    print("User saved. Please login") 

    while True: 
        user_name = input("Please Enter Your User Name to Login") 
        password = input("Please Enter Your Password") 
        if user_name == dict_user.get('name') and password == dict_user.get('password'): 
            return "Logged in successfully"
            break 
        else: 
            print('Wrong password or user_name please try again') 
 
 
    print(create_user()) 
  


user = User
# user.create_user()
# user.log_in()