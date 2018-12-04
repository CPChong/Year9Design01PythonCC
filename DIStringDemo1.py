import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title("Relative Calculator")


tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="English Version")


#					Titles

labele = tk.Label(tab1, text = "Relative Calculator", font = ("Helvitica",20))
labele.grid(row = 0, column = 1, sticky = "NESW")

labele = tk.Label(tab1, text = "First Relative", font = ("Helvitica",16))
labele.grid(row = 2, column = 0, sticky = "NESW")

labele = tk.Label(tab1, text = "Second Relative", font = ("Helvitica",16))
labele.grid(row = 2, column = 1, sticky = "NESW")

labele = tk.Label(tab1, text = "Third Relative", font = ("Helvitica",16))
labele.grid(row = 2, column = 2, sticky = "NESW")

labele = tk.Label(tab1, text = "Relative", font = ("Helvitica",20))
labele.grid(row = 14, column = 1, sticky = "NESW")

labele = tk.Label(tab1, text = "Y = Younger", font = ("Helvitica",14))
labele.grid(row = 2, column = 3)

labele = tk.Label(tab1, text = "O = Older", font = ("Helvitica",14))
labele.grid(row = 3, column = 3)

outpute = tk.Text(tab1, width=35, height=3, borderwidth = 3, relief=tk.GROOVE)
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

cHCe = tk.Checkbutton(tab1, text ="Dad", variable=var1e)
cHCe.grid(row=4, column =0, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Mom", variable=var2e)
cHCe.grid(row=5, column =0, sticky = "NESW")


#              SECOND RELATIVE




cHCe = tk.Checkbutton(tab1, text ="Dad", variable=var3e, font = ("Helvitica",13))
cHCe.grid(row=4, column =1, stick = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Mom", variable=var4e, font = ("Helvitica",13))
cHCe.grid(row=5, column =1, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Sister(Y)", variable=var5e, font = ("Helvitica",13))
cHCe.grid(row=6, column =1, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Sister(O)", variable=var6e, font = ("Helvitica",13))
cHCe.grid(row=7, column =1, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Brother(Y)", variable=var7e, font = ("Helvitica",13))
cHCe.grid(row=8, column =1, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Brother(O)", variable=var8e, font = ("Helvitica",13))
cHCe.grid(row=9, column =1, sticky = "NESW")



#              THIRD RELATIVE
cHCe = tk.Checkbutton(tab1, text ="Dad", variable=var9e, font = ("Helvitica",13))
cHCe.grid(row=4, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Mom", variable=var10e, font = ("Helvitica",13))
cHCe.grid(row=5, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Sister(Y)", variable=var11e, font = ("Helvitica",13))
cHCe.grid(row=6, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Sister(O)", variable=var12e, font = ("Helvitica",13))
cHCe.grid(row=7, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Brother(Y)", variable=var13e, font = ("Helvitica",13))
cHCe.grid(row=8, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Brother(O)", variable=var14e, font = ("Helvitica",13))
cHCe.grid(row=9, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Son", variable=var15e, font = ("Helvitica",13))
cHCe.grid(row=10, column =2, sticky = "NESW")

cHCe = tk.Checkbutton(tab1, text ="Daughter", variable=var16e, font = ("Helvitica",13))
cHCe.grid(row=11, column =2, sticky = "NESW")
 

tabControl.add(tab1, text="English Version")




























#********************************
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Mandarin Version")



#*********Tab 2


# Three stages t build elements/ objects
#1) CONSTRUCT the Object: We build and configure it.
#2) CONSTRUCT the Object: We specify behaviours and settings (OPTIONAL)
#3) Pack the Object: Put it in the window.
output = tk.Text(tab2,height = 30, width =10) #Parameters are what we send in.

#					Titles

labelm = tk.Label(tab2, text = "亲戚的计算器", font = ("Helvitica",20))
labelm.grid(row = 0, column = 1, sticky = "NESW")

labelm = tk.Label(tab2, text = "一个亲戚", font = ("Helvitica",16))
labelm.grid(row = 2, column = 0, sticky = "NESW")

labelm = tk.Label(tab2, text = "两个亲戚", font = ("Helvitica",16))
labelm.grid(row = 2, column = 1, sticky = "NESW")

labelm = tk.Label(tab2, text = "三个亲戚", font = ("Helvitica",16))
labelm.grid(row = 2, column = 2, sticky = "NESW")

labelm = tk.Label(tab2, text = "亲戚", font = ("Helvitica",20))
labelm.grid(row = 14, column = 1, sticky = "NESW")

outputm = tk.Text(tab2, width=35, height=3, borderwidth = 3, relief=tk.GROOVE)
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




#              FIRST RELATIVE

cHCm = tk.Checkbutton(tab2, text ="爸爸", variable=var1m)
cHCm.grid(row=4, column =0, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="妈妈", variable=var2m)
cHCm.grid(row=5, column =0, sticky = "NESW")


#              SECOND RELATIVE

cHCm = tk.Checkbutton(tab2, text ="爸爸", variable=var3m, font = ("Helvitica",13))
cHCm.grid(row=4, column =1, stick = "NESW")

cHCm = tk.Checkbutton(tab2, text ="妈妈", variable=var4m, font = ("Helvitica",13))
cHCm.grid(row=5, column =1, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="妹妹", variable=var5m, font = ("Helvitica",13))
cHCm.grid(row=6, column =1, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="姐姐", variable=var6m, font = ("Helvitica",13))
cHCm.grid(row=7, column =1, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="弟弟", variable=var7m, font = ("Helvitica",13))
cHCm.grid(row=8, column =1, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="哥哥", variable=var8m, font = ("Helvitica",13))
cHCm.grid(row=9, column =1, sticky = "NESW")



#              THIRD RELATIVE
cHCm = tk.Checkbutton(tab2, text ="爸爸", variable=var9m, font = ("Helvitica",13))
cHCm.grid(row=4, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="妈妈", variable=var10m, font = ("Helvitica",13))
cHCm.grid(row=5, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="妹妹", variable=var11m, font = ("Helvitica",13))
cHCm.grid(row=6, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="姐姐", variable=var12m, font = ("Helvitica",13))
cHCm.grid(row=7, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="弟弟", variable=var13m, font = ("Helvitica",13))
cHCm.grid(row=8, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="哥哥", variable=var14m, font = ("Helvitica",13))
cHCm.grid(row=9, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="儿子", variable=var15m, font = ("Helvitica",13))
cHCm.grid(row=10, column =2, sticky = "NESW")

cHCm = tk.Checkbutton(tab2, text ="女儿", variable=var16m, font = ("Helvitica",13))
cHCm.grid(row=11, column =2, sticky = "NESW")
 


tabControl.add(tab2, text="Mandarin Version")

tab1.mainloop()
tab2.mainloop()