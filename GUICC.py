#THis improts the tkinter "tool box" this contains
#all the support material to make GUI elements
#by including "as tk" we are givinga short name to 
#use. 
import tkinter as tk



#Main window
root = tk.Tk() 
# creates the standard main window.

#			Tabs   


# Three stages t build elements/ objects
#1) CONSTRUCT the Object: We build and configure it.
#2) CONSTRUCT the Object: We specify behaviours and settings (OPTIONAL)
#3) Pack the Object: Put it in the window.
output = tk.Text(root,height = 30, width =10) #Parameters are what we send in.

#Ordered parameters: The order we send them matters. (COMMON)

#Named paramters: JavaScpript and Python specific



#Using grid instead of pack 
#To make the columns and rows


#					Titles

labele = tk.Label(root, text = "Relative Calculator", font = ("Helvitica",20))
labele.grid(row = 0, column = 1, sticky = "NESW")

labele = tk.Label(root, text = "First Relative", font = ("Helvitica",16))
labele.grid(row = 2, column = 0, sticky = "NESW")

labele = tk.Label(root, text = "Second Relative", font = ("Helvitica",16))
labele.grid(row = 2, column = 1, sticky = "NESW")

labele = tk.Label(root, text = "Third Relative", font = ("Helvitica",16))
labele.grid(row = 2, column = 2, sticky = "NESW")

labele = tk.Label(root, text = "Relative", font = ("Helvitica",20))
labele.grid(row = 14, column = 1, sticky = "NESW")

labele = tk.Label(root, text = "Y = Younger", font = ("Helvitica",14))
labele.grid(row = 2, column = 3)

labele = tk.Label(root, text = "O = Older", font = ("Helvitica",14))
labele.grid(row = 3, column = 3)

outpute = tk.Text(root, width=35, height=3, borderwidth = 3, relief=tk.GROOVE)
outpute.config(state = 'disabled')
outpute.grid(row=15, column=1)


#   	Defining Relatives

#  Gives the relative names a variable // Defines it

var1e = tk.IntVar()
var2e = tk.IntVar()
var3e = tk.IntVar()
var4e = tk.IntVar()
var5e = tk.IntVar()
var6e = tk.IntVar()
var7e = tk.IntVar()
var8e = tk.IntVar()
var9e = tk.IntVar()
var10e = tk.IntVar()
var11e = tk.IntVar()
var12e = tk.IntVar()
var13e = tk.IntVar()
var14e = tk.IntVar()
var15e = tk.IntVar()
var16e = tk.IntVar()
#What the named parameter viriable does is binds 


# 					Rectangles







#              FIRST RELATIVE

cHCe = tk.Checkbutton(root, text ="Dad", variable=var1e)
cHCe.grid(row=4, column =0, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Mom", variable=var2e)
cHCe.grid(row=5, column =0, sticky = "NESW")


#              SECOND RELATIVE




cHCe = tk.Checkbutton(root, text ="Dad", variable=var3e, font = ("Helvitica",13))
cHCe.grid(row=4, column =1, stick = "NESW")

cHCe = tk.Checkbutton(root, text ="Mom", variable=var4e, font = ("Helvitica",13))
cHCe.grid(row=5, column =1, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Sister(Y)", variable=var5e, font = ("Helvitica",13))
cHCe.grid(row=6, column =1, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Sister(O)", variable=var6e, font = ("Helvitica",13))
cHCe.grid(row=7, column =1, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Brother(Y)", variable=var7e, font = ("Helvitica",13))
cHCe.grid(row=8, column =1, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Brother(O)", variable=var8e, font = ("Helvitica",13))
cHCe.grid(row=9, column =1, sticky = "NESW")



#              THIRD RELATIVE
cHCe = tk.Checkbutton(root, text ="Dad", variable=var9e, font = ("Helvitica",13))
cHCe.grid(row=4, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Mom", variable=var10e, font = ("Helvitica",13))
cHCe.grid(row=5, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Sister(Y)", variable=var11e, font = ("Helvitica",13))
cHCe.grid(row=6, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Sister(O)", variable=var12e, font = ("Helvitica",13))
cHCe.grid(row=7, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Brother(Y)", variable=var13e, font = ("Helvitica",13))
cHCe.grid(row=8, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Brother(O)", variable=var14e, font = ("Helvitica",13))
cHCe.grid(row=9, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Son", variable=var15e, font = ("Helvitica",13))
cHCe.grid(row=10, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(root, text ="Daughter", variable=var16e, font = ("Helvitica",13))
cHCe.grid(row=11, column =2, sticky = "NESW")
 


root.mainloop() #Starts the program
