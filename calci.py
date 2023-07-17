                                                #Standard calculator
from tkinter import *
import math
from tkinter import messagebox
operator=''

#-------------------------------------------------------------------------------
#COMMANDS
def Exit():
    Exit=messagebox.askyesno("CALCULATOR","Confirm if you want to exit")
    if Exit > 0:
        my_window.destroy()

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btnAC():
    text_input.set("")

def btnresult():
    global operator
    try:
        result=str(eval(operator))
        text_input.set(result)
        operator=''
    except:
        text_input.set("")
        operator=''
        messagebox.showinfo("Error","Enter valid equation")
        
def btnback():
    global operator
    operator=operator[0:-1]
    text_input.set(operator)
def standard():
    global text_input,my_window
    my_window=Tk()
    my_window.title("STANDARD CALCULATOR")
    my_window.configure(bg="grey",width=400,height=550)
    my_window.resizable(width=False, height=False)
    text_input=StringVar()
    label_1=Label(my_window,text="Solve your difficult problems in a second",bg="Black",fg="white",font="Arial 25 bold italic underline",bd=10,relief="sunken",padx=3,pady=3)
    label_1.grid(row=0,columnspan=5)

    space_label_1=Label(my_window,text='',bg="grey")
    space_label_1.grid(row=1)

    #Buttons
    label_2=Label(my_window,textvariable=text_input,width=32,bg="white",fg="black",font="Arial 25 bold",bd=5,relief="groove",justify="right")
    label_2.grid(row=3,columnspan=5)

    space_label_2=Label(my_window,text="",bg="grey")
    space_label_2.grid(row=4)

    button_k1=Button(my_window,text="CE",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=btnAC)
    button_k1.grid(row=5,column=0,pady=0.5)

    button_k2=Button(my_window,text="9",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick(9))
    button_k2.grid(row=5,column=1,pady=0.5)

    button_k3=Button(my_window,text="8",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick(8))
    button_k3.grid(row=5,column=2,pady=0.5)

    button_k4=Button(my_window,text="7",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick(7))
    button_k4.grid(row=5,column=3,pady=0.5)

    button_k5=Button(my_window,text="C",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=btnback)
    button_k5.grid(row=5,column=4,pady=0.5)

    button_k6=Button(my_window,text="%",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick("%"))
    button_k6.grid(row=6,column=0,pady=0.5)

    button_k7=Button(my_window,text="6",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick(6))
    button_k7.grid(row=6,column=1,pady=0.5)

    button_k8=Button(my_window,text="5",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick(5))
    button_k8.grid(row=6,column=2,pady=0.5)

    button_k9=Button(my_window,text="4",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick(4))
    button_k9.grid(row=6,column=3,pady=0.5)

    button_k10=Button(my_window,text="*",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick("*"))
    button_k10.grid(row=6,column=4,pady=0.5)

    button_k11=Button(my_window,text="(",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick("("))
    button_k11.grid(row=7,column=0,pady=0.5)

    button_k12=Button(my_window,text="3",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick(3))
    button_k12.grid(row=7,column=1,pady=0.5)

    button_k13=Button(my_window,text="2",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick(2))
    button_k13.grid(row=7,column=2,pady=0.5)

    button_k14=Button(my_window,text="1",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick(1))
    button_k14.grid(row=7,column=3,pady=0.5)

    button_k15=Button(my_window,text="+",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick("+"))
    button_k15.grid(row=7,column=4,pady=0.5)

    button_k16=Button(my_window,text=")",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick(")"))
    button_k16.grid(row=8,column=0,pady=0.5)

    button_k17=Button(my_window,text=".",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick("."))
    button_k17.grid(row=8,column=1,pady=0.5)

    button_k18=Button(my_window,text="0",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick(0))
    button_k18.grid(row=8,column=2,pady=0.5)

    button_k19=Button(my_window,text="/",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick("/"))
    button_k19.grid(row=8,column=3,pady=0.5)

    button_k18=Button(my_window,text="-",bg="Black",width=5, height=2,fg="white",font="Arial 18 bold ",bd=2,command=lambda:btnclick("-"))
    button_k18.grid(row=8,column=4,pady=0.5)
    button_kR=Button(my_window,text="=",width=5, height=2,bg="Black",fg="white",font="Arial 18 bold ",bd=2,command=btnresult)
    button_kR.grid(row=10,column=2)
    menubar=Menu(my_window)
    menubar.add_command(label="Scientific Calculator",command=lambda:[my_window.destroy(),scientific()])

    menubar.add_command(label="Standard Calculator",command=lambda:[my_window.destroy(),standard()])
    menubar.add_command(label="Exit",command=Exit)
    my_window.config(menu=menubar)
    my_window.mainloop()
#------------------------------------------------------------------------------------------------------

def scientific():
    def click(val):
        e = entry.get()  # getting the value
        ans = " "

        try:
        # To clear the last inserted text
            if val == "C":
                e = e[0:len(e) - 1]  # deleting the last entered value
                entry.delete(0, "end")
                entry.insert(0, e)
                entry1.delete(0, "end")
                return

        # To delete everything
            elif val == "CE":
                entry.delete(0, "end")
                entry1.delete(0, "end")
        # Square root
            elif val == "√":
                entry1.insert(0,"√")
                ans = math.sqrt(eval(e))

        # pi value
            elif val == "π":
                entry1.insert(0,"π")
                ans = math.pi

        # cos value
            elif val == "cosθ":
                entry1.insert(0,"cos")
                ans = math.cos(math.radians(eval(e)))

        # sin value
            elif val == "sinθ":
                entry1.insert(0,"sin")
                ans = math.sin(math.radians(eval(e)))
        # tan Value
            elif val == "tanθ":
                entry1.insert(0,"tan")
                ans = math.tan(math.radians(eval(e)))

        # 2π value
            elif val == "2π":
                entry1.insert(0,"2π")
                ans = 2 * math.pi

        # cosh value
            elif val == "cosh":
                entry1.insert(0,"cosh")
                ans = math.cosh(eval(e))

        # sinh value
            elif val == "sinh":
                entry1.insert(0,"sinh")
                ans = math.sinh(eval(e))

        # tanh value
            elif val == "tanh":
                entry1.insert(0,"tanh")
                ans = math.tanh(eval(e))
         # cube root value
            elif val == chr(8731):
                entry1.insert(0,chr(8731))
                ans = eval(e) ** (1 / 3)

        # x to the power y
            elif val == "x\u02b8":
                entry1.insert(0,"x\u02b8")
                entry.insert("end", "**")
                return

        # cube value
            elif val == "x\u00B3":
                entry1.insert(0,"x\u00B3")
                ans = eval(e) ** 3

        # square value
            elif val == "x\u00B2":
                entry1.insert(0,"x\u00B2")
                ans = eval(e) ** 2

        # ln value
            elif val == "ln":
                entry1.insert(0,"ln")
                ans = math.log2(eval(e))

        # deg value
            elif val == "deg":
                entry1.insert(0,"deg")
                ans = math.degrees(eval(e))

        # radian value
            elif val == "rad":
                entry1.insert(0,"rad")
                ans = math.radians(eval(e))

        # e value
            elif val == "e":
                entry1.insert(0,"e")
                ans = math.e
        # log10 value
            elif val == "log10":
                entry1.insert(0,"log10")
                ans = math.log10(eval(e))

        # factorial value
            elif val == "x!":
                entry1.insert(0,"x!")
                ans = math.factorial(eval(e))

        # division operator
            elif val == chr(247):
                entry1.insert(0,char(247))
                entry.insert("end", "/")
                return

            elif val == "=":
                ans = eval(e)
            else:
                entry1.insert("end", val)
                entry.insert("end", val)
                return
    
            entry.delete(0, "end")
            entry.insert(0, ans)

        except SyntaxError:
            pass

    global text_input,my_window
    my_window=Tk()
    my_window.title("STANDARD CALCULATOR")
    my_window.configure(bg="grey",width=600,height=700)
    my_window.resizable(width=False, height=False)
    text_input=StringVar()
    label_1=Label(my_window,text="Solve your difficult problems in a second",bg="Black",fg="white",font="Arial 30 bold italic underline",bd=10,relief="sunken",padx=3,pady=3)
    label_1.grid(row=0,columnspan=8)

    space_label_1=Label(my_window,text='',bg="grey")
    space_label_1.grid(row=1)

    entry1 = Entry(my_window,bg="white",fg="black",font="Arial 25 bold",bd=10,relief="groove",width=22)
    entry1.grid(row=3, column=0, columnspan=4)
    
    entry = Entry(my_window,bg="white",fg="black",font="Arial 25 bold",bd=10,relief="groove",width=22)
    entry.grid(row=3, column=4, columnspan=4)

    space_label_2=Label(my_window,text="",bg="grey")
    space_label_2.grid(row=4)

    button_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ", "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
               "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", "7", "8", "9", chr(247), "ln", "deg",
               "rad", "e", "0", ".", "%", "=", "log10", "(", ")", "x!"]
    r = 5
    c = 0
    for i in button_list:
        button = Button(my_window, width=5, height=2, bd=2, text=i, bg="black", fg="white",
                                font=("arial", 18, "bold"), command=lambda button=i: [click(button)])
        button.grid(row=r, column=c, pady=1)
        c += 1
        if c > 7:
            r += 1
            c = 0

    space_label_3=Label(my_window,text="",bg="grey")
    space_label_3.grid(row=9)

    menubar=Menu(my_window)
    menubar.add_command(label="Scientific Calculator",command=lambda:[my_window.destroy(),scientific()])
    menubar.add_command(label="Standard Calculator",command=lambda:[my_window.destroy(),standard()])
    menubar.add_command(label="Exit",command=Exit)
    my_window.config(menu=menubar)
    my_window.mainloop()
    
standard()


