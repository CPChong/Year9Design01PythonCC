#tkinter is a module that holds all the function
#that let us easily make GUI elements
import tkinter as tk

#creating the main window. To do this we need 
#to call the Tk() function
root = tk.Tk()

#These are just buttons,
#NEED TO PACK AFTER THIS

label = tk.Label(root, text = "Mandarin Name Relative Finder")
label.grid(row = 0, column = 0, columnspan = 2)
#Columnspan spreads title over the
#whole thing

#Making grid, needs column and row


btn1 = tk.Button(root, text = "1")
btn1.config(width = 5, height = 5)
btn1.grid(row = 1, column = 0, sticky = "NESW")

btn2 = tk.Button(root, text = "2")
btn2.config(width = 5, height = 5)
btn2.grid(row = 1, column = 1, sticky = "NESW")

btn3 = tk.Button(root, text = "3")
btn3.config(width = 5, height = 5)
btn3.grid(row = 2, column = 0, sticky = "NESW")

btn4 = tk.Button(root, text = "4")
btn4.config(width = 5, height = 5)
btn4.grid(row = 2, column = 1, sticky = "NESW")


#This is the main code to start the window
#Loops it for you
#Start then out stuff in the window


#This line display the root ands sets the program
#in an infinit loop. This is an EVENT DRIVEN PROGRAM

#Waits for user to do something ex. click the button 
root.mainloop()



