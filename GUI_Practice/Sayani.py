from tkinter import*

root = Tk()
root.title("FizzBuzz")
root.geometry("1200x1000")

def fizzbuzz(i):
    labl1 = Label(root, text=li[i], font=("Helvetica", 25), padx=10, pady=10, width=15)
    labl1.place(x=550,y=500)
    labl2 = Label(root, text=str(frm+i), font=("Helvetica", 25), padx=10, pady=10, width=15)
    labl2.place(x=550, y=550)

    if i+frm == frm:
        btn2 = Button(root, text="<<",font=("Helvetica", 25), padx=10, pady=10, width=5, state=DISABLED)
        btn2.place(x=350, y=500)
        btn3 = Button(root, text=">>", font=("Helvetica", 25), padx=10, pady=10, width=5, command= lambda: fizzbuzz(i+1))
        btn3.place(x=900, y=500)

    elif i+frm == to:
        btn2 = Button(root, text="<<", font=("Helvetica", 25), padx=10, pady=10, width=5, command=lambda: fizzbuzz(i - 1))
        btn2.place(x=350, y=500)
        btn3 = Button(root, text=">>", font=("Helvetica", 25), padx=10, pady=10, width=5, state=DISABLED)
        btn3.place(x=900, y=500)

    else:
        btn2 = Button(root, text="<<", font=("Helvetica", 25), padx=10, pady=10, width=5, command=lambda: fizzbuzz(i - 1))
        btn2.place(x=350, y=500)
        btn3 = Button(root, text=">>", font=("Helvetica", 25), padx=10, pady=10, width=5, command=lambda: fizzbuzz(i + 1))
        btn3.place(x=900, y=500)


def submit():
    global frm,to
    frm = int(ent1.get())
    to = int(ent2.get())
    global li
    li = []
    for i in range(frm, to+1):
        if (i%5==0) and (i%3==0):
            li.append("FizzBuzz")
        elif i%3==0:
            li.append("Fizz")
        elif i%5==0:
            li.append("Buzz")
        else:
            li.append("None")
    fizzbuzz(0)
filename = PhotoImage(file="poster.png")
back_lbl = Label(root, image=filename)
#back_lbl.pack()
#back_lbl.grid(row=0, column=0)
back_lbl.place(x=0, y=0)

lbl1 = Label(root, text="Welcome To FizzBuzz", font=("Helvetica", 60), padx=10, pady=10)
lbl1.place(x=350, y=100)

lbl2 = Label(root, text="Enter Range:", font=("Helvetica", 25), padx=10, pady=10, width=20)
lbl2.place(x=350, y=250)

lbl3 = Label(root, text="From :", font=("Helvetica", 25), padx=10, pady=10, width=15)
lbl3.place(x=400, y=330)

lbl4 = Label(root, text="To :", font=("Helvetica", 25), padx=10, pady=10, width=15)
lbl4.place(x=400, y=400)

ent1 = Entry(root, font=("Helvetica", 25), width=20, borderwidth=4)
ent1.place(x=750, y=340)

ent2 = Entry(root, font=("Helvetica", 25), width=20, borderwidth=4)
ent2.place(x=750, y=410)

btn1 = Button(root, text="Submit", font=("Helvetica", 20), padx=10, pady=10, width=5, command=submit)
btn1.place(x=1200, y=350)

root.mainloop()