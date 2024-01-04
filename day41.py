#python challenge day41
# Day 41: Only Words with Vowels  
# Create  a  function  called  words_with_vowels,  this  function 
# takes a string of words and returns a list of only words that have 
# vowels  in  them.  For  example,  ‘You  have no rhythm’  should 
# return [‘You’,’have’, ‘no’]. 

# Extra Challenge: Class of Cars  
# b.  Create  three  classes  of  three  car  brands  –  Ford,  BMW,  and 
# Tesla.  The  attributes  of  the  car's  objects  will  be,  model, 
# color, year, transmission, and whether the car is 
# electric or not (Boolean value.) Consider using inheritance 
# in your answer. 
# You will create one object for each car brand: 
#  bmw1 : model: x6, Color: silver, Year: 2018, Transmission: Auto, Electric: False  
# tesla1:  model: S, Color: beige, Year: 2017, Transmission: Auto, Electric: True 
# ford1 :  model:  focus, Color: white, Year: 2020, Transmission: Auto, Electric: False 
 
# You will create a class method, called print_cars that will be 
# able to print out objects of the class. For example, if you call the 
# method  on  the  ford1  object  of  the  Ford  class,  your  function 
# should be able to print out car info in this exact format: 
# car_model = focus 
# Color = White  
# Year = 2020  
# Transmission = Auto  
# Electric = False


def words_with_vowels(str_input: str) -> None:
    from operator import eq, __eq__, contains
    test = eq("a", "a")
    test2 = __eq__("a", "a")
    test3 = contains(["a", "e", "i", "o", "u"], "a")
    vowels =  ["a", "e", "i", "o", "u"]
    result_list = []
    for word in str_input.lower().split():
        for letter in word:
            if contains(vowels, letter):
                result_list.append(word)
                
    result_list3 = [] 
    for word in str_input.lower().split(): 
        for letter in word: 
            if letter in vowels: 
                if word not in result_list3: 
                    result_list3.append(word) 
                
               
    result_list2 = [word for word in str_input.lower().split() if contains(vowels, word)]
                
    pass



str_input = "You  have no rhythm"
# words_with_vowels(str_input)



class Cars:
    def __init__(self, key, car_model, color, year, transmission, electric_bool) -> None:
        self.key = key
        self.car_model = car_model 
        self.color = color  
        self.year = year  
        self.transmission = transmission  
        self.electric = electric_bool


    
    def get_car(self) -> None|tuple:
        return self.key, self.car_model, self.color, self.year, self.transmission, self.electric
        # bmw1 = {"model": "x6", "color":"silver", "year": 2018, "transmission": "auto", "electric": False}
        # tesla1 = {"model": "S", "color":"beige", "year": 2017, "transmission": "auto", "electric": True}
        # ford1 =  {"model": "focus", "color":"white", "year": 2020, "transmission": "auto", "electric": False}
        
    
    def set_car(self) -> None:
        self.key = {"car_model":self.car_model, "color":self.color, "year":self.year, "transmission":self.transmission, "electric_bool":self.electric}
        
        
        
    def del_car(self) -> None:
        del self.key, self.car_model, self.color, self.year, self.transmission, self.electric
        

cars = Cars
# bmw_prop = property(cars.get_car, cars.set_car, cars.del_car)
        

class Cars2:
    def __init__(self, key, car_model, color, year, transmission, electric_bool) -> None:
        self.key = key
        self.car_model = car_model 
        self.color = color  
        self.year = year  
        self.transmission = transmission  
        self.electric = electric_bool
   
   
    def printCar(self) -> None:
        print ("Car_Model = {}\nColor = {}\nYear = {}\nTransmission = {}\nElectric = {}".format(self.car_model, self.color, self.year, self.transmission, self.electric).upper())
        
        
        
        
class BMW1(Cars):
    pass

bmw = BMW1("bmw1", "x6", "silver", 2018, "auto", False)   

    
        
class BMW2(Cars2):
    pass

bmw2 = BMW2("bmw1", "x6", "silver", 2018, "auto", False)
bmw2.printCar()


class Cars3:
    def __init__(self) -> None:
        self.key = None
        self.car_model = None 
        self.color = None  
        self.year = None  
        self.transmission = None  
        self.electric = None


    @property
    def car(self) -> None|tuple:
        return self.key, self.car_model, self.color, self.year, self.transmission, self.electric
        # bmw1 = {"model": "x6", "color":"silver", "year": 2018, "transmission": "auto", "electric": False}
        # tesla1 = {"model": "S", "color":"beige", "year": 2017, "transmission": "auto", "electric": True}
        # ford1 =  {"model": "focus", "color":"white", "year": 2020, "transmission": "auto", "electric": False}
        
    @car.setter
    def car(self, key, car_model, color, year, transmission, electric_bool) -> None:
        self.key = {"car_model":self.car_model, "color":self.color, "year":self.year, "transmission":self.transmission, "electric_bool":self.electric}
        
        
    @car.deleter   
    def car(self) -> None:
        del self.key, self.car_model, self.color, self.year, self.transmission, self.electric
        
        
        
        
class Cars4: 
    def __init__(self, model, color, year, transmission, electric=False) -> None: 
        self.model = model 
        self.color = color 
        self.year = year 
        self.transmission = transmission 
        self.electric = electric 
 

    def print_car(self) -> None: 
        print("car_model = {self.model}\nColor = {self.color}\nYear = {self.year}\nTransmission = {self.transmission}\nElectric = {self.electric}")
 
class BMW(Cars4): 
    def __init__(self, model, color, year, transmission, electric=False) -> None: 
        Cars4.__init__(self, model, color, year, transmission, electric=electric) 
 
 
class Tesla(Cars4): 
    def __init__(self, model, color, year, transmission, electric=False) -> None: 
        Cars4.__init__(self, model, color, year, transmission, electric=electric) 
 
 
class Ford(Cars4): 
    def __init__(self, model, color, year, transmission, electric=False) -> None: 
        Cars4.__init__(self, model, color, year, transmission, electric=electric) 
 
 

ford1 = Ford("focus", "white", 2017, "auto", False) 
print(ford1.print_car()) 
tesla1 = Tesla("S", "grey", 2016, "manual", True) 
print(tesla1.print_car()) 
bmw1 = BMW("x6", "silver", 2018, "auto", False) 
print(bmw1.print_car())