#python challenge day44
# Day 44: Save Emails  
# Create  a  function  called  save_emails.  This  function  takes  no 
# arguments  but  asks  the  user  to  input  email,  and  it  saves  the 
# emails in a CSV file. The user can input as many emails as they 
# want. Once they hit ‘done’ the function saves the emails and 
# closes  the  file.  Create  another  function  called  open_emails. 
# This function opens and reads the content of the CSV file. Each 
# email must be in its line. Here is an example of how the emails 
# must be saved: 
# jj@gmail.com 
# kate@yahoo.com 
  
# and not like this: 
# jj@gmail.comkate@yahoo.com 



import os, re

 
def save_emails() -> None:
    file = open(file="C:/Users/Owner/source/vsc_repo/python_challenge/python.csv", mode='w', encoding="utf-8", errors="strict")
      
    counter = True
    while counter:
    
        email = input("Enter e-mail: ")
            
        if email.lower() == "done":
            counter = False
            break
        elif not(re.search("^[\w\.]+@([\w]+\.)+[\w]{2,4}$", email)):
            print("This is not a valid email!")
            # email = input("Enter a valid e-mail: ")
        else:
            file.write(email + "\n")
            print("Type \"done\" when finished.\n")
            
            
       
        
    
    file.close()
    
    
def open_emails() -> None:
    file = open(file="python.csv", mode='r', encoding="utf-8", errors="strict")
    
    file_content = file.readlines()

    
    file.close()
    
    
   
   
    
save_emails()

open_emails()