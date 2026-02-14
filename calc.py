from tkinter import *
window = Tk()
window.geometry("300x400")
window.title("Calculator")
expression=""
def exp(n):
    global expression
    expression+=str(n)
    I_T.set(expression)
    pass
def equal():
    global expression
    try:
        I_T.set(eval(expression))
        expression=str(eval(expression))
        pass
    except:
        I_T.set("INVALID INPUT")
        pass
    pass
def dele():
    global expression
    expression=expression[:-1]
    I_T.set(expression)
def clear():
    global expression
    expression=""
    I_T.set(expression)
    pass
I_T=StringVar()
dis=Entry(window,textvariable=I_T,bd=5,font=("Arial",20))
dis.grid(row=0,column=0,columnspan=4,sticky=NSEW)
buttons=[
    (7,1,0),(8,1,1),(9,1,2),('/',1,3),
    (6,2,0),(5,2,1),(4,2,2),('*',2,3),
    (3,3,0),(2,3,1),(1,3,2),('+',3,3),
    ('.',4,0),(0,4,1),('=',4,2),('-',4,3)
]
for (text,row,col) in buttons:
    if text=="=":
        eq=Button(window,text=text,command=equal,font=("Arial",18))
        eq.grid(row=row,column=col,sticky=NSEW)
        pass
    else:
        bt=Button(window,text=text,command=lambda t=text: exp(t),font=("Arial",18))
        bt.grid(row=row,column=col,sticky=NSEW)
    pass
ac=Button(window,text="Ac",command=clear,font=("Arial",18))
ac.grid(row=5,column=0,columnspan=3,sticky=NSEW)
ac=Button(window,text="X",command=dele,font=("Arial",18))
ac.grid(row=5,column=3,sticky=NSEW)

for i in range(6):
    window.rowconfigure(i,weight=1)
    pass
for i in range(4):
    window.columnconfigure(i,weight=1)
    pass
window.mainloop()