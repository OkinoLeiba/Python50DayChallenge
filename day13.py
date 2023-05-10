#python challenge day13
# Day 13: Pay Your Tax  
# Write  a  function  called  your_vat.  The  function  takes  no 
# parameter. The function asks the user to input the price of an 
# item and VAT (vat should be a percentage). The function should 
# return the price of the item plus VAT. If the price is 220 and, 
# VAT is 15% your code should return a vat inclusive price of 253. 
# Make sure that your code can handle ValueError. Ensure the 
# code  runs  until  valid  numbers  are  entered.  (hint:  Your  code 
# should include a while loop). 
 
# Extra Challenge: Pyramid of Snakes  
# Write a function called Python_snakes that takes a number 
# as  an  argument  and  creates  the  following  shape,  using  the 
# number’s range: (hint: Use the loops and emoji library. If you 
# pass 7 as argument, your code should print the following:



import sys, re






def your_vat() -> None|str|float|tuple:

    LOOP = True
    while LOOP:
        
        price = input("What is the price of the item?\n")
        
         #price
        reg_price = re.findall("\d.\d", str(price))
        str_price = ".".join(reg_price)
        float_price = float(str_price)
    
        if float_price is int or float_price is float:
            raise ValueError("Please input a valid number! ")
            self.your_vat()

        vat = input("What is the value added tax as a percentage?\n")

       

        #vat
        vat = re.findall("\d", vat)
        str_vat = "".join(vat)
        percent_vat = int(str_vat)/100


        price_vat = float_price + (float_price * (percent_vat + 1))
        print("The value added price is", price_vat)

        LOOP = False
        
       
        while True: 
            try: 
                price = int(input("Enter the price of item: ")) 
                vat = int(input('Enter vat: ')) 
            except ValueError: 
                print("Enter a valid number.") 
            else: 
                price_vat2 = float_price + (float_price * (percent_vat + 1)) 
                return 'The price VAT inclusive is', price_vat2

# your_vat()



def python_snakes(num_input: int) -> None:
    from emoji import emojize
    input_array = []
    flag_list = []
    flag_list2 = []
    for inter in range(num_input):
        #snake
        input_array.append("\U0001f40d")
        snake_array = "".join(input_array)

        #flag1
        flag_list.append("\U0001f1ef")
        flag_array = "".join(flag_list)

        #flag2
        flag_list2.append("\U0001f1f2")
        flag2_array = "".join(flag_list2)
        
        
    for iter in range(0, num_input):
        for j in range(num_input, iter, -1): 
            print(end=" ")
        for jter in range(0, iter):
            print(emojize(":snake:"), end=" ")
        print("\n")
        
        
    for iter in range(0, num_input):
        print(emojize(":snake:")*iter, end=" ")
        print("\n")
        
    for iter in range(num_input, 0, -1):
        print(emojize(":snake:")*iter, end=" ")
        print("\n")
    

   	
    print(snake_array)
    print(flag_array)
    print(flag2_array)


python_snakes(7)



