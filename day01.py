#python challenge day1
# Day 1: Division and Square-root
# Write a function called divide_or_square that takes one
# argument (a number), and returns the square root of the number
# if it is divisible by 5, returns its remainder if it is not divisible by
# 5. For example, if you pass 10 as an argument, then your function
# should return 3.16 as the square root.

# Extra Challenge: Longest Value
# Write a function called longest_value that takes a dictionary
# as an argument and returns the first longest value of the
# dictionary. For example, the following dictionary should return
# – apple as the longest value.
# fruits = {'fruit': 'apple', 'color': 'green'}


import sys, math 


class NewDivide:
    def __init__(self, num) -> None:
        self.num = num
        
    def __repr__(self, num) -> None:
        self.num = num
        
    @property
    def number(self) -> int:
        return self.num
        
    # property(fget=number, fset=None, fdel=None, doc=None)
    
    def divide_or_square(self) -> str|float:
        if ((self.num % 5) == 0):
            sol = math.sqrt(self.num)
            sol = self.num ** 0.5
            return f"The square root is {sol}"
        else:
            sol = self.num % 5
            print("The reminader is", sol)
        return sol 

    

newDivide = NewDivide(14)

map(NewDivide, [12, 9, 2])
print(newDivide.divide_or_square())
# print(newDivide.divide_or_square(15))
# print(newDivide.divide_or_square(16))
# print(newDivide.divide_or_square(70))
# print(newDivide.divide_or_square(300))






fruits = {"fruit":"apple", "color":"green"}


def longest_value(item: dict) -> int|str|None:
    val_fruit = fruits.values()
    len_word = []
    # x = fruits.values()
    # for individual_fruit in val_fruit:
    #     len_word.append(len(individual_fruit))
    counter = 0
    # while counter < len(len_word):
    #     if len_word[counter] < len_word[counter + 1]:
    #         return individual_fruit
    #         # temp = len_word
    #     counter += 1
       
    for individual_fruit in val_fruit:
        if len(individual_fruit) > counter:
            counter = len(individual_fruit)
            result = individual_fruit
            
            return result 
        
    max(len(individual_fruit) for individual_fruit in fruits.values())

def longest_value2(item: dict) -> int:
    key=lambda k: len(item[k])
    result = max(item, key=lambda k: len(item[k]))
    result = max(item.values(), key=len)
    return result

sort_list = sorted(fruits.values(), key=len)
print(sort_list[0])


print(longest_value2(fruits))

print(sys.path)
print(sys.meta_path)


    