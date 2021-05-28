import json
def main(): 
    file = open("dict_json.json",'r')  
    translator = json.load(file) 
    inp = input("Enter your state\n (U:user, D:Developer): ") 
    if inp == 'U': 
        user(translator)    
    else: 
        developer(translator) 
 def user(translator): 
        res =''  
   while True: 
         res = input("Enter an English word: 
('exit'\n to end)") 
        if res == 'exit': 
            break 
        print(translator[res]) 
 def developer(translator):
     while True: 
        en = input("Enter The English word 
('exit'\n to end):")       
        if en == 'exit':          
           break 
        ar = input("Enter The Arabic word:")     
        translator[en]=ar    
 file = open("dict_json.json",'w')   
  json.dump(translator,file) 
 main()


#This program is an Arabic-English dictionary. At the beginning, we call Al-Jasson, which is a library of coding represented by Dump and decoding the coding in the load, and it has two main parts, the user for entering a foreign word and knowing its translation, and the developer to insert a foreign word and its facilities in Arabic and save it for thenext operation.
