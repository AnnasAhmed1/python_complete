from tkinter import *
import time
import random
import tkinter.messagebox

root =Tk()

root.title("Restaurant Billing System")
root.configure(background='sky blue')

Tops = Frame(root, bg='dark blue', bd=25, pady=20)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('calibri', 30, 'bold'), text='FRESH JUICE CORNER', bd=15, bg='sky blue',
                fg='blue', justify=CENTER)
lblTitle.grid(row=0)

ReceiptCal_Function = Frame(root, bg='dark blue', bd=10, relief=GROOVE)
ReceiptCal_Function.pack(side=LEFT)

Buttons_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=3, relief=GROOVE)
Buttons_Function.pack(side=TOP)

Bill_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=6, relief=GROOVE)
Bill_Function.pack(side=BOTTOM)

Receipt_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=4, relief=GROOVE)
Receipt_Function.pack(side=BOTTOM)


MenuFrame = Frame(root, bg='sky blue')
MenuFrame.pack(side=RIGHT)
Total_Function = Frame(MenuFrame, bg='sky blue')
Total_Function.pack(side=BOTTOM)
Drinks_Function = Frame(MenuFrame,bg='sky blue')
Drinks_Function.pack(side=TOP)


Drinks_Function = Frame(MenuFrame, bg='sky blue')
Drinks_Function.pack(side=LEFT)
Food_Function = Frame(MenuFrame, bg='sky blue')
Food_Function.pack(side=RIGHT)
# variables

variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()
variable5 = IntVar()
variable6 = IntVar()
variable7 = IntVar()
variable8 = IntVar()
variable9 = IntVar()
variable10 = IntVar()
variable11 = IntVar()
variable12 = IntVar()
variable13 = IntVar()
variable14 = IntVar()
variable15 = IntVar()
variable16 = IntVar()

Date_of_Order = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()

TotalCost = StringVar()
ServiceCharge = StringVar()
text_Input = StringVar()
operator = ""


hot_chocolate = StringVar()
orange_juice = StringVar()
milkshake = StringVar()
sting = StringVar()
hot_chocolate.set("0")
orange_juice.set("0")
milkshake.set("0")
sting.set("0")



Date_of_Order.set(time.strftime("%d/%m/%y"))

# Function Declaration

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    
    TotalCost.set("")
    
    
    ServiceCharge.set("")
    textReceipt.delete("1.0", END)


    
    hot_chocolate.set("0")
    orange_juice.set("0")
    milkshake.set("0")
    
    sting.set("0")
    
    
    variable1.set(0)
    variable2.set(0)
    variable3.set(0)
    variable4.set(0)
    variable5.set(0)
    variable6.set(0)
    variable7.set(0)
    variable8 .set(0)
    variable9 .set(0)
    variable10 .set(0)
    variable11 .set(0)
    variable12 .set(0)
    variable13 .set(0)
    variable14 .set(0)
    variable15 .set(0)
    variable16 .set(0)


    textHotChocolate.configure(state=DISABLED)
    textOrangeJuice.configure(state=DISABLED)
    textMilkShake.configure(state=DISABLED)
    textSting.configure(state=DISABLED)

def TotalofUnit():
    Unit3 = float(hot_chocolate.get())
    Unit4 = float(orange_juice.get())
    Unit5 = float(milkshake.get())
    Unit7 = float(sting.get())
    
    Prices_Drinks =   (Unit3 * 60) + (Unit4 * 35) + (Unit5 * 70)  + (Unit7 * 55) 
    DrinksPrices = "P" + str('%.2f' % Prices_Drinks)
    SC = "P" + str('%.2f' % 1.59)
    ServiceCharge.set(SC)
    Tax = "P" + str('%.2f'%((Prices_Drinks) * 0.15))
    PaidTax.set(Tax)

    TT = ((Prices_Drinks ) * 0.15)
    TC = "P" + str('%.2f'%(Prices_Drinks  + TT))
    TotalCost.set(TC)

def drinksHotChocolate():
    if variable3.get() == 1:
        textHotChocolate.configure(state=NORMAL)
        textHotChocolate.delete('0', END)
        textHotChocolate.focus()
    elif variable3.get() == 0:
        textHotChocolate.configure(state=DISABLED)
        hot_chocolate.set("0")

def drinksOrangeJuice():
    if variable4.get() == 1:
        textOrangeJuice.configure(state=NORMAL)
        textOrangeJuice.delete('0', END)
        textOrangeJuice.focus()
    elif variable4.get() == 0:
        textOrangeJuice.configure(state=DISABLED)
        orange_juice.set("0")

def drinksMilkShake():
    if variable5.get() == 1:
        textMilkShake.configure(state=NORMAL)
        textMilkShake.delete('0', END)
        textMilkShake.focus()
    elif variable5.get() == 0:
        textMilkShake.configure(state=DISABLED)
        milkshake.set("0")

def drinksSting():
    if variable7.get() == 1:
        textSting.configure(state=NORMAL)
        textSting.delete('0', END)
        textSting.focus()
    elif variable7.get() == 0:
        textSting.configure(state=DISABLED)
        sting.set("0")

def Receipt():
    textReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("Bill" + randomRef)
    
    textReceipt.insert(END, 'Receipt Ref:\t\t\t'+Receipt_Ref.get() + '\t' + Date_of_Order.get() + '\n')
    textReceipt.insert(END, 'Unit\t\t\t\t'+"Total of Unit \n")
    textReceipt.insert(END, 'Hot Chocolate:\t\t\t\t\t' + hot_chocolate.get()+'\n')
    textReceipt.insert(END, 'Orange Juice:\t\t\t\t\t' + orange_juice.get()+'\n')
    textReceipt.insert(END, 'Milk Shake:\t\t\t\t\t' + milkshake.get()+'\n')
    textReceipt.insert(END, 'Sting:\t\t\t\t\t' + sting.get()+'\n')
    textReceipt.insert(END, 'Total Cost:\t\t\t\t' +str(TotalCost.get())+"\n")

# Drinks
HotChocolate = Checkbutton(Drinks_Function, text='Hot Chocolate', variable=variable3, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksHotChocolate).grid(row=2, sticky=W)

OrangeJuice = Checkbutton(Drinks_Function, text='Orange Juice', variable=variable4, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksOrangeJuice).grid(row=3, sticky=W)
MilkShake = Checkbutton(Drinks_Function, text='Milk Shake', variable=variable5, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksMilkShake).grid(row=4, sticky=W)
Sting = Checkbutton(Drinks_Function, text='Sting', variable=variable7, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksSting).grid(row=6, sticky=W)

# Drink Entry
textHotChocolate = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=hot_chocolate)
textHotChocolate.grid(row=2,column=1)

textOrangeJuice= Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=orange_juice)
textOrangeJuice.grid(row=3,column=1)

textMilkShake = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=milkshake)
textMilkShake.grid(row=4,column=1)
textSting = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=sting)
textSting.grid(row=6,column=1)


# ToTal Cost

lblServiceCharge=Label(Total_Function,font=('arial',14,'bold'),text='Service Charge',bg='sky blue',fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
# Payment information

lblPaidTax=Label(Total_Function,font=('arial',14,'bold'),text='\tPaid Tax',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
textPaidTax=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=PaidTax)
textPaidTax.grid(row=0,column=3)

lblTotalCost=Label(Total_Function,font=('arial',14,'bold'),text='\tTotal',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
textTotalCost=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=TotalCost)
textTotalCost.grid(row=2,column=3)

# RECEIPT
textReceipt=Text(Receipt_Function,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
textReceipt.grid(row=0,column=0)

# BUTTONS
buttonTotal=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Total',bg='black',command=TotalofUnit).grid(row=0,column=0)
buttonReceipt=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Receipt',bg='black',command=Receipt).grid(row=0,column=1)
buttonReset=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Reset',bg='black',command=Reset).grid(row=0,column=2)
buttonExit=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Exit',bg='black',command=iExit).grid(row=0,column=3)

root.mainloop()

