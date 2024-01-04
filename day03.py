#python challenge day3
# Day 3: Register Check
# Write a function called register_check that checks how many
# students are in school. The function takes a dictionary as a
# parameter. If the student is in school, the dictionary says ‘yes’. If
# the student is not in school, the dictionary says ‘no’. Your
# function should return the number of students in school. Use the
# dictionary below. Your function should return 3.
# register = {'Michael':'yes','John': 'no',
# 'Peter':'yes', 'Mary': 'yes'}

# Extra Challenge: Lowercase Names
# names = ["kerry", "dickson", "John", "Mary",
# "carol", "Rose", "adam"]
# You are given a list of names above. This list is made up of names
# of lowercase and uppercase letters. Your task is to write a code
# that will return a tuple of all the names in the list that have only
# lowercase letters. Your tuple should have names sorted
# alphabetically in descending order. Using the list above, your
# code should return:
# ('kerry', 'dickson', 'carol', 'adam')

import operator

class Register:
    def __init__(self, register: dict) -> None:
        self.register = register


    def check_register(self) -> None:
        count_student = 0
        # count_student =  [iterable.count for iterable in self.resigter.values() if self.resigter.values() == "yes"]
        # count_student = [if self.register.values() == "yes" count_student += 1 for iterable in self.register.values()]
        for value in self.register.values():
            # if x == "yes":
            if operator.eq(value, "yes"):
                count_student += 1
        
        count_student2 = 0        
        for key, value in self.register.items():
            if value.lower() == "yes":
                count_student2 += 1
        
        y_students = [student for student in self.register.values() if student == "yes"]
        len(y_students)
        count_students = sum(student.count() for student in self.register.values() if student == "yes")
        count_students = y_students.count(y_students)
        
        y_student2 = sum(1 for student in self.register.values() if student == "yes")
    
        print("Number of Registered Student is ", count_student)


register = {"michael" : "yes", "john" : "no", "peter" : "yes", "mary" : "yes"}
check = Register(register)
check.check_register()




list_name = ["kerry", "dickson", "John", "mary","carol", "Rose", "adam"]
def case_sensitive(list_name: list) -> None:
    print(tuple(sorted([x for x in list_name if x.islower()], reverse=True)))
    # new_list.sort(reverse=True)
    # new_tuple = (new_list)
    
    

# case_sensitive(list_name)
            


