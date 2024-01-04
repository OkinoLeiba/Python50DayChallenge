#python challenge day43  
# Day 43: Student Marks  
 
# Write  a  function  called  student_marks  that  records  marks 
# achieved by students in a test. The function should ask the user 
# to input the name of the student and then ask the user to input 
# the  marks  achieved  by  the  student.  The  information  should  be 
# stored in a dictionary. The name is the key and the marks is the 
# value. When the user enters done, the function should return a 
# dictionary of names and values entered.




import sys, sysconfig


def student_marks() -> dict:
    
    counter = True
    student = ""
    student_id = 0
    name = ""
    mark = ""
    student_records = {student : {name:mark}}
    while counter:
        name = input("Input Student Name: ")
        mark = input("Input Student Mark: ")

    
        for stu in student_records.keys():
            if stu == student:    
                student_id += 1
                student = "student" + str(student_id)
                
        student_records[student] = {name:mark}
        
        done = input("Enter \"exit\" to Finish.\n")
        if done == "exit":
            counter = False
            break
            
    print(student_records)   
    return student_records
    
    
student_marks()


print(sys.getprofile())
print(sysconfig.get_makefile_filename())
print(sysconfig.get_config_vars())