from tkinter import *
from tkinter import messagebox
from database import *
from send_info import receive_info
from order_page import *

is_background_color_black = True
background_color = '#4E4E4E'

if not is_background_color_black:
    background_color = 'white'
elif is_background_color_black:
    background_color = '#4E4E4E'

w = Tk()
w.title('R-JPOS')
w.config(bg=background_color)
w.attributes('-fullscreen', True)
icon = PhotoImage(file='assets/cashier.png')
w.iconphoto(False, icon)


def start_page():
    global is_background_color_black, background_color
    if not is_background_color_black:
        background_color = 'white'
    elif is_background_color_black:
        background_color = '#4E4E4E'
    global icon
    root = Toplevel(w)
    root.title('Order Page')
    root.attributes('-fullscreen', True)
    root.config(bg=background_color)
    root.iconphoto(False, icon)
    Category_lf = LabelFrame(root, text='Food Category:', relief=GROOVE, bg=background_color, width=550, height=650
                             , font=('Segoe UI Light Italic', 20), fg='#8CFF1A')
    Category_lf.pack(side=TOP, padx=10)

    def breakfast_page():
        global is_background_color_black, background_color
        if not is_background_color_black:
            background_color = 'white'
        elif is_background_color_black:
            background_color = '#4E4E4E'
        root02 = Toplevel(root)
        root02.title('Breakfast Order Page')
        root02.attributes('-fullscreen', True)
        root02.config(bg=background_color)
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

        Button(root02, text='<- EXIT', relief=SUNKEN, bd=0, fg='red', bg=background_color,
               font=('Segoe UI Light Italic', 15), command=destroy_window).grid(row=1, column=0)

        current_status = ''
        full_status = 'Status : ' + str(current_status)

        def add_eggs():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Eggs!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Eggs')

        def add_bread():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Bread!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Bread')

        def add_parota():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Parota!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Parota')

        def add_tamales():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Tamales!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Tamales')

        def add_waffels():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Waffels!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Waffels')

        def add_french_toast():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added French Toast!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('French Toast')

        def add_cereal():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Cereals!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Cereal')

        def add_pancakes():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Pancakes!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Pancakes')

        def add_bacon():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Bacon!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root02, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Bacon')

        eggs = Button(root02, text=breakfast_products01, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                      fg='#FFA500', activebackground=background_color, background=background_color,
                      command=add_eggs).grid(row=2, column=0, pady=10,
                                             padx=10)

        bread = Button(root02, text=breakfast_products02, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                       fg='#FFA500', activebackground=background_color, background=background_color,
                       command=add_bread).grid(row=2, column=1, pady=10,
                                               padx=10)

        parota = Button(root02, text=breakfast_products03, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                        fg='#FFA500', activebackground=background_color, background=background_color,
                        command=add_parota).grid(row=2, column=2, pady=10,
                                                 padx=10)

        tamales = Button(root02, text=breakfast_products04, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                         fg='#FFA500', activebackground=background_color, background=background_color,
                         command=add_tamales).grid(row=2, column=3, pady=10,
                                                   padx=10)

        waffels = Button(root02, text=breakfast_products05, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                         fg='#FFA500', activebackground=background_color, background=background_color,
                         command=add_waffels).grid(row=2, column=4, pady=10,
                                                   padx=10)

        French_Toast = Button(root02, text=breakfast_products06, font=('Segoe UI Light Italic', 30), relief=SUNKEN,
                              bd=0,
                              fg='#FFA500', activebackground=background_color, background=background_color,
                              command=add_french_toast).grid(row=3, column=0, pady=5,
                                                             padx=5)

        Cereals = Button(root02, text=breakfast_products07, font=('Segoe UI Light Italic', 30), relief=SUNKEN,
                         bd=0,
                         fg='#FFA500', activebackground=background_color, background=background_color,
                         command=add_cereal).grid(row=3, column=1, pady=5,
                                                  padx=5)

        Pancakes = Button(root02, text=breakfast_products08, font=('Segoe UI Light Italic', 30), relief=SUNKEN,
                          bd=0,
                          fg='#FFA500', activebackground=background_color, background=background_color,
                          command=add_pancakes).grid(row=3, column=2, pady=5,
                                                     padx=5)

        Bacon = Button(root02, text=breakfast_products09, font=('Segoe UI Light Italic', 30), relief=SUNKEN,
                       bd=0,
                       fg='#FFA500', activebackground=background_color, background=background_color,
                       command=add_bacon).grid(row=3, column=3, pady=5,
                                               padx=5)

    breakfast_btn = Button(Category_lf, text='Breakfast', bg=background_color, relief=SUNKEN, bd=0, fg='#007FFF',
                           font=('Segoe UI Light Italic', 35), activebackground=background_color,
                           activeforeground='red', command=breakfast_page).pack(side=TOP, pady=10)

    def lunch_page():
        global is_background_color_black, background_color
        if not is_background_color_black:
            background_color = 'white'
        elif is_background_color_black:
            background_color = '#4E4E4E'
        root06 = Toplevel(root)
        root06.title('Lunch Page')
        root06.attributes('-fullscreen', True)
        root06.config(bg=background_color)
        root06.iconphoto(False, icon)

        lunch_products00 = lunch_foods[0] + ' : ' + str(lunch_prices[0])
        lunch_products01 = lunch_foods[1] + ' : ' + str(lunch_prices[1])
        lunch_products02 = lunch_foods[2] + ' : ' + str(lunch_prices[2])
        lunch_products03 = lunch_foods[3] + ' : ' + str(lunch_prices[3])
        lunch_products04 = lunch_foods[4] + ' : ' + str(lunch_prices[4])

        current_status = ''
        full_status = 'Added ' + str(current_status) + '!'

        def destroy_window():
            root06.destroy()

        exit_btn = Button(root06, text='<- EXIT', relief=SUNKEN, bd=0, fg='red', bg=background_color,
                          font=('Segoe UI Light Italic', 15), command=destroy_window).grid(row=1, column=0)

        def add_rice():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Rice!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root06, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Rice')

        def add_fish():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Fish!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root06, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Fish')

        def add_chicken():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Chicken!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root06, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Chicken')

        def add_salad():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Salad!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root06, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Salad')

        def add_pasta():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Pasta!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root06, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Pasta')

        rice = Button(root06, text=lunch_products00, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                      fg='#FFA500', activebackground=background_color, background=background_color,
                      command=add_rice).grid(row=2, column=0, pady=10,
                                             padx=10)

        fish = Button(root06, text=lunch_products01, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                      fg='#FFA500', activebackground=background_color, background=background_color,
                      command=add_fish).grid(row=2, column=1, pady=10,
                                             padx=10)

        chicken = Button(root06, text=lunch_products02, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                         fg='#FFA500', activebackground=background_color, background=background_color,
                         command=add_chicken).grid(row=2, column=2, pady=10,
                                                   padx=10)

        salad = Button(root06, text=lunch_products03, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                       fg='#FFA500', activebackground=background_color, background=background_color,
                       command=add_salad).grid(row=2, column=3, pady=10,
                                               padx=10)

        pasta = Button(root06, text=lunch_products04, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                       fg='#FFA500', activebackground=background_color, background=background_color,
                       command=add_pasta).grid(row=2, column=0, pady=10,
                                               padx=10)

    lunch_btn = Button(Category_lf, text='Lunch', bg=background_color, relief=SUNKEN, bd=0, fg='#007FFF',
                       font=('Segoe UI Light Italic', 35), activebackground=background_color,
                       activeforeground='red', command=lunch_page).pack(side=TOP, pady=10)

    def dinner_page():
        global is_background_color_black, background_color
        if not is_background_color_black:
            background_color = 'white'
        elif is_background_color_black:
            background_color = '#4E4E4E'
        root09 = Toplevel(root)
        root09.title('Dinner Page')
        root09.attributes('-fullscreen', True)
        root09.config(bg=background_color)
        root09.iconphoto(False, icon)

        current_status = ''
        full_status = 'Added ' + str(current_status) + '!'

        def destroy_window():
            root09.destroy()

        exit_btn = Button(root09, text='<- EXIT', relief=SUNKEN, bd=0, fg='red', bg=background_color,
                          font=('Segoe UI Light Italic', 15), command=destroy_window).grid(row=1, column=0)

        dinner_products00 = dinner_foods[0] + ' : ' + str(dinner_prices[0])
        dinner_products01 = dinner_foods[1] + ' : ' + str(dinner_prices[1])
        dinner_products02 = dinner_foods[2] + ' : ' + str(dinner_prices[2])
        dinner_products03 = dinner_foods[3] + ' : ' + str(dinner_prices[3])
        dinner_products04 = dinner_foods[4] + ' : ' + str(dinner_prices[4])
        dinner_products05 = dinner_foods[5] + ' : ' + str(dinner_prices[5])

        def add_burger():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Pasta!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root09, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Burger')

        burger = Button(root09, text=dinner_products00, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                        fg='#FFA500', activebackground=background_color, background=background_color,
                        command=add_burger).grid(row=2, column=0, pady=10,
                                                 padx=10)

        def add_nuggets():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added nuggets!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root09, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Nuggets')

        nuggets = Button(root09, text=dinner_products01, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                         fg='#FFA500', activebackground=background_color, background=background_color,
                         command=add_nuggets).grid(row=2, column=1, pady=10,
                                                   padx=10)

        def add_chips():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added chips!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root09, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Chips')

        chips = Button(root09, text=dinner_products02, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                       fg='#FFA500', activebackground=background_color, background=background_color,
                       command=add_chips).grid(row=2, column=2, pady=10,
                                               padx=10)

        def add_pizza():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Pizza!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root09, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Pizza')

        pizza = Button(root09, text=dinner_products03, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                       fg='#FFA500', activebackground=background_color, background=background_color,
                       command=add_pizza).grid(row=2, column=3, pady=10,
                                               padx=10)

        def add_tacos():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Tacos!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root09, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Tacos')

        tacos = Button(root09, text=dinner_products04, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                       fg='#FFA500', activebackground=background_color, background=background_color,
                       command=add_tacos).grid(row=3, column=1, pady=10,
                                               padx=10)

        def add_chimichangas():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Chimichangas!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root09, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Chimichangas')

        chimichangas = Button(root09, text=dinner_products05, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                              fg='#FFA500', activebackground=background_color, background=background_color,
                              command=add_chimichangas).grid(row=3, column=2, pady=10,
                                                             padx=10)

    dinner_btn = Button(Category_lf, text='Dinner', bg=background_color, relief=SUNKEN, bd=0, fg='#007FFF',
                        font=('Segoe UI Light Italic', 35), activebackground=background_color,
                        activeforeground='red', command=dinner_page).pack(side=TOP, pady=10)

    def dessert_page():
        global is_background_color_black, background_color
        if not is_background_color_black:
            background_color = 'white'
        elif is_background_color_black:
            background_color = '#4E4E4E'
        root04 = Toplevel(root)
        root04.title('Dessert Page')
        root04.attributes('-fullscreen', True)
        root04.config(bg=background_color)
        root04.iconphoto(False, icon)

        def destroy_window03():
            root04.destroy()

        exit_btn = Button(root04, text='<- EXIT', relief=SUNKEN, bd=0, fg='red', bg=background_color,
                          font=('Segoe UI Light Italic', 15), command=destroy_window03).grid(row=1, column=0)

        dessert_products00 = dessert_foods[0] + ' : ' + str(dessert_prices[0])
        dessert_products01 = dessert_foods[1] + ' : ' + str(dessert_prices[1])
        dessert_products02 = dessert_foods[2] + ' : ' + str(dessert_prices[2])
        dessert_products03 = dessert_foods[3] + ' : ' + str(dessert_prices[3])
        dessert_products04 = dessert_foods[4] + ' : ' + str(dessert_prices[4])

        def add_strawberry_milkshake():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added StrawBerry Milkshake!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root04, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Strawberry Milkshake')

        strb_mlsh = Button(root04, text=dessert_products00, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                           fg='#FFA500', activebackground=background_color, background=background_color,
                           command=add_strawberry_milkshake).grid(row=2, column=0, pady=10,
                                                                  padx=10)

        def add_oreo_milkshake():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Oreo Milkshake!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root04, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Oreo Milkshake')

        oreo_mlsh = Button(root04, text=dessert_products01, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                           fg='#FFA500', activebackground=background_color, background=background_color,
                           command=add_oreo_milkshake).grid(row=2, column=1, pady=10,
                                                            padx=10)

        def add_kitkat_milkshake():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added KitKat Milkshake!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root04, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Kitkat Milkshake')

        ktkt_mlsh = Button(root04, text=dessert_products02, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                           fg='#FFA500', activebackground=background_color, background=background_color,
                           command=add_kitkat_milkshake).grid(row=2, column=2, pady=10,
                                                              padx=10)

        def add_lotus_milkshake():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Lotus Milkshake!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root04, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Lotus Milkshake')

        lotus_mlsh = Button(root04, text=dessert_products03, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                            fg='#FFA500', activebackground=background_color, background=background_color,
                            command=add_lotus_milkshake).grid(row=3, column=0, pady=10,
                                                              padx=10)

        def add_chocolate_milkshake():
            global is_background_color_black, background_color
            if not is_background_color_black:
                background_color = 'white'
            elif is_background_color_black:
                background_color = '#4E4E4E'
            current_status01 = 'Added Chocolate Milkshake!'
            full_status01 = 'Status : ' + str(current_status01)
            status_lbl = Label(root04, text=full_status01, fg='yellow', bg=background_color,
                               font=('Segoe UI Light Italic', 15)).grid(row=1, column=1, pady=5, padx=5)
            get_order('Chocolate Milkshake')

        chlt_mlsh = Button(root04, text=dessert_products04, font=('Segoe UI Light Italic', 30), relief=SUNKEN, bd=0,
                           fg='#FFA500', activebackground=background_color, background=background_color,
                           command=add_chocolate_milkshake).grid(row=3, column=1, pady=10,
                                                                 padx=10)

    dessert_btn = Button(Category_lf, text='Desserts', bg=background_color, relief=SUNKEN, bd=0, fg='#007FFF',
                         font=('Segoe UI Light Italic', 35), activebackground=background_color,
                         activeforeground='red', command=dessert_page).pack(side=TOP, pady=10)

    send_info = Button(Category_lf, text='Send all Info to Kitchen Unit', bg=background_color, relief=SUNKEN,
                       bd=0, fg='red',
                       font=('Segoe UI Light Italic', 35), activebackground=background_color,
                       activeforeground='green', command=store_order).pack(side=TOP, pady=10)

    def destroy_window02():
        root.destroy()

    exit_btn = Button(root, text='<- EXIT', relief=SUNKEN, bd=0, fg='red', bg=background_color,
                      font=('Segoe UI Light Italic', 15), command=destroy_window02).pack()


start_btn = Button(w, text='Start', fg="#FFA500", font=('Segoe UI Light Italic', 20), bg=background_color,
                   relief=SUNKEN,
                   borderwidth=0, activeforeground='white', activebackground='#FFA500',
                   command=start_page).pack(side=TOP, pady=20)


def error01():
    messagebox.showerror('Err!', 'This Button is Still Under Development')


add_item_btn = Button(w, text='Add New Item to Database', fg="#00FF00", font=('Segoe UI Light Italic', 20),
                      bg=background_color, relief=SUNKEN,
                      borderwidth=0, activeforeground='white', activebackground='#00FF00',
                      command=error01).pack(side=TOP, pady=20)


def setting_page():
    global is_background_color_black, background_color
    if not is_background_color_black:
        background_color = 'white'
    elif is_background_color_black:
        background_color = '#4E4E4E'
    root10 = Toplevel(w)
    root10.title('Settings Page')
    root10.attributes('-fullscreen', True)
    root10.config(bg=background_color)

    def theme_swicther_on():
        global is_background_color_black, background_color
        is_background_color_black = False

    def theme_swicther_off():
        global is_background_color_black, background_color
        is_background_color_black = True

    light_mode_on = Button(root10, text='Light Mode ON', relief=SUNKEN, bd=0, fg='green', bg=background_color,
                           font=('Segoe UI Light Italic', 25), command=theme_swicther_on).pack()

    light_mode_on = Button(root10, text='Light Mode OFF', relief=SUNKEN, bd=0, fg='yellow', bg=background_color,
                           font=('Segoe UI Light Italic', 25), command=theme_swicther_off).pack()

    def destroy_window02():
        root10.destroy()

    exit_btn = Button(root10, text='<- EXIT', relief=SUNKEN, bd=0, fg='red', bg=background_color,
                      font=('Segoe UI Light Italic', 15), command=destroy_window02).pack()


setting_btn = Button(w, text='Settings', fg='yellow', font=('Segoe UI Light Italic', 20),
                     bg=background_color, relief=SUNKEN,
                     borderwidth=0, activeforeground='white', activebackground='#00FF00',
                     command=setting_page).pack(side=TOP, pady=20)


def destroy_window():
    w.destroy()


exit_btn = Button(w, text='<- EXIT', relief=SUNKEN, bd=0, fg='red', bg=background_color,
                  font=('Segoe UI Light Italic', 15), command=destroy_window).pack(side=BOTTOM)

w.mainloop()
