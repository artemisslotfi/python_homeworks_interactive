from tkinter import *
import re
from tkinter.messagebox import *

Product_list = []

def name_validator(name):
    if re.match(r"^[a-zA-Z\d\s]{3,30}$",name):
        return True
    else:
        return False

def save_click():
    if name_validator(name.get()) and 1<=quantity.get()<=10 and 0<price.get()<=1000:
        Product = {"name":name.get(), "quantity": quantity.get(), "price":price.get()}
        Product_list.append(Product)
        print(Product_list)
        name.set("")
        quantity.set(0)
        price.set(0)
        showinfo("Save", "Product Saved")
        result=Product["quantity"]*Product["price"]
        total.set(f"Total = {result}")
    else:
        showerror("Error", "Please enter a valid name/Quantity/Price")

window = Tk()

window.title("Product")
window.geometry("400x250")



Label(window, text="Name").place(x=20, y=20)
name = StringVar()
Entry(window,textvariable=name).place(x=80, y=20)



Label(window, text="Quantity").place(x=20, y=60)
quantity = IntVar()
Entry(window,textvariable=quantity).place(x=80, y=60)


Label(window, text="Price").place(x=20, y=100)
price = IntVar()
Entry(window,textvariable=price).place(x=80, y=100)


total = StringVar(value="Total = 0")
Label(window,textvariable=total, font=("Arial", 18)).place(x=220, y=70)


Button(window,text="Save",width=10,command=save_click,bg="lightblue",font=("Arial", 12)).place(x=80, y=150)

window.mainloop()