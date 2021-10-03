from tkinter import *
from datetime import datetime


def get_month_number(month_name):
    try:
        month_no = datetime.strptime(month_name, "%B").month
    except:
        month_no = -1

    return month_no

def calculate():
    name = txt_name.get()
    birth_month = get_month_number(txt_month.get())
    birth_year = txt_year.get()

    if birth_month == -1:
        lbl_display = Label(window, text="Invalid Month, Please type it correctly.", font=("Arial", 14), bg="steelBlue1", fg="red")
        lbl_display.pack(pady=(0, 10))

    elif not birth_year.isdigit():
        lbl_display = Label(window, text="Invalid year, Please type it correctly.", font=("Arial", 14), bg="steelBlue1", fg="red")
        lbl_display.pack(pady=(0, 10))

    else:
        birth_year = int(birth_year)
        current_year = datetime.today().year
        current_month = datetime.today().month
        current_day = datetime.today().day
        age = current_year - birth_year

        if current_month < birth_month:
            age -= 1
        elif current_month == birth_month:
            if current_day < birth_day:
                age -= 1

        message = "Hello " + name + ", you are " + str(age) + " years old."
        lbl_display = Label(window, text=message, font=("Arial", 14), bg="steelBlue1")
        lbl_display.pack(pady=(0, 10))


window = Tk()
window.title("Age Calculator")
window.geometry("500x450")
window.config(background='steelBlue1')
window.iconbitmap("age-group.ico")

lbl_title = Label(window, text="Age Calculator", font=("Frosty's Winterland", 45, "bold"),bg="steelBlue1", fg="Purple")
lbl_title.pack(pady=(30, 20))

lbl_name = Label(window, text="What is your name ?", font=("Arial", 14), bg="steelBlue1")
lbl_name.pack(pady=(0, 5))

txt_name = Entry(window, font=("Arial", 14))
txt_name.pack(pady=(0, 10))

lbl_month = Label(window, text="Type your birth month ?", font=("Arial",14), bg="steelBlue1")
lbl_month.pack(pady=(0, 5))

txt_month = Entry(window, font=("Arial", 14))
txt_month.pack(pady=(0, 10))

lbl_year = Label(window, text="Type your birth year ?", font=("Arial", 14), bg="steelBlue1")
lbl_year.pack(pady=(0, 10))

txt_year = Entry(window, font=("Arial", 14))
txt_year.pack(pady=(0, 10))

btn_calculate = Button(window, text="Calculate the age", font=("Arial", 14, "bold"), bg="orange", fg="white", command=calculate)
btn_calculate.pack(pady=(0, 10))



window.mainloop()