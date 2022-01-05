from tkinter import messagebox
order_list = []


def store_order():
    global order_list
    with open('order.txt', 'r+') as f:
        pre_msg = 'order = '
        full_msg = str(pre_msg) + str(order_list)
        f.write(str(full_msg))
        f.close()
    messagebox.showinfo('Done!', 'Successfully Sent!')


def get_order(order):
    global order_list
    order_list.append(str(order))
    print(order_list[0:100])
