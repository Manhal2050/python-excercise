 
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
proc = input("Enter the process (*,/,+,-):")
if (proc=='*'): 
    print(num1*num2)
elif(proc=='/'):    
   print(num1/num2)
elif(proc=='+'):     
  print(num1+num2) 
else: 
   print(num1-num2) 

#This program asks the user to enter two numbers, Then the user is asked to enter the mathematical operation he wantsso that if the operation is a multiplication, the product of the two numbers is printed, and if it is an addition, the sum of the two numbers is printed, and so on.

