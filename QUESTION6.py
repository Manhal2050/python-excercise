 binary_number=[]
 inp = int(input("Enter the decimal number: "))
 res = inp 
 while res != 0: 
      remind = res % 2                                                                                                                                                                                                                               
      binary_number.append(remind)
      res = res // 2
 binary_number.reverse()
 out="" 
 for i in binary_number:
    out = out +str(i)
 print(out) 


#This program gives the corresponding binary number to the decimal number where an empty matrix is defined and then the user is asked to enter a decimal number. The weel loop is used so that its work is sufficient for the length of what the result is not equal to zero. The While condition is met, and in the end the binary number is the numbers that entered the matrix, but are reversed, and then the print is done to show the result
