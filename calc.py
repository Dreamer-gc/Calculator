from tkinter import *
window = Tk()
window.geometry("300x400")
window.title("Calculator")
expression=""
def exp(n):
    global expression
    expression+=str(n)
    I_T.set(expression)

def apply_operation(a, b, op):
    a = float(a)
    b = float(b)

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError
        return a / b

def is_operator(c):
    return c in "+-*/"

def evaluate_expression(expr):
    if not expr:
        raise ValueError

    if is_operator(expr[-1]):
        raise ValueError

    numbers = []
    operators = []
    num = ""

    for char in expr:
        if char.isdigit() or char == '.':
            num += char
        elif is_operator(char):
            if num == "":
                raise ValueError
            numbers.append(num)
            operators.append(char)
            num = ""

    numbers.append(num)

    i = 0
    while i < len(operators):
        if operators[i] in "*/":
            result = apply_operation(numbers[i], numbers[i+1], operators[i])
            numbers[i] = str(result)
            del numbers[i+1]
            del operators[i]
        else:
            i += 1

    result = float(numbers[0])
    for i in range(len(operators)):
        result = apply_operation(result, numbers[i+1], operators[i])

    return result

def equal():
    global expression
    try:
        result = evaluate_expression(expression)
        I_T.set(result)
        expression = str(result)
    except:
        I_T.set("INVALID INPUT")
        expression = ""        
    
def dele():
    global expression
    expression=expression[:-1]
    I_T.set(expression)

def clear():
    global expression
    expression=""
    I_T.set(expression)

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
        
    else:
        bt=Button(window,text=text,command=lambda t=text: exp(t),font=("Arial",18))
        bt.grid(row=row,column=col,sticky=NSEW)
    
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
