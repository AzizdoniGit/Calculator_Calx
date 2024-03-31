from tkinter import *

root = Tk()
root.title('Calculator (Sam)')
root.geometry('292x500+650+150')
root.config(bg="black")
root.resizable(False, False)
window__entry = Entry(root, width=30, font=("Bahnschrift Ligh", 20), bg="#3d6173", bd=0, fg="#d1dee0", justify=RIGHT)
window = Listbox(root, width=30, font=("Bahnschrift Ligh", 20), bg="#243842", bd=0, fg="#d1dee0", justify=RIGHT, height=2)

def get_text():
    d = window__entry.get()
    window__entry.delete(0, END)
    window__entry.insert(0, d[:len(d)-1])

place_button = Frame(background="black", width=500, height=300, )
btn16 = Button(place_button, text='AC', height=2, width=5, bg='#3d6173', font=("Bahnschrift Light", 18), borderwidth=1,
               relief="flat", )
btn17 = Button(place_button, text='()', height=2, width=5, bg='#3d6173', font=("Bahnschrift Light", 18), borderwidth=1,
               relief="flat")
btn18 = Button(place_button, text='%', height=2, width=5, bg='#3d6173', font=("Bahnschrift Light", 18), borderwidth=1,
               relief="flat")
btn19 = Button(place_button, text='<', height=2, width=5, bg='#3d6173', font=("Bahnschrift Light", 18), borderwidth=1,
               relief="flat", command=get_text)
btn1 = Button(place_button, text='7', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
              relief="flat")
btn2 = Button(place_button, text='8', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
              relief="flat")
btn3 = Button(place_button, text='9', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
              relief="flat")
btn4 = Button(place_button, text='÷', height=2, width=5, bg='#eb732c', font=("Bahnschrift Light", 18), borderwidth=1,
              relief="flat")
btn5 = Button(place_button, text='4', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
              relief="flat")
btn6 = Button(place_button, text='5', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
              relief="flat")
btn7 = Button(place_button, text='6', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
              relief="flat")
btn8 = Button(place_button, text='×', height=2, width=5, bg='#eb732c', font=("Bahnschrift Light", 18), borderwidth=1,
              relief="flat")
btn9 = Button(place_button, text='1', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
              relief="flat")
btn10 = Button(place_button, text='2', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
               relief="flat")
btn11 = Button(place_button, text='3', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
               relief="flat")
btn12 = Button(place_button, text='+', height=2, width=5, bg='#eb732c', font=("Bahnschrift Light", 18), borderwidth=1,
               relief="flat")
btn13 = Button(place_button, text='+/-', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
               relief="flat")
btn14 = Button(place_button, text='0', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
               relief="flat")
btn15 = Button(place_button, text='.', height=2, width=5, bg='#d1dee0', font=("Bahnschrift Light", 18), borderwidth=1,
               relief="flat")
btn20 = Button(place_button, text='-', height=2, width=5, bg='#eb732c', font=("Bahnschrift Light", 18), borderwidth=1,
               relief="flat")

window__entry.pack(ipadx=5, ipady=5)
window.pack()
place_button.pack(ipady=39, ipadx=3)
btn1.grid(column=0, row=1)
btn2.grid(column=1, row=1)
btn3.grid(column=2, row=1)
btn4.grid(column=3, row=1)
btn5.grid(column=0, row=2)
btn6.grid(column=1, row=2)
btn7.grid(column=2, row=2)
btn8.grid(column=3, row=2)
btn9.grid(column=0, row=3)
btn10.grid(column=1, row=3)
btn11.grid(column=2, row=3)
btn12.grid(column=3, row=3)
btn13.grid(column=0, row=4)
btn14.grid(column=1, row=4)
btn15.grid(column=2, row=4)
btn20.grid(column=3, row=4)
btn16.grid(column=0, row=0)
btn17.grid(column=1, row=0)
btn18.grid(column=2, row=0)
btn19.grid(column=3, row=0)

root.mainloop()
