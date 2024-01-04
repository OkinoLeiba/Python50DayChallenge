#python challenge day42
# Day 42: Spelling Checker  
# Write a function called spelling_checker. This code asks the 
# user  to  input  a  word  and  if  a  user  inputs  a  wrong  spelling  it 
# should  suggest  the  correct  spelling  by  asking  the  user  if  they 
# meant to type that word. If the user says no, it should ask the 
# user  to  enter  the  word  again.  If  the  user  says  yes,  it  should 
# return  the  correct  word.  If  the  word  entered  by  the  user  is 
# correctly spelled the function should return the correct word. 
# Use the module textblob.  
 
# Extra Challenge: Create an Alarm clock  
# Create a function called alarm that sets an alarm clock for the 
# user. The function should ask the user to enter time they want 
# the  alarm  to  go  off.  The  user  should  enter  the  hour  and 
# minute. The function should then print out the time when the 
# alarm will go off. When its alarm time, the code should let off a 
# sound. Use the winsound module for sound. 

import textblob

def spelling_checker(response) -> None:
    
    counter = True
    while counter:
        if response.lower() == "yes":
            counter = False
            print("Excellent!")
            break
        else:
            checker()
            counter = True
            
            
    while True: 
        word = input("Enter a word to the check spelling and to check the spelling of the word: ") 
        if word != textblob.TextBlob(word).correct(): 
            correct_spell = input(f"Is this the correct spelling {textblob.TextBlob(word).correct()}?.\nType Yes/No") 
            if correct_spell.lower() == "yes": 
                break 
            else: 
                print("Please try again") 
        
        elif word == textblob.TextBlob(word).correct(): 
            break 
        print("Your word is", {textblob.TextBlob(word).correct()})
      
      
            
def checker() -> None:
    
    word_check = input("Input word for spellchecker...\nCheck yourself before you wreck yourself!: \n")

    spell_check = textblob.TextBlob(word_check)

    correct_spell = spell_check.correct()

    print("Is this the correct word \"{}\".".format(correct_spell))
    response = input()   
    
    spelling_checker(response)

# checker()



def alarm() -> None:
    import string, re, datetime, winsound
    alarm_time = input("Set Alarm: ")
    
    test1 = alarm_time.lstrip().rstrip().split(":")
    test2 = [item for item in alarm_time]
    test3 = filter(lambda alarm_time: alarm_time.isnumeric(), alarm_time)
    
    num_alarm = re.findall("\d", alarm_time)
    
    counter = True
    while counter:
        if int(num_alarm[1]) > 6:
            alarm_time = input("Set Alarm: ")
            num_alarm = re.findall("\d", alarm_time)
            counter = True
        else:
            counter = False
    
    test =  datetime.time(hour = int(num_alarm[0]), minute = int(num_alarm[1] + num_alarm[2]))
    test1 = datetime.time()
    test2 = datetime.datetime.now().strftime("%H:%M") 
    if datetime.time(hour = int(num_alarm[0]), minute = int(num_alarm[1] + num_alarm[2])) == datetime.time():
        print("ALARM!")
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    
    print(test3)
    pass


alarm()