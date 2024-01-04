#python challenge day47
# Day 47: Save a JSON  
 
# Write a function called save_json. This function takes a 
# dictionary below as an argument and saves it on a file in JSON 
# format. 
 
# Write  another  function  called  read_json  that  opens  the  file 
# that you just saved and reads its content. 
# names = {'name': 'Carol','sex': 'female','age': 55} 
 
  



import json

def save_json(names: dict) -> None: 
    j_data = json.dumps(names)
    read_json(j_data)
    
    with open("file.json", "w") as file: 
        #saving to file and adding indent 
        json.dump(names, file)


def read_json(j_data: str) -> None:
    json.loads(j_data)

    with open("file.json", "r") as file: 
        json_file = json.load(file)


names = {'name': 'Carol','sex': 'female','age': 55} 
save_json(names)
    