#python challenge day2
# Day 2: Strings to Integers
# Write a function called convert_add that takes a list of strings
# as an argument and converts it to integers and sums the list. For
# example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
# summed to 9.

# Extra Challenge: Duplicate Names
# Write a function called check_duplicates that takes a list of
# strings as an argument. The function should check if the list has
# any duplicates. If there are duplicates, the function should return
# the duplicates. If there are no duplicates, the function should
# return "No duplicates". For example, the list of fruits below
# should return apple as a duplicate and list of names should
# return "no duplicates".
# fruits = ['apple', 'orange', 'banana', 'apple']
# names = ['Yoda', 'Moses', 'Joshua', 'Mark']


import math, re, itertools




def convert_add(values: list) -> int:
    from operator import add
    int_val = []
    for value in values:
        int_val.append(int(value))
        
        
    
    int_val2 = [int(value) for value in values]
    # int_val3 = int(values) //typeError
    # lambda x: int(x)
    
    int_val5 = map(lambda x: int(x), values)
    
    the_sum = itertools.accumulate(map(lambda x: int(x), values), func=add)
    
    int_val4 = []
    for value in values:
        int_val4.append(int(value))
    
    sumup = 0    
    for value in int_val4:
        sumup += value

    return sum(int_val)

   
values = ["1", "3", "5"]
print(convert_add(values))


def check_duplicates(input) -> None:
    iterator_counter = 0
    try:
        while iterator_counter < len(input):
            if input[iterator_counter] == input[iterator_counter+1]:
                print("Duplicates")
            if input[iterator_counter] != input[iterator_counter+1]:
                print("No Duplicates")
            iterator_counter+=1
    except:
        IndexError
       

   

def check_duplicates2(input: list) -> None:
    check_list = bool(iter for fruit in input if fruit == fruit)
    if check_list == True:
        print("Duplicates")
    else:
        print("No Duplicates")

""" def check_duplicates_reg(input):
    re.search("apple", input)
    for x in input:
        if re.search("apple", input):
            print("Duplicate")
        else:
            print("No Duplicates") """

def check_list(fruits: list, names: list) -> bool|None:
    for fruit in names:
        for name in fruits:
            if fruit == name:
                return True
                print("The truth of the matter")
            else:
                print("Never pure and rarely simple")


def check_duplicates3(fruits: list) -> str|None:
    #for iterable in fruits:
        i = 1
        while i < len(fruits):
            if [iterable for iterable in fruits] == fruits[i]:
                return "A Few Good Men"
            else:
                return "The truth is the lie"
        i += 1

def check_duplicates4(fruits: list) -> str|None:
    for fruit in fruits:
        if fruits.count(fruit) > 1:
            return print("Duplicates {}".format(fruit))
        else:
            return f"Not To Be the Duplicates"
    
    


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark', 'orange']
list = ["apple", "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "apple"]
#check_duplicates2(list)
eval_list = {fruit for fruit in fruits}
if len(fruits) < len(eval_list):
    pass



check_duplicates3(fruits)
