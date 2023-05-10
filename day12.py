#python challenge day12  
# Day 12: Count the Dots  
# Write  a  function  called  count_dots.  This  function  takes  a 
# string  separated  by  dots  as  a  parameter  and  counts  how  many 
# dots  are  in  the  string.  For  example,  ‘h.e.l.p.’ should return 4 
# dots, and ‘he.lp.’ should return 2 dots. 
# Extra Challenge: Your Age in Minutes  
# Write a function called age_in_minutes that tells a user how 
# old  they  are  in  minutes.  Your  code  should  ask  the  user  to 
# enter  their  year  of  birth,  and  it  should  return  their  age  in 
# minutes (by subtracting their year of birth to the current year). 
# Here are things to look out for: 
 
# a. The  user  can  only  input  a  4-digit  year  of  birth.  For 
# example,  1930  is  a  valid  year.  However,  entering  any 
# number  longer  or  less  than  4  digits  long  should  render 
# input invalid. Notify the user to input a four digits 
# number. 
# b.  If  a  user  enters  a  year  before  1900,  your  code  should 
# tell  the  user  that  input  is  invalid.  If  the  user  enters  the 
# year after the current year, the code should tell the user, 
# to input a valid year. 
# The  code  should  run  until  the  user  inputs  a  valid  year. 
# Your  function  should  return  the  user's  age  in  minutes.  For 
# example,  if  someone  enters  1930,  as  their  year  of  birth  your 
# function should return: 
# You are 48,355,200 minutes old.


import sys, re, datetime, math



def count_dots(input_string: str) -> str:
    list_string = list([iter for iter in input_string.split(" ")])
    test = [list(iter) for iter in input_string.split(" ")]
    list_string2 = re.findall('.', input_string)
    count_of_dots2 = len([iter for iter in list_string2 if iter == '.'])
    
    # count_of_dots3 = sum([int(iter) for iter in input_string if iter == '.'])

    count_of_dots = list_string.count('.')

    count_of_dots3 = all(1 for iter in input_string if "." in iter)
    print(count_of_dots2)



input_string = "h.e.l.p"
input_string2 = "he.lp."
count_dots(input_string)


def age_in_mintes() ->int|str|None:
    from operator import lt, gt

    LOOP = True

    while LOOP:
        year_input = input("Please input your birth year: ")
        length = len(list(year_input))    
        current_year = datetime.datetime.now().year 
        current_year2 = int(datetime.datetime.now().strftime("%Y"))
        year_input = int(year_input)
        length = int(length)
        current_year = int(current_year)
        

        # if length < 4:
        if lt(length, 4) or gt(length, 4):
            print("Input a four year digit number!")
        elif int(year_input) <= 1900:
            print("Input a year after 1900!")
        elif int(year_input) == int(current_year):
            print("Input a year that is not the current year!")
        elif length == 4:
            min_year = math.fabs(current_year - year_input) * 525949.2
            
            print("You are {:.0f} minutes old.".format(min_year))
            return f"You are {min_year} minutes old."
            # 48,355,200 
            LOOP = False   
        else:
            print("Please Try Again.")
     
    current_year = datetime.datetime.now().year         
    while (year_input := int(input('Enter your year of birth: '))) not in range(1900, current_year):
        print("Enter a valid year between 1900 and 2022.")
    else:
        return (current_year - year_input) * 365 * 24 * 60

age_in_mintes()


print(sys.getfilesystemencoding())
