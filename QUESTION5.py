L=['Network' , 'Math' , 'Programming', 'Physics' , 'Music'] 
max = 'Network' 
for i in L:
     if len(i) > len(max): 
        max = i 
 
print("The Longest word is: ", max) 


#This program defines an array containing several words and its task is to find the longest word, where in the beginning the first word in the array is assigned to a variable called Max, and through a loop, immediately, the elements of the matrix are rotated and compared to each word with the word saved in Max. If it is longer than it, it is placed instead of the old one, and so on. Until the elements of the matrix expire 
