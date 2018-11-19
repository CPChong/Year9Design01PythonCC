#THis improts the tkinter "tool box" this contains
#all the support material to make GUI elements
#by including "as tk" we are givinga short name to 
#use. 
import tkinter as tk

#Main window
root = tk.Tk() 
# creates the standard main window.



# THree stages t build elements/ objects
#1) CONSTRUCT the Object: We build and configure it.
#2) CONSTRUCT the Object: We specify behaviours and settings (OPTIONAL)
#3) Pack the Object: Put it in the window.

output = tk.Text(root,height = 10, width =30) #Parameters are what we send in.

#Ordered parameters: The order we send them matters. (COMMON)

#Named paramters: JavaScpript and Python specific



#Using grid instead of pack 
#To make the columns and rows


labInput1 = tk.Label(root, text = "Relative Calculator")
labInput1.grid(row = 0, column = 1, sticky = "NESW")

labInput1 = tk.Label(root, text = "First Relative")
labInput1.grid(row = 2, column = 0, sticky = "NESW")

labInput1 = tk.Label(root, text = "Second Relative")
labInput1.grid(row = 2, column = 1, sticky = "NESW")

labInput1 = tk.Label(root, text = "Third Relative")
labInput1.grid(row = 2, column = 2, sticky = "NESW")



var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()
var9 = tk.IntVar()
var10 = tk.IntVar()
var11 = tk.IntVar()
var12 = tk.IntVar()
var13 = tk.IntVar()
var14 = tk.IntVar()
var15 = tk.IntVar()
var16 = tk.IntVar()
#What the named parameter viriable does is binds 



#              FIRST RELATIVE

cHC = tk.Checkbutton(root, text ="Dad", variable=var1)
cHC.grid(row=4, column =0, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Mom", variable=var2)
cHC.grid(row=5, column =0, sticky = "NESW")


#              SECOND RELATIVE




cHC = tk.Checkbutton(root, text ="Dad", variable=var3)
cHC.grid(row=4, column =1, stick = "NESW")

cHC = tk.Checkbutton(root, text ="Mom", variable=var4)
cHC.grid(row=5, column =1, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Sister(Y)", variable=var5)
cHC.grid(row=6, column =1, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Sister(O)", variable=var6)
cHC.grid(row=7, column =1, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Brother(Y)", variable=var7)
cHC.grid(row=8, column =1, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Brother(O)", variable=var8)
cHC.grid(row=9, column =1, sticky = "NESW")



#              THIRD RELATIVE
cHC = tk.Checkbutton(root, text ="Dad", variable=var9)
cHC.grid(row=4, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Mom", variable=var10)
cHC.grid(row=5, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Sister(Y)", variable=var11)
cHC.grid(row=6, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Sister(O)", variable=var12)
cHC.grid(row=7, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Brother(Y)", variable=var13)
cHC.grid(row=8, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Brother(O)", variable=var14)
cHC.grid(row=9, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Son", variable=var15)
cHC.grid(row=10, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="Daughter", variable=var16)
cHC.grid(row=11, column =2, sticky = "NESW")

#WE are writing an EVENT DRIVEN PROGRAM.
#Build the GUI 
#Start it running
#Wait for "EVENT" 

root.mainloop() #Starts the program
