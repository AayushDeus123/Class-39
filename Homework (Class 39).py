from tkinter import *

def display():
    num1 = int(label1_entry.get())
    num2 = int(label2_entry.get())
    product = num1 * num2
    text_box.insert(END, f"Product: {product}")

window = Tk()
window.geometry('300x400')
window.title('Getting Started with Widgets')

label = Label(text='This program multiplies two numbers!', fg='white', bg='red')
label1 = Label(text='Enter 1st Number', bg='light blue')
label1_entry = Entry()

label2 = Label(text='Enter 2nd Number', bg='light blue')
label2_entry = Entry()

button = Button(text='Calculate!', command=display, bg='beige')

text_box = Text(height=3, width=25)

# Pack all widgets at the end
label.pack(pady=5)
label1.pack()
label1_entry.pack()
label2.pack()
label2_entry.pack()
button.pack(pady=10)
text_box.pack()

window.mainloop()