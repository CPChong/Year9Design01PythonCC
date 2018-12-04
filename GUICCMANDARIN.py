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

labelm = tk.Label(root, text = "亲戚的计算器", font = ("Helvitica",20))
labelm.grid(row = 0, column = 1, sticky = "NESW")

labelm = tk.Label(root, text = "一个亲戚", font = ("Helvitica",16))
labelm.grid(row = 2, column = 0, sticky = "NESW")

labelm = tk.Label(root, text = "两个亲戚", font = ("Helvitica",16))
labelm.grid(row = 2, column = 1, sticky = "NESW")

labelm = tk.Label(root, text = "三个亲戚", font = ("Helvitica",16))
labelm.grid(row = 2, column = 2, sticky = "NESW")

labelm = tk.Label(root, text = "亲戚", font = ("Helvitica",20))
labelm.grid(row = 14, column = 1, sticky = "NESW")

outputm = tk.Text(root, width=35, height=3, borderwidth = 3, relief=tk.GROOVE)
outputm.config(state = 'disabled')
outputm.grid(row=15, column=1)


#   	Defining Relatives

#  Gives the relative names a variable // Defines it

var1m = tk.IntVar()
var2m = tk.IntVar()
var3m = tk.IntVar()
var4m = tk.IntVar()
var5m = tk.IntVar()
var6m = tk.IntVar()
var7m = tk.IntVar()
var8m = tk.IntVar()
var9m = tk.IntVar()
var10m = tk.IntVar()
var11m = tk.IntVar()
var12m = tk.IntVar()
var13m = tk.IntVar()
var14m = tk.IntVar()
var15m = tk.IntVar()
var16m = tk.IntVar()
#What the named parameter viriable does is binds 


# 					Rectangles







#              FIRST RELATIVE

cHCm = tk.Checkbutton(root, text ="爸爸", variable=var1m)
cHCm.grid(row=4, column =0, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="妈妈", variable=var2m)
cHCm.grid(row=5, column =0, sticky = "NESW")


#              SECOND RELATIVE

cHCm = tk.Checkbutton(root, text ="爸爸", variable=var3m, font = ("Helvitica",13))
cHCm.grid(row=4, column =1, stick = "NESW")

cHCm = tk.Checkbutton(root, text ="妈妈", variable=var4m, font = ("Helvitica",13))
cHCm.grid(row=5, column =1, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="妹妹", variable=var5m, font = ("Helvitica",13))
cHCm.grid(row=6, column =1, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="姐姐", variable=var6m, font = ("Helvitica",13))
cHCm.grid(row=7, column =1, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="弟弟", variable=var7m, font = ("Helvitica",13))
cHCm.grid(row=8, column =1, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="哥哥", variable=var8m, font = ("Helvitica",13))
cHCm.grid(row=9, column =1, sticky = "NESW")



#              THIRD RELATIVE
cHCm = tk.Checkbutton(root, text ="爸爸", variable=var9m, font = ("Helvitica",13))
cHCm.grid(row=4, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="妈妈", variable=var10m, font = ("Helvitica",13))
cHCm.grid(row=5, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="妹妹", variable=var11m, font = ("Helvitica",13))
cHCm.grid(row=6, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="姐姐", variable=var12m, font = ("Helvitica",13))
cHCm.grid(row=7, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="弟弟", variable=var13m, font = ("Helvitica",13))
cHCm.grid(row=8, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="哥哥", variable=var14m, font = ("Helvitica",13))
cHCm.grid(row=9, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="儿子", variable=var15m, font = ("Helvitica",13))
cHCm.grid(row=10, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(root, text ="女儿", variable=var16m, font = ("Helvitica",13))
cHCm.grid(row=11, column =2, sticky = "NESW")
 


root.mainloop() #Starts the program
