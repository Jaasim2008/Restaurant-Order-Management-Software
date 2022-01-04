from tkinter import *
from tkinter import messagebox
from database import *

w = Tk()
w.title('R-JPOS')
w.config(bg='#4E4E4E')
w.attributes('-fullscreen', True)
icon = PhotoImage(file='assets/cashier.png')
w.iconphoto(False, icon)


def start_page():
    global icon
    root = Toplevel(w)
    root.title('Order Page')
    root.attributes('-fullscreen', True)
    root.config(bg='#4E4E4E')
    root.iconphoto(False, icon)
    Category_lf = LabelFrame(root, text='Food Category:', relief=GROOVE, bg='#4E4E4E', width=550, height=650
                             , font=('Segoe UI Light Italic', 20), fg='#8CFF1A')
    Category_lf.pack(side=TOP, padx=10)

    def breakfast_page():
        root02 = Toplevel(root)
        root02.title('Breakfast Order Page')
        root02.attributes('-fullscreen', True)
        root02.config(bg='#4E4E4E')
        root02.iconphoto(False, icon)

        breakfast_products01 = breakfast_foods[0] + " : " + str(breakfast_prices[0])
        breakfast_products02 = breakfast_foods[1] + ' : ' + str(breakfast_prices[1])
        breakfast_products03 = breakfast_foods[2] + ' : ' + str(breakfast_prices[2])
        breakfast_products04 = breakfast_foods[3] + ' : ' + str(breakfast_prices[3])
        breakfast_products05 = breakfast_foods[4] + ' : ' + str(breakfast_prices[4])
        breakfast_products06 = breakfast_foods[5] + ' : ' + str(breakfast_prices[5])
        breakfast_products07 = breakfast_foods[6] + ' : ' + str(breakfast_prices[6])
        breakfast_products08 = breakfast_foods[7] + ' : ' + str(breakfast_prices[7])
        breakfast_products09 = breakfast_foods[8] + ' : ' + str(breakfast_prices[8])

        def destroy_window():
            root02.destroy()

        exit_btn = Button(root02, text='<- EXIT', relief=SUNKEN, bd=0, fg='red', bg='#4E4E4E',
                          font=('Segoe UI Light Italic', 15), command=destroy_window).grid(row=1, column=0)

        current_status = ''
        full_status = 'Status : ' + str(current_status)

        def add_eggs():
            current_status01 = 'Added Eggs!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg='#4E4E4E',
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)

        def add_bread():
            current_status01 = 'Added Bread!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg='#4E4E4E',
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)

        def add_parota():
            current_status01 = 'Added Parota!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg='#4E4E4E',
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)

        def add_tamales():
            current_status01 = 'Added Tamales!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg='#4E4E4E',
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)

        def add_waffels():
            current_status01 = 'Added Waffels!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg='#4E4E4E',
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)

        def add_french_toast():
            current_status01 = 'Added French Toast!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg='#4E4E4E',
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)

        def add_cereal():
            current_status01 = 'Added Cereals!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg='#4E4E4E',
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)

        def add_pancakes():
            current_status01 = 'Added Pancakes!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg='#4E4E4E',
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)

        def add_bacon():
            current_status01 = 'Added Bacon!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg='#4E4E4E',
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)

        eggs = Button(root02, text=breakfast_products01, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                      fg='#FFA500', activebackground='#4E4E4E', background='#4E4E4E',
                      command=add_eggs).grid(row=2, column=0, pady=10,
                                             padx=10)

        bread = Button(root02, text=breakfast_products02, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                       fg='#FFA500', activebackground='#4E4E4E', background='#4E4E4E',
                       command=add_bread).grid(row=2, column=1, pady=10,
                                               padx=10)

        parota = Button(root02, text=breakfast_products03, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                        fg='#FFA500', activebackground='#4E4E4E', background='#4E4E4E',
                        command=add_parota).grid(row=2, column=2, pady=10,
                                                 padx=10)

        tamales = Button(root02, text=breakfast_products04, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                         fg='#FFA500', activebackground='#4E4E4E', background='#4E4E4E',
                         command=add_tamales).grid(row=2, column=3, pady=10,
                                                   padx=10)

        waffels = Button(root02, text=breakfast_products05, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                         fg='#FFA500', activebackground='#4E4E4E', background='#4E4E4E',
                         command=add_waffels).grid(row=2, column=4, pady=10,
                                                   padx=10)

        French_Toast = Button(root02, text=breakfast_products06, font=('Segoe UI Light Italic', 30), relief=SUNKEN,
                              bd=0,
                              fg='#FFA500', activebackground='#4E4E4E', background='#4E4E4E',
                              command=add_french_toast).grid(row=3, column=0, pady=5,
                                                             padx=5)

        Cereals = Button(root02, text=breakfast_products07, font=('Segoe UI Light Italic', 30), relief=SUNKEN,
                         bd=0,
                         fg='#FFA500', activebackground='#4E4E4E', background='#4E4E4E',
                         command=add_cereal).grid(row=3, column=1, pady=5,
                                                  padx=5)

        Pancakes = Button(root02, text=breakfast_products08, font=('Segoe UI Light Italic', 30), relief=SUNKEN,
                          bd=0,
                          fg='#FFA500', activebackground='#4E4E4E', background='#4E4E4E',
                          command=add_pancakes).grid(row=3, column=2, pady=5,
                                                     padx=5)

        Bacon = Button(root02, text=breakfast_products09, font=('Segoe UI Light Italic', 30), relief=SUNKEN,
                       bd=0,
                       fg='#FFA500', activebackground='#4E4E4E', background='#4E4E4E',
                       command=add_bacon).grid(row=3, column=3, pady=5,
                                               padx=5)

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

    def destroy_window02():
        root.destroy()

    exit_btn = Button(root, text='<- EXIT', relief=SUNKEN, bd=0, fg='red', bg='#4E4E4E',
                      font=('Segoe UI Light Italic', 15), command=destroy_window02).pack()


start_btn = Button(w, text='Start', fg="#FFA500", font=('Segoe UI Light Italic', 20), bg='#4E4E4E', relief=SUNKEN,
                   borderwidth=0, activeforeground='white', activebackground='#FFA500',
                   command=start_page).pack(side=TOP, pady=20)


def error01():
    messagebox.showerror('Err!', 'This Button is Still Under Development')


add_item_btn = Button(w, text='Add New Item to Database', fg="#00FF00", font=('Segoe UI Light Italic', 20),
                      bg='#4E4E4E', relief=SUNKEN,
                      borderwidth=0, activeforeground='white', activebackground='#00FF00',
                      command=error01).pack(side=TOP, pady=20)


def destroy_window():
    w.destroy()


exit_btn = Button(w, text='<- EXIT', relief=SUNKEN, bd=0, fg='red', bg='#4E4E4E',
                  font=('Segoe UI Light Italic', 15), command=destroy_window).pack(side=BOTTOM)

w.mainloop()
