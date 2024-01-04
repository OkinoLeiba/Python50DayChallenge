#python challenge day29
# Day 29: Middle Figure  
# Write a function called middle_figure that takes two 
# parameters a, and b. The two parameters are strings. The 
# function joins the two strings and finds the middle element. 
# If the combined string has a middle element, the function should 
# return the element, otherwise, return ‘no middle figure’. Use 
# ‘make  love’  as  an  argument for  a  and  ‘not  wars’  as an 
# argument  for  b.  Your  function  should  return  ‘e’ as  the  middle 
# element. Whitespaces should be removed. 
  



if __name__ == "__main__":            

    def middle_figure(string1: str, string2: str) -> None|str:
        import statistics, math
        
        trim_str = (string1 + string1).replace(" ","").strip()
        middle = len(trim_str) // 2 
        if len(trim_str) % 2 == 1: 
            print(trim_str[middle])
        else: 
            print('No middle figure')
        
        
        test = math.floor(len((string1+string2).replace(" ", ""))/2)
        middle_value = (string1+string2).replace(" ", "")[math.floor(len((string1+string2).replace(" ", "").strip())/2):math.ceil(len((string1+string2).replace(" ", "").strip())/2)]
        if type(middle_value) == str and len(trim_str) % 2 == 1:
            return middle_value
        else: 
            return f"No Middle Figure!"
        
        
       
    string1 = "make  love"
    string2 = "not  wars"
    middle_figure(string1, string2)