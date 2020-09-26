# Hands-on-Practice
# Developer Student Clubs - Siliguri Institute Of Technology
# Prasun Roy - https://github.com/PRASUNR0Y

from tkinter import*

root = Tk()
root.title("FizzBuzz Game")
root.geometry("1350x650")
root.configure(background='coral')

def fizzbuzz(i):
    labl1 = Label(root, text=li[i], font=("Helvetica", 25), padx=10, pady=10, width=15,bg='RosyBrown2')
    labl1.place(x=550,y=500)
    labl2 = Label(root, text=str(frm+i), font=("Helvetica", 25), padx=10, pady=10, width=15,bg='RosyBrown2')
    labl2.place(x=550, y=550)

    if i+frm == frm:
        btn2 = Button(root, text="Prev",font=("Helvetica", 25), padx=10, pady=10, width=5, state=DISABLED,bg='red2',fg='white')
        btn2.place(x=350, y=500)
        btn3 = Button(root, text="Next", font=("Helvetica", 25), padx=10, pady=10, width=5, command= lambda: fizzbuzz(i+1),bg='red2',fg='white')
        btn3.place(x=900, y=500)

    elif i+frm == to:
        btn2 = Button(root, text="Prev", font=("Helvetica", 25), padx=10, pady=10, width=5, command=lambda: fizzbuzz(i - 1),bg='red2',fg='white')
        btn2.place(x=350, y=500)
        btn3 = Button(root, text="Next", font=("Helvetica", 25), padx=10, pady=10, width=5, state=DISABLED,bg='red2',fg='white')
        btn3.place(x=900, y=500)

    else:
        btn2 = Button(root, text="Prev", font=("Helvetica", 25), padx=10, pady=10, width=5, command=lambda: fizzbuzz(i - 1),bg='red2',fg='white')
        btn2.place(x=350, y=500)
        btn3 = Button(root, text="Next", font=("Helvetica", 25), padx=10, pady=10, width=5, command=lambda: fizzbuzz(i + 1),bg='red2',fg='white')
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

#filename = PhotoImage(file="Walpaper.png")
#back_lbl = Label(root, background='yellow',fg='blue')
#back_lbl.pack()
#back_lbl.grid(row=0, column=0)
#back_lbl.place(x=0, y=0)

lbl1 = Label(root, text="Welcome To FizzBuzz Game", font=("Helvetica", 60), padx=10, pady=10, bg='blue',fg='white')
lbl1.place(x=150, y=40)

lbl2 = Label(root, text="Enter Your Range:", font=("Helvetica", 25), padx=10, pady=10, width=20,bg='skyblue',fg='blue')
lbl2.place(x=200, y=250)

lbl3 = Label(root, text="From :", font=("Helvetica", 25), padx=10, pady=10, width=15,fg='firebrick2',background='coral')
lbl3.place(x=250, y=330)

lbl4 = Label(root, text="To :", font=("Helvetica", 25), padx=10, pady=10, width=15,fg='firebrick2',background='coral')
lbl4.place(x=250, y=400)

ent1 = Entry(root, font=("Helvetica", 25), width=20, borderwidth=4,bg='tan1')
ent1.place(x=500, y=340)

ent2 = Entry(root, font=("Helvetica", 25), width=20, borderwidth=4,bg='tan1')
ent2.place(x=500, y=410)

btn1 = Button(root, text="Submit", font=("Helvetica", 20), padx=10, pady=10, width=5,bg='yellow', command=submit)
btn1.place(x=900, y=360)

root.mainloop()