#python challenge day15
# Day 15: Same in Reverse
# Write a function called same_in_reverse that takes a string
# and checks if the string reads the same in reverse. If it is the
# same, the code should return True if not, it should return False.
# For example, ‘dad’ should return True, because it reads the
# same in reverse.

# Extra Challenge: What’s My Age?
# Write a function called your_age. This function asks a student
# to enter their name and then it returns their age. For example, if
# a user enters Peter as their name, your function should return,
# ‘Hi, Peter, you are 27 years old. This function reads data
# from the database (dictionary below). If the name is not in the
# dictionary, your code should tell the user that their name is not
# in the dictionary, and ask them for their age. Your code should
# then add the name and age to the dictionary of names_age
# below. Once added your code should return to the user ‘Hi,
# (added name), you are (added age) years old’. Remember
# to convert the input from user to lowercase letters
# names_age = {"jane": 23, "kerry": 45, "tim": 34, “peter": 27}



import sys




class Reverse:
    def __init__(self, input_string: str) -> None:
        self.input_string = input_string


    def same_in_reverse(self) -> bool|str|None:
        
        rev_string = self.input_string[::-1]
        counter = 0
        
        while counter < len(self.input_string):
            if self.input_string[counter] == self.input_string[::-1][counter]:
                return True
            else:
                return False
        counter += 1

        
        if self.input_string == rev_string:
            print("I know this much is true")
            return True
            
        else:
            print("Not the answer")
            return False
           

        return True if self.input_string == self.input_string[::-1] else False

    

reverse = Reverse("dad")
reverse.same_in_reverse()
        





class Age:
    def __init__(self, names_age: dict) -> None:
        self.names_age = names_age

    def your_age(self):
        name = input("What is your name: ").lower()
        
        if name in self.names_age:
            #[iterable for iterable in self.names_age.keys()]
            age = self.names_age.get(name)
            # name = name.capitalize()
            print("Hi, {}, you are {} years old.".format(name.capitalize(), age))
            #print_out = "Hi, {}, you are {} years old."
            #print(print_out.format(name, age))
        elif name not in self.names_age:
            name = name.capitalize()
            age_input = input("Hi, {}, your name was not found, what is your age: ".format(name))
            name = name.lower()
            self.names_age.update({name:age_input})
            name = name.capitalize()
            print("Hi, {}, you are {} years old.".format(name, age_input))
            # print_out = "Hi, {}, you are {} years old."
            # print(print_out.format(name, age_input))
        else:
            ValueError


        for key in self.names_age.keys(): 
            try:
                if key.lower() == name.lower(): 
                    print("Hi, {}! You are {} years old".format(name.capitalize(), self.names_age.get(key) ))
                else: 
                    while name not in self.names_age.keys(): 
                        age = input("Your name is not found, please enter your age? ").lower() 
                        self.names_age.update({name: age}) 
                        print("Hi, {}! You are {} years old".format(name.capitalize(), self.names_age.get(name)))
            except ValueError:
                print("Enter valid values.")
                

names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}


age = Age(names_age)
age.your_age()