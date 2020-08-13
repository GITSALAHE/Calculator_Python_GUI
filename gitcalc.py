from tkinter import *

root = Tk()
root.title("GITSALAH Calculator")
root.iconbitmap(r'calc.ico')
root.resizable(0,0)
root.configure(bg="black")
s = Entry(root, width=40, borderwidth=5)
s.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

#function clicker
def button_clicker(number):
    current = s.get() #get the current data in the textbox
    s.delete(0, END) #to not duplicate data in the textbox
    s.insert(0, str(current) + str(number))

#function Clear
def button_del():
    s.delete(0, END)

def button_add():
    firstnumbertext = s.get() #to save the first number in the textbox
    global f_num 
    global math
    math = "addition"
    f_num = int(firstnumbertext) # make sure firstnumbertext is integer 
    s.delete(0, END) #for passing the second number
    
def button_equals():
    second_number = s.get()
    s.delete(0, END)
    #let me put some logique 
    if math == "addition":
        s.insert(0, f_num + int(second_number))
    if math == "subtraction":
        s.insert(0, f_num - int(second_number))
    if math == "mutliplacation":
        s.insert(0, f_num * int(second_number))
    if math == "division":
        s.insert(0, f_num / int(second_number))

def button_sub():
    firstnumbertext = s.get() #to save the first number in the textbox
    global f_num 
    global math
    math = "subtraction"
    f_num = int(firstnumbertext) # make sure firstnumbertext is integer 
    s.delete(0, END) #for passing the second number
    

def button_mult():
    firstnumbertext = s.get() #to save the first number in the textbox
    global f_num 
    global math
    math = "mutliplacation"
    f_num = int(firstnumbertext) # make sure firstnumbertext is integer 
    s.delete(0, END) #for passing the second number
    

def button_div():
    firstnumbertext = s.get() #to save the first number in the textbox
    global f_num 
    global math
    math = "division"
    f_num = int(firstnumbertext) # make sure firstnumbertext is integer 
    s.delete(0, END) #for passing the second number
    

#Define the buttons 
button_1 = Button(root, text="1", background ="black", fg="white", padx=40, pady=20, command=lambda: button_clicker(1))
button_2 = Button(root, text="2", background ="black", fg="white", padx=40, pady=20, command=lambda: button_clicker(2))
button_3 = Button(root, text="3", background ="black", fg="white", padx=40, pady=20, command=lambda: button_clicker(3))
button_4 = Button(root, text="4", background ="black", fg="white", padx=40, pady=20, command=lambda: button_clicker(4))
button_5 = Button(root, text="5", background ="black", fg="white", padx=40, pady=20, command=lambda: button_clicker(5))
button_6 = Button(root, text="6", background ="black", fg="white", padx=40, pady=20, command=lambda: button_clicker(6))
button_7 = Button(root, text="7", background ="black", fg="white", padx=40, pady=20, command=lambda: button_clicker(7))
button_8 = Button(root, text="8", background ="black", fg="white", padx=40, pady=20, command=lambda: button_clicker(8))
button_9 = Button(root, text="9", background ="black", fg="white", padx=40, pady=20, command=lambda: button_clicker(9))
button_0 = Button(root, text="0", background ="black", fg="white", padx=40, pady=20, command=lambda: button_clicker(0))
button_add = Button(root, text="+", background ="orange", fg="white", padx=38, pady=20, command=button_add)
button_sub = Button(root, text="-", background ="orange", fg="white", padx=38, pady=20, command=button_sub)
button_mult = Button(root, text="*", background ="orange", fg="white", padx=38, pady=20, command=button_mult)
button_div = Button(root, text="/", background ="orange", fg="white", padx=42, pady=20, command=button_div)

button_clear = Button(root, text="C", background ="orange", fg="white", padx=38, pady=20, command=button_del)
button_equal = Button(root, text="=", background ="orange", fg="white", padx=38, pady=20, command=button_equals)

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
button_sub.grid(row=3, column=4)
button_mult.grid(row=4, column=4)
button_div.grid(row=4, column=2)
button_clear.grid(row=1, column=4)
button_equal.grid(row=4, column=0)
root.mainloop()
