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
output = tk.Text(root,height = 30, width =10) #Parameters are what we send in.

#Ordered parameters: The order we send them matters. (COMMON)

#Named paramters: JavaScpript and Python specific



#Using grid instead of pack 
#To make the columns and rows


#					Titles

labInput1 = tk.Label(root, text = "Relative Calculator", font = ("Helvitica",20))
labInput1.grid(row = 0, column = 1, sticky = "NESW")

labInput1 = tk.Label(root, text = "亲戚的计算器", font = ("Helvitica",16))
labInput1.grid(row = 2, column = 0, sticky = "NESW")

labInput1 = tk.Label(root, text = "两个亲戚", font = ("Helvitica",16))
labInput1.grid(row = 2, column = 1, sticky = "NESW")

labInput1 = tk.Label(root, text = "三个亲戚", font = ("Helvitica",16))
labInput1.grid(row = 2, column = 2, sticky = "NESW")

labInput1 = tk.Label(root, text = "亲戚", font = ("Helvitica",20))
labInput1.grid(row = 14, column = 1, sticky = "NESW")

output = tk.Text(root, width=35, height=3, borderwidth = 3, relief=tk.GROOVE)
output.config(state = 'disabled')
output.grid(row=15, column=1)


#   	Defining Relatives

#  Gives the relative names a variable // Defines it

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


# 					Rectangles







#              FIRST RELATIVE

cHC = tk.Checkbutton(root, text ="爸爸", variable=var1)
cHC.grid(row=4, column =0, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="妈妈", variable=var2)
cHC.grid(row=5, column =0, sticky = "NESW")


#              SECOND RELATIVE




cHC = tk.Checkbutton(root, text ="爸爸", variable=var3, font = ("Helvitica",13))
cHC.grid(row=4, column =1, stick = "NESW")

cHC = tk.Checkbutton(root, text ="妈妈", variable=var4, font = ("Helvitica",13))
cHC.grid(row=5, column =1, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="妹妹", variable=var5, font = ("Helvitica",13))
cHC.grid(row=6, column =1, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="姐姐", variable=var6, font = ("Helvitica",13))
cHC.grid(row=7, column =1, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="弟弟", variable=var7, font = ("Helvitica",13))
cHC.grid(row=8, column =1, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="哥哥", variable=var8, font = ("Helvitica",13))
cHC.grid(row=9, column =1, sticky = "NESW")



#              THIRD RELATIVE
cHC = tk.Checkbutton(root, text ="爸爸", variable=var9, font = ("Helvitica",13))
cHC.grid(row=4, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="妈妈", variable=var10, font = ("Helvitica",13))
cHC.grid(row=5, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="妹妹", variable=var11, font = ("Helvitica",13))
cHC.grid(row=6, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="姐姐", variable=var12, font = ("Helvitica",13))
cHC.grid(row=7, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="弟弟", variable=var13, font = ("Helvitica",13))
cHC.grid(row=8, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="哥哥", variable=var14, font = ("Helvitica",13))
cHC.grid(row=9, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="儿子", variable=var15, font = ("Helvitica",13))
cHC.grid(row=10, column =2, sticky = "NESW")

cHC = tk.Checkbutton(root, text ="女儿", variable=var16, font = ("Helvitica",13))
cHC.grid(row=11, column =2, sticky = "NESW")
 


root.mainloop() #Starts the program
