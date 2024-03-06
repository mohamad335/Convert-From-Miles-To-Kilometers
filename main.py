from tkinter import *
def calculate():
    mile = float(entry.get())
    km = mile*1.60934
    label1.config(text=f"{km}")

# Creating a new window and configurations
window = Tk()
window.title("Convert From Miles To Kilometer")
window.minsize(width=250, height=200)
window.config(padx=50, pady=50)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.place(x=100, y=0)

print(entry.get())

label = Label(text="Miles")
label.place(x=150, y=0)

label2 = Label(text="is equal to")
label2.place(x=40, y=20)

label1 = Label(text="0")
label1.place(x=100, y=20)

label3 = Label(text="Km")
label3.place(x=150,y=20)

button = Button(text="Calculate", command=calculate)
button.place(x=100, y=40)


window.mainloop()
