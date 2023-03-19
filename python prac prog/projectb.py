import tkinter
from typing import ValuesView

root = tkinter.Tk()
root.title("BMI Calculator")
        
        
# Creatiing function(s)
def calculate_bmi():
    Weight_kg = float(entry_Weight_kg.get())
    Height_cm = float(entry_height_cm.get())
    Height_cm = Height_cm/100
    bmi = Weight_kg/(Height_cm**2)
    BMI = round(bmi, 2)
        

     
    label_result['text'] = f"BMI: {BMI}"
    
def printSomething():
    if(calculate_bmi>0):
        if(calculate_bmi<=16):
            c=("you are severely underweight")
        elif(calculate_bmi<=18.5):
            c=("you are underweight")
        elif(calculate_bmi<=25):
            c=("you are healthy")
        elif(calculate_bmi<=30):
            c=("you are overweight")
    else:("enter valid details")
    print(c)
    return(C)


# Creating GUI
label_Weight_kg = tkinter.Label(root, text="WEIGHT_KG: ")
label_Weight_kg.grid(column=0, row=0)

entry_Weight_kg = tkinter.Entry(root)
entry_Weight_kg.grid(column=1, row=0)

label_height_cm = tkinter.Label(root, text="HEIGHT_CM: ")
label_height_cm.grid(column=0, row=1)

entry_height_cm = tkinter.Entry(root)
entry_height_cm.grid(column=1, row=1)

button_calculate = tkinter.Button(root, text="Calculate", command=calculate_bmi)
button_calculate.grid(column=0, row=2)

button_print = tkinter.Button(root, text="Print Me", command=printSomething)
button_print.grid(column=0, row=3)

label_result = tkinter.Label(root, text="BMI: ")
label_result.grid(column=1, row=2)



root.mainloop()


