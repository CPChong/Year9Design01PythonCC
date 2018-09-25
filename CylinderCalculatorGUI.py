import tkinter as tk 
import math

#Function
def submit():

	print("Submit pressed")
	r = float(entr.get())
	h = float(entr.get())

	v = math.pi*r*r*h
	v = round (v,3)

	output.config(state="normal")
	output.insert(tk.INSERT,v)
	output.config(state="disabled")


	output.insert(tk.INSERT,v)


#Python programs find the first non indented code
#to start.  and def is ignored until you call it

root = tk.Tk()
root.title("Volume of a Cyliner")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

root.mainloop()