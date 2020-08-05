from tkinter import *

root = Tk()
root.title("GITSALAH Calculator")
root.iconbitmap(r'calc.ico')
root.resizable(0,0)
root.configure(bg="black")
s = Entry(root, width=40, borderwidth=5)
s.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

#function calc ADD
def buttonAdd():
    return

#Define the buttons 
button_1 = Button(root, text="1", background ="black", fg="white", padx=40, pady=20, command=buttonAdd)
button_2 = Button(root, text="2", background ="black", fg="white", padx=40, pady=20, command=buttonAdd)
button_3 = Button(root, text="3", background ="black", fg="white", padx=40, pady=20, command=buttonAdd)
button_4 = Button(root, text="4", background ="black", fg="white", padx=40, pady=20, command=buttonAdd)
button_5 = Button(root, text="5", background ="black", fg="white", padx=40, pady=20, command=buttonAdd)
button_6 = Button(root, text="6", background ="black", fg="white", padx=40, pady=20, command=buttonAdd)
button_7 = Button(root, text="7", background ="black", fg="white", padx=40, pady=20, command=buttonAdd)
button_8 = Button(root, text="8", background ="black", fg="white", padx=40, pady=20, command=buttonAdd)
button_9 = Button(root, text="9", background ="black", fg="white", padx=40, pady=20, command=buttonAdd)
button_0 = Button(root, text="0", background ="black", fg="white", padx=40, pady=20, command=buttonAdd)
button_add = Button(root, text="+", background ="orange", fg="white", padx=38, pady=20, command=buttonAdd)
button_clear = Button(root, text="C", background ="orange", fg="white", padx=38, pady=20, command=buttonAdd)
button_equal = Button(root, text="=", background ="orange", fg="white", padx=38, pady=20, command=buttonAdd)

#UI buttons 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_add.grid(row=2, column=4)
button_clear.grid(row=1, column=4)
button_equal.grid(row=3, column=4)
root.mainloop()
