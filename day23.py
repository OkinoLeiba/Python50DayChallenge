#python challenge day23
# Day 23: Simple Calculator  
# Create a simple calculator. The calculator should be able to perform 
# basic math operations, add, subtract, divide and multiply. The 
# calculator  should  take  input  from  users.  The  calculator  should  be 
# able to handle ZeroDivisionError, NameError, and 
# TypeError. 
 
# Extra Challenge: Multiply Words  
# s = "love live and laugh"  
# Write a function called multiply_words that takes a string as an 
# argument  and  multiplies  the  length  of  each  word  in  the  string  by 
# the  length  of  other  words  in  the  string.  For  example,  the  string 
# above should return 240 - love (4) live (4) and (3) laugh (5). 
# However, your function should only multiply words will all 
# lowercase letters. If a word has one upper case letter, it should be 
# ignored.  For example, the following string: 
# s = "Hate war love Peace" should return 12 – war (3) love (4). 
# Hate  and  Peace  will  be  ignored  because  they  have  at  least  one 
# uppercase letter. 



if __name__ == "__main__":
    class Simple_Calculator:
        # def __init__(self, inti) -> None:
        #     inti = inti
        #     pass
            
        @classmethod  
        def input_operation(cls) -> None:
            sc = Simple_Calculator
            print("Choose Mathematical Operation:\n0: Addition:\n1: Subtraction\n2: Division\n3: Multiplication\n")
            operation = input()
            operation = operation.lower()
            # if operation == 'Addition' or operation == 'ADDITION' or operation == 'addition':
            #     operation.lower()
            if operation not in ['0', '1', '2', '3']:
                print("No, Nope, Naught...Please choose a number between zero and four, or name of the operation")
                cls.input_operation()
            print("\nInput First Number: \n")
            num1 = input()
            print("\nInput Second Number: \n")
            num2 = input()
            # input validation: valuerror, second check embedded at function invocation

            try:
                num1 = float(num1)
                num2 = float(num2)
            except TypeError:
                print("Please input a number.\n")
                # do while loop
                sc.input_operation()
        
            try:
                match operation:
                    
                    case '0' | 'addition': 
                        # type: ignore 
                        sc.add(num1, num2)
                    case '1' | 'subtract':  
                        # type: ignore 
                        sc.subtract(num1, num2)  
                    case '2' | 'divide':  
                        # type: ignore 
                        sc.divide(num1, num2) 
                    case '3' | 'multiply': 
                        # type: ignore  
                        sc.multiply(num1, num2)  
                        
                """"""        
                # if operation == '0' or operation == 'addition': 
                #         # type: ignore 
                #         sc.add(num1, num2)
                # elif operation == '1' or operation == 'subtract':  
                #         # type: ignore 
                #         sc.subtract(num1, num2)  
                # elif operation == '2' or operation == 'divide': 
                #         # type: ignore 
                #         sc.divide(num1, num2) 
                # elif operation == '3' or operation == 'multiply':  
                #         # type: ignore  
                #         sc.multiply(num1, num2) 
                          
                # def wrapper_function(cls, operation):
                #     operation.replace("add", "0")
                #     operation.replace("subtract", "1")
                #     operation.replace("divide", "2")
                #     operation.replace("multiply", "3")
                #     return getattr(cls, "case_" + str(operation))
                
                # def case_1():
                #     # type: ignore 
                #     sc.add(num1, num2)
                #     sc.subtract(num1, num2) 
                #     sc.divide(num1, num2)
                #     sc.multiply(num1, num2)
                    
                # switch = {
                #     0: cls.add(num1, num2)
                #     1: cls.subtract(num1, num2)
                #     2: cls.divide(num1, num2)
                # }
                """"""
                    
                        
            except NameError:
                sc.input_operation()
            
        
        @classmethod            
        def add(cls, num1, num2) -> None:
            sc = Simple_Calculator
            try:
                result = num1 + num2
                print("The result is: {:.2f}".format(result))
            except TypeError:
                print("Choose a numerical value, you were warned [angry baby emoji]!")
                sc.input_operation()
            
        @classmethod           
        def subtract(cls, num1, num2) -> None:
            # sc = Simple_Calculator
            try:
                result = num1 - num2
                print("The result is: %.2f" %result)
            except TypeError:
                print("Choose a numerical value, you were warned [angry baby emoji]!")
                cls.input_operation()
            
        @classmethod
        def divide(cls, num1, num2) -> None:
            # sc = Simple_Calculator
            try:
                result = num1 / num2
                print("The result is: {:.2f}".format(result))
            except TypeError:
                print("Choose a numerical value, you were warned [angry baby emoji]!")
                cls.input_operation()
            except ZeroDivisionError:
                print("I pity the fool who try to divide by zero, you can not divide by zero.")
                cls.input_operation()
                    
        @classmethod           
        def multiply(cls, num1, num2) -> None:
            # sc = Simple_Calculator
            #  result = 0
            try:
                result = num1 * num2
                print("The result is: %.2f" %result)
            except TypeError:
                print("Choose a numerical value, you were warned [angry baby emoji]!")
                cls.input_operation()
            
        
    inti="True"
    simple_calculator = Simple_Calculator
    # simple_calculator.input_operation()
    # simpleCalculator()
        
        
  
    
def multiply_words(string_input: str) -> None:
    from math import prod
    result = prod([len(word) for word in string_input.split(" ") if word.lower()])
    return result

    result_arry = []
    for word in string_input.split(" "):
        if word.lower():
            mult_result = prod(result_arry.append(len(word)))
     
   
    
    
     
     
     
     
string_input = "love live and laugh" 
# string_input = "Hate war love Peace"
multiply_words(string_input)
 
 
def simpleCalculator() -> None|str:
    import operator     
    try: 
        num_input1 = int(input("Enter number: \n"))
        operation = input("Pick operator(+,-,*,/): \n") 
        num_input2 = int(input('Enter another number: \n')) 
        if operation not in ['+', '-', '*', '/'] or len(operation) > 1: 
            print('Please enter a valid operator') 
    except ValueError: 
        print('Please enter a valid number') 
    except ZeroDivisionError: 
        print('You cannot divide a number by zero.Try again') 
    else: 
        if operation == '+': 
            return f'Answer is: {operator.add(num_input1, num_input2)}' 
        elif operation == '-': 
            return f'Answer is: {operator.sub(num_input1, num_input2)}' 
        elif operation == '*': 
            return f'Answer is: {operator.mul(num_input1, num_input2)}' 
        elif operation == '/': 
            return f' Answer is: {operator.truediv(num_input1, num_input2)}' 
        return 'Try again'