#python challenge day5
# Day 5: My Discount  
# Create a function called my_discount. The function takes no 
# arguments but asks the user to input the price and the 
# discount (percentage) of the product. Once the user inputs the 
# price and discount, it calculates the price after the discount. 
# The  function  should  return  the  price  after  the  discount.  For 
# example, if the user enters 150 as price and 15% as the discount, 
# your function should return 127.5. 
 
# Extra Challenge: Tuple of Student Sex  
# You work for a school and your boss wants to know how many 
# female and male students are enrolled in the school. The school 
# has saved the students in a list. Your task is to write a code that 
# will count how many males and females are in the list. Here is a 
# list below: 
#  students = ['Male', 'Female', 'female', 'male', 'male', 'male', 
#             'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female'] 
 
# Your  code  should  return  a  list  of  tuples.  The  list  above  should 
# return: 
#  [(‘Male’,7), (‘female’,6)] 
  

import sys, math



def my_discount(price: float, discount:float) -> None:
    price = int(price)
    discount =  float(discount) / 100
    new_price = price - (price*discount)

    new_price2 = int(price) - (int(price) * (float(discount)/100))
    print(new_price)
    



#price = input("Input Price: ")
#discount = input("Input Discount: ")

#my_discount(price, discount)


def gender_count(students: list) -> None|str:
    from collections import Counter
    count_male = 0
    count_female = 0

    lower_case_stu = [x.lower() for x in students]
    
    count_male2 = lower_case_stu.count("male")
    count_female2 = lower_case_stu.count("female")
    
    count = Counter(lower_case_stu)
    count_male3 = count['male']
    count_female3 = count['female']

    count_male4 = [x.count() for x in lower_case_stu if lower_case_stu == "male"]
    count_female5 = [x.count() for x in lower_case_stu if lower_case_stu == "female"]
    
    for x in lower_case_stu:
        if x == "male":
            count_male += 1
            break
        elif x =="female":
            count_female += 1
            break
        else:
            return None
    
    male_list = tuple(["Male", count_male])
    female_list = tuple(["Female", count_female])

    new_list = [male_list, female_list]

    print(new_list)

    


students = ["Male","Female", "female", "male","male","male","female","male","Female","Male","Female","Male","female"]

gender_count(students)


