from tkinter import *

# 1. Math functions
def addition():
    try:
        ans = float(num1.get()) + float(num2.get())
        result.config(text=f"Result: {ans}")
    except ValueError:
        result.config(text="Error: Enter valid numbers")

def subtraction():
    try:
        ans = float(num1.get()) - float(num2.get())
        result.config(text=f"Result: {ans}")
    except ValueError:
        result.config(text="Error: Enter valid numbers")

def division():
    try:
        ans = float(num1.get()) / float(num2.get())
        result.config(text=f"Result: {ans}")
    except ZeroDivisionError:
        result.config(text="Error: Cannot divide by 0")
    except ValueError:
        result.config(text="Error: Enter valid numbers")

def multiplication():
    try:
        ans = float(num1.get()) * float(num2.get())
        result.config(text=f"Result: {ans}")
    except ValueError:
        result.config(text="Error: Enter valid numbers")

def exponent():
    try:
        ans = float(num1.get()) ** float(num2.get())
        result.config(text=f"Result: {ans}")
    except ValueError:
        result.config(text="Error: Enter valid numbers")

# 2. Window setup
root = Tk()
root.title("Simple Calculator")
root.geometry("500x500")
root.maxsize(600, 600)
root.minsize(300, 300)

# 3. Title banner
f1 = Frame(root, bg="black", bd=10)
f1.pack(pady=20, fill=X)
title = Label(f1, text="CALCULATOR", font=("Times New Roman", 19), fg="white", bg="black")
title.pack()

# 4. Inputs
num1 = StringVar()
ne1 = Entry(root, textvariable=num1, font=("Arial", 12))
ne1.pack(pady=5)

num2 = StringVar()
ne2 = Entry(root, textvariable=num2, font=("Arial", 12))
ne2.pack(pady=5)

# 5. Buttons
btn_frame = Frame(root)
btn_frame.pack(pady=20)

b1 = Button(btn_frame, text="+", font=("Arial", 14), width=4, command=addition)
b1.pack(side=LEFT, padx=5)

b2 = Button(btn_frame, text="-", font=("Arial", 14), width=4, command=subtraction)
b2.pack(side=LEFT, padx=5)

b3 = Button(btn_frame, text="*", font=("Arial", 14), width=4, command=multiplication)
b3.pack(side=LEFT, padx=5)

b4 = Button(btn_frame, text="/", font=("Arial", 14), width=4, command=division)
b4.pack(side=LEFT, padx=5)

b5 = Button(btn_frame, text="^n", font=("Arial", 14), width=4, command=exponent)
b5.pack(side=LEFT, padx=5)

# 6. Output display
result = Label(root, text="Result: ", font=("Arial", 16, "bold"), fg="blue")
result.pack(pady=20)

root.mainloop()
