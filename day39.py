#python challenge day39
# Day 39: Password Generator 
 
# Create a function called generate_password that generates any 
# length  of  password  for  the  user.  The password  should  have a 
# random mix of upper letters, lower letters, numbers, and 
# punctuation  symbols.  The  function  should  ask  the  user  how 
# strong  they  want  the  password  to  be.  The  user  should  pick  from  - 
# weak,  strong,  and  very  strong.  If  the  user  picks  weak,  the 
# function should generate a 5-character long password. If the user 
# picks strong, generate an 8-character password and if they pick 
# very strong, generate a 12-character password.



def generate_password() -> str:
    import string, random
    
    
    counter = True
    while counter:
        print("Pick the Strength of the Password: \n1: weak\n2: strong\n3: very strong")
        pass_strength = input()
        if pass_strength not in ["", "1", "2", "3", "weak", "strong", "very strong"]:
            counter = True
        else:
            counter = False
    
    
    password_source = string.ascii_letters + string.digits + string.punctuation
    
    password_source_len = len(password_source)
    
    test1 = random.choices(password_source, k=5)
    
    # test2 = random.shuffle(password_source)
    test2 = random.sample(password_source, k=len(password_source))
    
    test3 = random.sample(password_source, k=5)
    
    i = 0
    test4 = []
    while i < 5:
        rand_num = random.randrange(0, len(password_source))
        test4.append(password_source[rand_num])
        i += 1
    
    match pass_strength:
        case "1" | "weak":
            pass_len = 5
        case "2" |"strong":
            pass_len = 8
        case "3" | "very strong":
            pass_len = 12
        case _:
            print("Pick the Strength of the Password: \n1: weak\n2: strong\n3: very strong")
            pass_strength = input()
            
    
    rand_password = "".join(random.choices(password_source, k=pass_len))
    
    password_final = []
    if pass_strength == "1" or pass_strength == "weak": 
        pass_len = 5 
    elif pass_strength == "2" or pass_strength == "strong": 
        pass_len = 8 
    elif pass_strength == "3" or pass_strength == "very strong": 
        pass_len = 12 
        for i in range(pass_len): 
            password = str(random.choice(password_source)) 
            password_final.append(password) 
    print("Your password is", password_final)
    
    return rand_password
    




generate_password()