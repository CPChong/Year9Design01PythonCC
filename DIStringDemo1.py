import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title("GUI Tabs")

tabControl = ttk.Notebook(root)

output = tk.Text(root,height = 30, width =10)

tab1 = ttk.Frame (tabControl)
tabControl.add(tab1, text="Tab1")
tabControl.pack(expand=1, fill="both")

labInput1 = tk.Label(root, text = "Relative Calculator", font = ("Helvitica",20))
labInput1.grid(row = 0, column = 1, sticky = "NESW")

labInput1 = tk.Label(root, text = "First Relative", font = ("Helvitica",16))
labInput1.grid(row = 2, column = 0, sticky = "NESW")

labInput1 = tk.Label(root, text = "Second Relative", font = ("Helvitica",16))
labInput1.grid(row = 2, column = 1, sticky = "NESW")

labInput1 = tk.Label(root, text = "Third Relative", font = ("Helvitica",16))
labInput1.grid(row = 2, column = 2, sticky = "NESW")

labInput1 = tk.Label(root, text = "Relative", font = ("Helvitica",20))
labInput1.grid(row = 14, column = 1, sticky = "NESW")

labInput1 = tk.Label(root, text = "Y = Younger", font = ("Helvitica",14))
labInput1.grid(row = 2, column = 3)

labInput1 = tk.Label(root, text = "O = Older", font = ("Helvitica",14))
labInput1.grid(row = 3, column = 3)

output = tk.Text(root, width=35, height=3, borderwidth = 3, relief=tk.GROOVE)
output.config(state = 'disabled')



tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")
tabControl.pack(expand=1, fill="both")


root.mainloop()