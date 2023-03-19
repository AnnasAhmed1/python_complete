import tkinter
top=tkinter.Tk()
b1=tkinter.Button(text="1",command = 1 , width=2)
b1.grid(column=1 ,row=1)
b2=tkinter.Button(text="2",command = 2 , width=2)
b2.grid(column=2 ,row=1)
b3=tkinter.Button(text="3",command = 3 , width=2)
b3.grid(column=3 ,row=1)
b4=tkinter.Button(text="4",command = 4 , width=2)
b4.grid(column=1 ,row=2)
b5=tkinter.Button(text="5",command = 5 , width=2)
b5.grid(column=2 ,row=2)
b6=tkinter.Button(text="6",command = 6 , width=2)
b6.grid(column=3 ,row=2)
b7=tkinter.Button(text="7",command = 7 , width=2)
b7.grid(column=1 ,row=3)
b8=tkinter.Button(text="8",command = 8 , width=2)
b8.grid(column=2 ,row=3)
b9=tkinter.Button(text="9",command = 9 , width=2)
b9.grid(column=3 ,row=3)
b0=tkinter.Button(text="0",command = 0 , width=2)
b0.grid(column=1 ,row=4)
ba=tkinter.Button(text="+", command = 0 , width=2, height=4)
ba.grid(column=4 ,row=4)
bs=tkinter.Button(text="-",command = 0 , width=2)
bs.grid(column=5,row=4)
bm=tkinter.Button(text="*",command = 0 , width=2)
bm.grid(column=4 ,row=3)
bd=tkinter.Button(text="/",command = 0 , width=2)
bd.grid(column=5 ,row=3)







top.mainloop()
