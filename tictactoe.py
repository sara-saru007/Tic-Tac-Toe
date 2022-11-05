from tkinter import*
from tkinter import font as tkFont
from tkinter import simpledialog
from tkinter import messagebox
import random as r

win = Tk()
win.title("NOUGHTS AND CROSSES")
win.state('zoomed')
win.rowconfigure(0,weight=1)
win.columnconfigure(0,weight=1)
bg = PhotoImage(file = "C:\\Users\\tanis\\Downloads\\bk.png")
canvas1 = Canvas(win, width = 200, 
                 height = 200) 

canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")

canvas1.create_text( 450, 450)
photo = PhotoImage(file = "")
photo = photo.subsample(2,2)
label2 = Label(canvas1 , image = photo)
label2.pack(padx = 100,pady = 100,side = "right")

def showframe2():
    win.withdraw()
 
def Start():
    global s
    global na1
    global na2
    s = simpledialog.askinteger("INPUT","ENTER NUMBER OF MATCHES YOU WISH TO  PLAY: ")
    na1 = simpledialog.askstring("INPUT","ENTER THE NAME OF PLAYER 1 : ")
    na2 = simpledialog.askstring("INPUT","ENTER THE NAME OF PLAYER 2 : ")
    if s>0:
        btn_start["text"] = "LET'S PLAY" 
        btn_start["command"] = showframe2
        btn_start["bg"] = "gold"
    else:
        messagebox.showerror("Error","Invalid Entry!TRY AGAIN")

helv36 = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)
btn_start = Button(canvas1 , text = "START" ,width = 15,height = 3,bg = "light blue",fg="brown",font = helv36, command = Start)
btn_start.pack(padx = 100,pady = 100,side = "bottom")
from tkinter import *
from tkinter import messagebox
import random as r
def button(frame):
    b=Button(frame,padx=1,bg="light sky blue",width=3,text="   ",font=('algerian',60,'bold'),bd=(15))
    return b
def change_a():
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
def reset():
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
def check():
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Congrats!!","'"+a+"' has won")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' has won")
        reset()
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
        label.config(text=a+"'s Chance")
root=Tk()
root.title("NOUGHTS AND CROSSES")
a=r.choice(['O','X'])
colour={'O':"yellow",'X':"red"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label=Label(text=a+"'s Chance",font=('rockwell',20,'bold'))
root.mainloop()

