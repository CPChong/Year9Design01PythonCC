import tkinter as tk
from tkinter import ttk 

#*****************************CHECK FUNCS*************************
def var1eFNC(*args):
	var2e.set(0)
	chineseName[0] = "ba ba"
	displaye("var1e")

def var2eFNC(*args):
	var1e.set(0)
	chineseName[0] = "ma ma"
	displaye("var2e")

def var3eFNC(*args):
	var4e.set(0)
	var5e.set(0)
	var6e.set(0)
	var7e.set(0)
	var8e.set(0)
	chineseName[1] = "ba ba"
	displaye("var3e")

def var4eFNC(*args):
	var3e.set(0)
	var5e.set(0)
	var6e.set(0)
	var7e.set(0)
	var8e.set(0)
	chineseName[1] = "ma ma"
	displaye("var4e")

def var5eFNC(*args):
	var3e.set(0)
	var4e.set(0)
	var6e.set(0)
	var7e.set(0)
	var8e.set(0)
	chineseName[1] = "mei mei"
	displaye("var5e")

def var6eFNC(*args):
	var3e.set(0)
	var4e.set(0)
	var5e.set(0)
	var7e.set(0)
	var8e.set(0)
	chineseName[1] = "jie jie"
	displaye("var6e")

def var7eFNC(*args):
	var3e.set(0)
	var4e.set(0)
	var5e.set(0)
	var6e.set(0)
	var8e.set(0)
	chineseName[1] = "di di"
	displaye("var7e")

def var8eFNC(*args):
	var3e.set(0)
	var4e.set(0)
	var5e.set(0)
	var6e.set(0)
	var7e.set(0)
	chineseName[1] = "ge ge"
	displaye("var8e")

def var9eFNC(*args):
	var10e.set(0)
	var11e.set(0)
	var12e.set(0)
	var13e.set(0)
	var14e.set(0)
	var15e.set(0)
	var16e.set(0)
	chineseName[2] = "ba ba"
	displaye("var9e")

def var10eFNC(*args):
	var9e.set(0)
	var11e.set(0)
	var12e.set(0)
	var13e.set(0)
	var14e.set(0)
	var15e.set(0)
	var16e.set(0)
	chineseName[2] = "ma ma"
	displaye("var10e")

def var11eFNC(*args):
	var9e.set(0)
	var10e.set(0)
	var12e.set(0)
	var13e.set(0)
	var14e.set(0)
	var15e.set(0)
	var16e.set(0)
	chineseName[2] = "mei mei"
	displaye("var11e")

def var12eFNC(*args):
	var9e.set(0)
	var10e.set(0)
	var11e.set(0)
	var13e.set(0)
	var14e.set(0)
	var15e.set(0)
	var16e.set(0)
	chineseName[2] = "jie jie"
	displaye("var12e")

def var13eFNC(*args):
	var9e.set(0)
	var10e.set(0)
	var11e.set(0)
	var12e.set(0)
	var14e.set(0)
	var15e.set(0)
	var16e.set(0)
	chineseName[2] = "di di"
	displaye("var13e")

def var14eFNC(*args):
	var9e.set(0)
	var10e.set(0)
	var11e.set(0)
	var12e.set(0)
	var13e.set(0)
	var15e.set(0)
	var16e.set(0)
	chineseName[2] = "ge ge"
	displaye("var14e")

def var15eFNC(*args):
	var9e.set(0)
	var10e.set(0)
	var11e.set(0)
	var12e.set(0)
	var13e.set(0)
	var14e.set(0)
	var16e.set(0)
	chineseName[2] = "er zi"
	displaye("var15e")

def var16eFNC(*args):
	var9e.set(0)
	var10e.set(0)
	var11e.set(0)
	var12e.set(0)
	var13e.set(0)
	var14e.set(0)
	var15e.set(0)
	chineseName[2] = "nu er"
	displaye("var16e")

def displaye(a):
	print(chineseName[0])
	#Constructo name
	name = ""
	#loop to go through chineseName
	for i in range(0, len(chineseName),1):
		name = name + chineseName[i] + " "

	print(name)
	#Trace:
	# i = 0 | 0 < 3 | T - name = "" + "baba" + " "
	# i = 1 | 1 < 3 | T - name = "baba " + "empty" + " "
	# i = 2 | 2 < 3 | T - name = "baba empty " + "empty" + " "
	# i = 3 | 3 < 3 | F - EXIT LOOP

	outpute.config(state = "normal")
	outpute.delete("1.0",tk.END)
	outpute.insert(tk.END,name)
	outpute.config(state = "disabled")


#*************************************************************************************
#*********************************MANDARIN********************************************
#*************************************************************************************


def var1mFNC(*args):
	var2m.set(0)
	chineseName[0] = "爸爸"
	displaym("var1m")

def var2mFNC(*args):
	var1m.set(0)
	chineseName[0] = "妈妈"
	displaym("var2m")

def var3mFNC(*args):
	var4m.set(0)
	var5m.set(0)
	var6m.set(0)
	var7m.set(0)
	var8m.set(0)
	chineseName[1] = "爸爸"
	displaym("var3m")

def var4mFNC(*args):
	var3m.set(0)
	var5m.set(0)
	var6m.set(0)
	var7m.set(0)
	var8m.set(0)
	chineseName[1] = "妈妈"
	displaym("var4m")

def var5mFNC(*args):
	var3m.set(0)
	var4m.set(0)
	var6m.set(0)
	var7m.set(0)
	var8m.set(0)
	chineseName[1] = "妹妹"
	displaym("var5m")

def var6mFNC(*args):
	var3m.set(0)
	var4m.set(0)
	var5m.set(0)
	var7m.set(0)
	var8m.set(0)
	chineseName[1] = "姐姐"
	displaym("var6m")

def var7mFNC(*args):
	var3m.set(0)
	var4m.set(0)
	var5m.set(0)
	var6m.set(0)
	var8m.set(0)
	chineseName[1] = "弟弟"
	displaym("var7m")

def var8mFNC(*args):
	var3m.set(0)
	var4m.set(0)
	var5m.set(0)
	var6m.set(0)
	var7m.set(0)
	chineseName[1] = "哥哥"
	displaym("var8m")

def var9mFNC(*args):
	var10m.set(0)
	var11m.set(0)
	var12m.set(0)
	var13m.set(0)
	var14m.set(0)
	var15m.set(0)
	var16m.set(0)
	chineseName[2] = "ba ba"
	displaym("var9m")

def var10mFNC(*args):
	var9m.set(0)
	var11m.set(0)
	var12m.set(0)
	var13m.set(0)
	var14m.set(0)
	var15m.set(0)
	var16m.set(0)
	chineseName[2] = "妈妈"
	displaym("var10m")

def var11mFNC(*args):
	var9m.set(0)
	var10m.set(0)
	var12m.set(0)
	var13m.set(0)
	var14m.set(0)
	var15m.set(0)
	var16m.set(0)
	chineseName[2] = "妹妹"
	displaym("var11m")

def var12mFNC(*args):
	var9m.set(0)
	var10m.set(0)
	var11m.set(0)
	var13m.set(0)
	var14m.set(0)
	var15m.set(0)
	var16m.set(0)
	chineseName[2] = "姐姐"
	displaym("var12m")

def var13mFNC(*args):
	var9m.set(0)
	var10m.set(0)
	var11m.set(0)
	var12m.set(0)
	var14m.set(0)
	var15m.set(0)
	var16m.set(0)
	chineseName[2] = "弟弟"
	displaym("var13m")

def var14mFNC(*args):
	var9m.set(0)
	var10m.set(0)
	var11m.set(0)
	var12m.set(0)
	var13m.set(0)
	var15m.set(0)
	var16m.set(0)
	chineseName[2] = "哥哥"
	displaym("var14m")

def var15mFNC(*args):
	var9m.set(0)
	var10m.set(0)
	var11m.set(0)
	var12m.set(0)
	var13m.set(0)
	var14m.set(0)
	var16m.set(0)
	chineseName[2] = "儿子"
	display("var15m")

def var16mFNC(*args):
	var9m.set(0)
	var10m.set(0)
	var11m.set(0)
	var12m.set(0)
	var13m.set(0)
	var14m.set(0)
	var15m.set(0)
	chineseName[2] = "女儿"
	displaym("var16m")

#*****************************************************************************

def displaym(a):
	print(chineseName[0])
	#Constructo name
	name = ""
	#loop to go through chineseName
	for i in range(0, len(chineseName),1):
		name = name + chineseName[i] + " "

	print(name)
	#Trace:
	# i = 0 | 0 < 3 | T - name = "" + "baba" + " "
	# i = 1 | 1 < 3 | T - name = "baba " + "empty" + " "
	# i = 2 | 2 < 3 | T - name = "baba empty " + "empty" + " "
	# i = 3 | 3 < 3 | F - EXIT LOOP

	outputm.config(state = "normal")
	outputm.delete("1.0",tk.END)
	outputm.insert(tk.END,name)
	outputm.config(state = "disabled")






#******************************************************************
#******************************************************************
#******************************************************************

#index0 - first relative
#index1 - second relative
#index2 - third relative
#add the three together I get name


chineseName = ["First Relative","Second Relative","Third Relative"]

root = tk.Tk()
root.title("Relative Calculator")

tabControl = ttk.Notebook(root)

#**************************************************************************************
#**************************************************************************************
#**************************************************************************************

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
#What the named parameter variable does is binds 

#              FIRST RELATIVE
 
cHCe = tk.Checkbutton(tab1, text ="Dad", variable=var1e)
cHCe.grid(row=4, column =0, sticky = "NESW")

var2e.trace("w",var2eFNC)
cHCe = tk.Checkbutton(tab1, text ="Mom", variable=var2e)
cHCe.grid(row=5, column =0, sticky = "NESW")


#              SECOND RELATIVE

var3e.trace("w",var3eFNC)
cHCe = tk.Checkbutton(tab1, text ="Dad", variable=var3e, font = ("Helvitica",13))
cHCe.grid(row=4, column =1, stick = "NESW")

var4e.trace("w",var4eFNC)
cHCe = tk.Checkbutton(tab1, text ="Mom", variable=var4e, font = ("Helvitica",13))
cHCe.grid(row=5, column =1, sticky = "NESW")

var5e.trace("w",var5eFNC)
cHCe = tk.Checkbutton(tab1, text ="Sister(Y)", variable=var5e, font = ("Helvitica",13))
cHCe.grid(row=6, column =1, sticky = "NESW")

var6e.trace("w",var6eFNC)
cHCe = tk.Checkbutton(tab1, text ="Sister(O)", variable=var6e, font = ("Helvitica",13))
cHCe.grid(row=7, column =1, sticky = "NESW")

var7e.trace("w",var7eFNC)
cHCe = tk.Checkbutton(tab1, text ="Brother(Y)", variable=var7e, font = ("Helvitica",13))
cHCe.grid(row=8, column =1, sticky = "NESW")

var8e.trace("w",var8eFNC)
cHCe = tk.Checkbutton(tab1, text ="Brother(O)", variable=var8e, font = ("Helvitica",13))
cHCe.grid(row=9, column =1, sticky = "NESW")



#              THIRD RELATIVE

var9e.trace("w",var9eFNC)
cHCe = tk.Checkbutton(tab1, text ="Dad", variable=var9e, font = ("Helvitica",13))
cHCe.grid(row=4, column =2, sticky = "NESW")

var10e.trace("w",var10eFNC)
cHCe = tk.Checkbutton(tab1, text ="Mom", variable=var10e, font = ("Helvitica",13))
cHCe.grid(row=5, column =2, sticky = "NESW")

var11e.trace("w",var11eFNC)
cHCe = tk.Checkbutton(tab1, text ="Sister(Y)", variable=var11e, font = ("Helvitica",13))
cHCe.grid(row=6, column =2, sticky = "NESW")

var12e.trace("w",var12eFNC)
cHCe = tk.Checkbutton(tab1, text ="Sister(O)", variable=var12e, font = ("Helvitica",13))
cHCe.grid(row=7, column =2, sticky = "NESW")

var13e.trace("w",var13eFNC)
cHCe = tk.Checkbutton(tab1, text ="Brother(Y)", variable=var13e, font = ("Helvitica",13))
cHCe.grid(row=8, column =2, sticky = "NESW")

var14e.trace("w",var14eFNC)
cHCe = tk.Checkbutton(tab1, text ="Brother(O)", variable=var14e, font = ("Helvitica",13))
cHCe.grid(row=9, column =2, sticky = "NESW")

var15e.trace("w",var15eFNC)
cHCe = tk.Checkbutton(tab1, text ="Son", variable=var15e, font = ("Helvitica",13))
cHCe.grid(row=10, column =2, sticky = "NESW")

var16e.trace("w",var16eFNC)
cHCe = tk.Checkbutton(tab1, text ="Daughter", variable=var16e, font = ("Helvitica",13))
cHCe.grid(row=11, column =2, sticky = "NESW")




#*********************************************************************************
#*********************************************************************************
#*********************************************************************************

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Mandarin Version")

#*********Tab 2

# Three stages t build elements/ objects
#1) CONSTRUCT the Object: We build and configure it.
#2) CONSTRUCT the Object: We specify behaviours and settings (OPTIONAL)
#3) Pack the Object: Put it in the window.

#					Titles

labelm = tk.Label(tab2, text = "亲戚的计算器", font = ("Helvitica",20))
labelm.grid(row = 0, column = 1, sticky = "NESW")

labelm = tk.Label(tab2, text = "第一个亲戚", font = ("Helvitica",16))
labelm.grid(row = 2, column = 0, sticky = "NESW")

labelm = tk.Label(tab2, text = "第两个亲戚", font = ("Helvitica",16))
labelm.grid(row = 2, column = 1, sticky = "NESW")

labelm = tk.Label(tab2, text = "第三个亲戚", font = ("Helvitica",16))
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



#*******************************************************************************
#*****************************MANDARIN******************************************
#*******************************************************************************


#              FIRST RELATIVE
var1m.trace("w",var1mFNC)
cHCm = tk.Checkbutton(tab2, text ="爸爸", variable=var1m)
cHCm.grid(row=4, column =0, sticky = "NESW")

var2m.trace("w",var2mFNC)
cHCm = tk.Checkbutton(tab2, text ="妈妈", variable=var2m)
cHCm.grid(row=5, column =0, sticky = "NESW")


#              SECOND RELATIVE
var3m.trace("w",var3mFNC)
cHCm = tk.Checkbutton(tab2, text ="爸爸", variable=var3m, font = ("Helvitica",13))
cHCm.grid(row=4, column =1, stick = "NESW")

var4m.trace("w",var4mFNC)
cHCm = tk.Checkbutton(tab2, text ="妈妈", variable=var4m, font = ("Helvitica",13))
cHCm.grid(row=5, column =1, sticky = "NESW")

var5m.trace("w",var5mFNC)
cHCm = tk.Checkbutton(tab2, text ="妹妹", variable=var5m, font = ("Helvitica",13))
cHCm.grid(row=6, column =1, sticky = "NESW")

var6m.trace("w",var6mFNC)
cHCm = tk.Checkbutton(tab2, text ="姐姐", variable=var6m, font = ("Helvitica",13))
cHCm.grid(row=7, column =1, sticky = "NESW")

var7m.trace("w",var7mFNC)
cHCm = tk.Checkbutton(tab2, text ="弟弟", variable=var7m, font = ("Helvitica",13))
cHCm.grid(row=8, column =1, sticky = "NESW")

var8m.trace("w",var8mFNC)
cHCm = tk.Checkbutton(tab2, text ="哥哥", variable=var8m, font = ("Helvitica",13))
cHCm.grid(row=9, column =1, sticky = "NESW")



#              THIRD RELATIVE
var9m.trace("w",var9mFNC)
cHCm = tk.Checkbutton(tab2, text ="爸爸", variable=var9m, font = ("Helvitica",13))
cHCm.grid(row=4, column =2, sticky = "NESW")

var10m.trace("w",var10mFNC)
cHCm = tk.Checkbutton(tab2, text ="妈妈", variable=var10m, font = ("Helvitica",13))
cHCm.grid(row=5, column =2, sticky = "NESW")

var11m.trace("w",var11mFNC)
cHCm = tk.Checkbutton(tab2, text ="妹妹", variable=var11m, font = ("Helvitica",13))
cHCm.grid(row=6, column =2, sticky = "NESW")

var12m.trace("w",var12mFNC)
cHCm = tk.Checkbutton(tab2, text ="姐姐", variable=var12m, font = ("Helvitica",13))
cHCm.grid(row=7, column =2, sticky = "NESW")

var13m.trace("w",var13mFNC)
cHCm = tk.Checkbutton(tab2, text ="弟弟", variable=var13m, font = ("Helvitica",13))
cHCm.grid(row=8, column =2, sticky = "NESW")

var14m.trace("w",var14mFNC)
cHCm = tk.Checkbutton(tab2, text ="哥哥", variable=var14m, font = ("Helvitica",13))
cHCm.grid(row=9, column =2, sticky = "NESW")

var15m.trace("w",var15mFNC)
cHCm = tk.Checkbutton(tab2, text ="儿子", variable=var15m, font = ("Helvitica",13))
cHCm.grid(row=10, column =2, sticky = "NESW")

var16m.trace("w",var16mFNC)
cHCm = tk.Checkbutton(tab2, text ="女儿", variable=var16m, font = ("Helvitica",13))
cHCm.grid(row=11, column =2, sticky = "NESW")
 


tabControl.pack()
root.mainloop()