#Loops are structures used to repeat sections of code. 
#They are useful if you have to do the smaet thing 
#more than once
#Or your can establish a pattern

#Example 1:


#This is counted loop. I want you to think about 
#count, check, change
#i = 0, 0 < 5 TRUE - RUN LOOP
#i = 1, 1 < 5 TRUE - RUN LOOP
#i = 2, 2 < 5 TRUE - RUN LOOP
#i = 3, 3 < 5 TRUE - RUN LOOP
#i = 4, 4 < 5 TRUE - RUN LOOP
#i = 5, 5 < 5 FALSE - EXIT AND MOVE ON


	#ANYTHING TABBED IS CONSIDERED THE LOOP BLOCK
	
#If you change your increment to go in reverse
#the check is always i > check, in theis case -1


#ALWAYS INDICATE THE LENGTH OF A WORD USING THE FUNCTION
#len 


print("*****Printing String Characters*****")
str = "Monkey"

for i in range (len(str)-1,-1,-1):
	print(str[i])


print("*****PRINT EVERY SECOND LETTER IN STR START AT INDEX 0******")
str = M1O2N3K4E5Y

for i in range(0, len(str), 2)
print (str[1])