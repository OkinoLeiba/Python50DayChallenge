#python challenge day24
# Day 24: Average Calories 
 
# Create  a  function  called  average_calories  that  calculates  the 
# average calories intake of a user. The function should ask the user 
# to input their calories intake for any number of days and once they 
# hit ‘done’ it should calculate and return the average intake. 
  
# Extra Challenge: Create a Nested List  
# Write a function called nested_lists that takes any number of 
# lists and creates a 2-dimensional nested list of lists. For example, 
# if you pass the following lists as arguments: [1, 2, 3, 5], [1, 2, 3, 
# 4], [1, 3, 4, 5]. 
# Your code should return: [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]

import statistics, sys



def average_calories() -> None:
    calories_list = []
    counter = True
    while counter:
        calories_dict = {}
        day = input("Enter the Day: \n").lower()
        calories = input("Enter the Calories: ")
        done = input()
        if done.lower( ) == "done":
            counter = False
            break
        
        calories_dict[day] = calories
        
        calories_list.append(calories)
        
    avg_cal = lambda avg: statistics.mean(calories_dict.values())
        
    print(avg_cal)
    
# average_calories()


def nest_list(*list_input: list) -> None:
    print(list_input)
    nest = [nlist for nlist in list_input]
    nest1 = [list_input]
    nest2 = list(list_input)
    
    nest_list = []
    for list_nest in range(len(list_input)):
        for iter in list_input:
            nest_list.append(iter)
        break
            
    print(nest)
    print(nest_list)
    

list_input = [1, 2, 3, 5], [1, 2, 3,  4], [1, 3, 4, 5]
nest_list(list_input)


print(sys.argv)