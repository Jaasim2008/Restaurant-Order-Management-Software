from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from database import *

w = Tk()
w.title('R-JPOS')
w.config(bg='#4E4E4E')
w.geometry('1000x500')
icon = PhotoImage(file='assets/cashier.png')
w.iconphoto(False, icon)


def start_page():
    global icon
    root = Toplevel(w)
    root.title('Order Page')
    root.geometry('1100x650')
    root.config(bg='#4E4E4E')
    root.iconphoto(False, icon)
    Category_lf = LabelFrame(root, text='Food Category:', relief=GROOVE, bg='#4E4E4E', width=550, height=650
                             , font=('Segoe UI Light Italic', 20), fg='#8CFF1A')
    Category_lf.pack(side=TOP, padx=10)

    def breakfast_page():
        root02 = Toplevel(root)
        root02.title('Breakfast Order Page')
        root02.geometry('1100x550')
        root02.config(bg='#4E4E4E')
        root02.iconphoto(False, icon)

        breakfast_products01 = breakfast_foods[0] + " : " + str(breakfast_prices[0])

        exit_btn_ph = PhotoImage(file='assets/Exit_Button.png')

        exit_btn = Button(root02, text='<- EXIT', relief=SUNKEN, bd=0, fg='red', bg='#4E4E4E').grid(row=1, column=0)

        food01 = Button(root02, text=breakfast_products01, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                        fg='#FFA500', activebackground='#4E4E4E', background='#4E4E4E').grid(row=2, column=0, pady=10,
                                                                                             padx=10)

    breakfast_btn = Button(Category_lf, text='Breakfast', bg='#4E4E4E', relief=SUNKEN, bd=0, fg='#007FFF',
                           font=('Segoe UI Light Italic', 35), activebackground='#4E4E4E',
                           activeforeground='red', command=breakfast_page).pack(side=TOP, pady=10)
    lunch_btn = Button(Category_lf, text='Lunch', bg='#4E4E4E', relief=SUNKEN, bd=0, fg='#007FFF',
                       font=('Segoe UI Light Italic', 35), activebackground='#4E4E4E',
                       activeforeground='red').pack(side=TOP, pady=10)
    dinner_btn = Button(Category_lf, text='Dinner', bg='#4E4E4E', relief=SUNKEN, bd=0, fg='#007FFF',
                        font=('Segoe UI Light Italic', 35), activebackground='#4E4E4E',
                        activeforeground='red').pack(side=TOP, pady=10)
    dessert_btn = Button(Category_lf, text='Desserts', bg='#4E4E4E', relief=SUNKEN, bd=0, fg='#007FFF',
                         font=('Segoe UI Light Italic', 35), activebackground='#4E4E4E',
                         activeforeground='red').pack(side=TOP, pady=10)


start_btn = Button(w, text='Start', fg="#FFA500", font=('Segoe UI Light Italic', 20), bg='#4E4E4E', relief=SUNKEN,
                   borderwidth=0, activeforeground='white', activebackground='#FFA500',
                   command=start_page).pack(side=TOP, pady=20)


def error01():
    messagebox.showerror('Err!', 'This Button is Still Under Development')


add_item_btn = Button(w, text='Add New Item to Database', fg="#00FF00", font=('Segoe UI Light Italic', 20),
                      bg='#4E4E4E', relief=SUNKEN,
                      borderwidth=0, activeforeground='white', activebackground='#00FF00',
                      command=error01).pack(side=TOP, pady=20)

w.mainloop()
