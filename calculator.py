import tkinter.messagebox as msg

def calcbutton():       #function for packing buttons in 5 frames
   L1 = ["7" , "8" , "9" , "*"]
   L2 = ["4" , "5" , "6" , "+"]
   L3 = ["1" , "2" , "3" , "-"]
   L4 = ["Quit" , "0" , ".", "=" ]

   b1 = Button(f1 , text = "C" , width = 10, height= 4 , bg = "Orange", fg = "White" , padx=5 , pady=5)
   b1.pack(side = LEFT)
   b1.bind("<Button - 1>",show)
   b2 = Button(f1 , text = "[x" , width = 10 , height=4 , bg = "Black", fg = "White", padx=5 , pady=5)
   b2.pack(side = LEFT)
   b2.bind("<Button - 1>",show)
   b4 = Button(f1 , text = "%" , width = 10 , height= 4 , bg = "Black", fg = "White", padx=5 , pady=5)
   b4.pack(side = LEFT)
   b4.bind("<Button - 1>",show)
   b3 = Button(f1 , text = "/" , width = 10, height=4 , bg = "Black", fg = "White", padx=5 , pady=5)
   b3.pack(side = LEFT)
   b3.bind("<Button - 1>",show)

   for i in L1:
      b = Button(f2 , text = i , width = 10 , height=4 , bg = "Black", fg = "White", padx=5 , pady=5)
      b.pack(side = LEFT)
      b.bind("<Button - 1>",show)

   for i in L2:
      b = Button(f3 , text = i , width = 10, height=4, bg = "Black", fg = "White", padx=5 , pady=5)
      b.pack(side = LEFT)
      b.bind("<Button - 1>",show)

   for i in L3:
      b = Button(f4 , text = i , width = 10, height=4 ,bg = "Black", fg = "White", padx=5, pady=5)
      b.pack(side = LEFT)
      b.bind("<Button - 1>",show)

   for i in L4:
      if i == "=":
         b = Button(f5 , text = i , width = 14, height=4 , bg = "Green" , fg = "White", padx=5, pady=5)
         b.pack(side = LEFT)
         b.bind("<Button - 1>",show)
      elif i == "Quit":
         b4 = Button(f5 , text = i , width = 10 , height= 4 , bg = "Red", fg = "White", padx=5 , pady=5)
         b4.pack(side = LEFT)
         b4.bind("<Button - 1>",show)
      else:
        b = Button(f5 , text = i , width = 10, height=4, bg = "Black" , fg = "White", padx=5, pady=5)
        b.pack(side = LEFT)
        b.bind("<Button - 1>",show)


def show(event):        #fuction for binding the buttons with the widget

    global scval         #initialize a global string type variable in order to update its value

    text = event.widget.cget("text")
    print(text)

    if text == "=":     # for the working of te equal to button
       if scval.get().isdigit():    #converting into integer if any digit is present in the string 
          value = int(scval.get())
       else:
          try:      # error handling such as DivisionByZero erorr
            value = eval(scval.get())
          except :
             value = "Error"
       scval.set(value)
       ent.update()

    elif text == "C":   # for the working of clear button 
        scval.set("")
        ent.update()

    elif text == "%": # working of percentage button
      if scval.get().isdigit():
          value = int(scval.get())
          value = value / 100 
      else:
          try:
            value = eval(scval.get())    #error handling 
            value = value / 100
          except:
             value = "Error"
      scval.set(value)
      ent.update()


    elif text == "Quit":   # for pop button
       a = msg.askquestion("Quit" , "Do you want to quit?")
       if a == "yes":
        win.destroy()

    elif text == "[x":  #backspace
        value = scval.get()
        n = len(scval.get())
        scval.set(value[:n-1])
        ent.update

    else :
        scval.set(scval.get() + text)  # will print the value in the entry widget
        ent.update
#Main
from tkinter import *

win = Tk()      # creating a GUI window

scval = StringVar() #intialize a string type variable to store updated values
win.title("Simple Calculator")
win.geometry("330x450")     
win.resizable(0,0)

ent = Entry(win , textvar = scval, font=('lucida 20') )  #creating an area to display operations
ent.pack(fill = X , ipadx = 8 , pady = 8 , padx = 8 )

f1 = Frame(win , bg = "grey" )      #creating frames to pack buttons 
f1.pack()
f2 = Frame(win , bg = "grey")
f2.pack()
f3 = Frame(win , bg = "grey")
f3.pack()
f4 = Frame(win , bg = "grey")
f4.pack()
f5= Frame(win , bg = "grey")
f5.pack()

calcbutton()        # function calling to create buttons 

win.mainloop()
