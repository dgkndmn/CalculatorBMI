from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300 , height=300)


label1 = Label(text="Enter Your Weight (kg)")
label1.config()
label1.pack()

entry1 = Entry(width=20)
entry1.pack()

label2 = Label(text="Enter Your Height (cm)")
label2.place(x=78,y=80)


entry2 = Entry(width=20)
entry2.place(x=55,y=100)

def button_clicked():
    kilo = float(entry1.get())
    boy = float(entry2.get())
    metreboy = (boy / 100)
    print(f"Boyunuz(cm): {metreboy}\nKilonuz: {kilo}")
    endeks = kilo / (metreboy*metreboy)
    formatli_sayi = "{:.2f}".format(endeks)
    if(endeks>25):
        label3 = Label(text=f"Your BMI is {formatli_sayi}. You are over-weight.")
        label3.place(x=30, y=250)
    elif(18.5 < endeks < 24.9):
        label3 = Label(text=f"Your BMI is {formatli_sayi}. You are normal weight.")
        label3.place(x=30, y=250)
    else:
        label3 = Label(text=f"Your BMI is {formatli_sayi}. You are light-weight.")
        label3.place(x=30, y=250)


newbutton = Button(text="Calculate",command=button_clicked)
newbutton.place(x=100,y=130)

window.resizable(width=False, height=False)



window.mainloop()