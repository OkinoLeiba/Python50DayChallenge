#python challenge day14
# Day 14: Flatten the List  
# Write  a  function  called  flat_list  that  takes  one  argument,  a 
# nested  list.  The  function  converts  the  nested  list  into  a  one-
# dimension list. For example [[2,4,5,6]] should return 
# [2,4,5,6].  

# Extra Challenge: Teacher’s Salary 
# A  school  has  asked  you  to  write  a  program  that  will  calculate 
# teachers' salaries. The program should ask the user to enter the 
# teacher’s name, the number  of periods taught in a month, 
# and  the  rate  per  period.  The  monthly  salary  is  calculated  by 
# multiplying  the  number  of  periods  by  the  monthly  rate. 
# The  current  monthly  rate  per  period  is  $20.  If  a  teacher  has 
# more  than  100  periods  in  a  month,  everything  above  100  is 
# overtime. Overtime is $25 per period. For example, if a teacher 
# has  taught  105  periods,  their  monthly  gross  salary  should  be 
# 2,125. Write a function called your_salary that calculates a 
# teacher’s  gross  salary.  The  function  should  return  the 
# teacher’s name, periods taught, and gross salary. Here is 
# how you should format your output: 
 
# Teacher: John Kelly,  
# Periods: 105  
# Gross salary:2,125 
  

#constant module?
import sys

global BASE_PERIOD 
BASE_PERIOD = int(100)
global MONTHLY_RATE 
MONTHLY_RATE = int(20)
global OVERTIME_RATE 
OVERTIME_RATE = int(25)



"""  def __init__(self, nest_list) -> any:
        self.nest_list """

""" class Challenge:
    def _init_(self, nest_list):
        self.nest_list = nest_list """
        
new_list = []
new_list2 = []


def flat_list(nest_list: list) -> list|tuple:
    for iter in nest_list:
        for jter in iter:
            new_list.append(jter)

    new_list2 = [item for sublist in nest_list for item in sublist]  
    
      
    
    return new_list, new_list2


#all_day = Challenge()

nest_list = [["Please Please Me (1963)", "With The Beatles (1963)", "A Hard Day\'s Night (1964)", "Beatles For Sale (1964)",
    "Help! (1965)", "Rubber Soul (1965)","Revolver (1966)", "Sgt Pepper\'s Lonely Hearts Club Band (1967)", "The Beatles (White Album) (1968)",
    "Yellow Submarine (1969)","Abbey Road (1969)","Let It Be (1970)]"], ["Love Me Do", "Please Please Me", "Can't Buy Me Love", "I'll Follow the Sun", 
    "Help!", "Drive My Car",  "Eleanor Rigby", "Sgt. Pepper\'s Lonely Hearts Club Band", "Everybody's Got Something to Hide Except Me and My Monkey", 
    "Yellow Submarine", "Come Together","Let It Be"]]

#all_day.flat_list()
#flat_list(nest_list)

def your_salary() -> str:
    from re import findall
    
    name = input("Enter the Teacher\'s name: ")
    rate = input("Enter the Rate per Period: ")
    num_periods = int(input("Enter the Number of Periods: "))
    num_periods = int(num_periods)
    
    rate = int("".join(findall('\d', rate)))
    
    

   

    if num_periods <= BASE_PERIOD:
        gross_salary = num_periods * MONTHLY_RATE
    else:
        overtime_period = num_periods - BASE_PERIOD
        gross_salary = (num_periods * MONTHLY_RATE) + (overtime_period * OVERTIME_RATE)

    if num_periods <= BASE_PERIOD: 
        gross_salary = rate * num_periods 
    else: 
        gross_salary = (rate * BASE_PERIOD) + ((num_periods-BASE_PERIOD) * (rate + 5)) 

    # return gross_salary 

    print("Teacher: {}\nPeriods: {}\nGross Salary: {:,}".format(name, num_periods, gross_salary))


your_salary()

    

                




    









