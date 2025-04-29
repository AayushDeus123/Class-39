from tkinter import *
from datetime import date

#Create window
root = Tk()
root.geometry('500x500')
root.title('Getting started with Widgets')

#Add widgets

#Add label
label = Label(text = 'Hey There!' , fg = 'white' , bg = 'Dark Blue')

#Add label for getting name as input from user
#Use entry widget to create a text box for user to enter their name
name_label = Label(text = 'Full Name' , bg = 'Red')
name_entry = Entry()

#Function to display a message
def display():
    #Read input given by the user
    name = name_entry.get()
    #Declaring a global variable to make it accessible anywhere in the program
    global message
    message = "Welcome to the application \nToday's date is : "
    greet = 'Hello ' +name+ '\n'
    
    #Display details in a text box
    #Specify where to add the details inside the text box
    text_box.insert(END , greet)
    text_box.insert(END , message)
    text_box.insert(END , date.today())
    
#Add a text widget to display information/messages
text_box = Text(height = 3)    

#Add button and give value of command as name of the function
#Press button, display function will be called automatically
button = Button(text = 'Begin' , command = display , height = 1 , bg = 'Beige')

#Organise all the widgets in the window
label.pack()
name_label.pack()
name_entry.pack()
button.pack()
text_box.pack()

root.mainloop()