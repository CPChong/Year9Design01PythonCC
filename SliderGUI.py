import tninter as tk

root = tk.Tk()
root.title ("SliderGUI")

slide1 = tk.Scale(root, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL)



root.mainloop()