# importing the tkinter module
from tkinter import *

# importing the pyperclip module to use it to copy our generated 
# password to clipboard
import pyperclip

# random module will be used in generating the random password
import random
# initializing the tkinter
root = Tk()

root.title("Password Generator")
root.config(padx=50, pady=50, bg='#aed6dc')
               

# setting the width and height of the gui
root.geometry("600x400")    # x is small case here
root['background']='#aed6dc'

# declaring a variable of string type and this variable will be 
# used to store the password generated
passstr = StringVar()

# declaring a variable of integer type which will be used to 
# store the length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)


# function to generate the password
def generate():
    # storing the keys in a list which will be used to generate 
    # the password 
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    # declaring the empty string
    password = ""

    # loop to generate the random password of the length entered           
    # by the user
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting the password to the entry widget
    passstr.set(password)

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)


# Creating a text label widget
Label(root, text="Password Generator", font="Georgia 24 ",bg='#aed6dc',fg="#4a536b").place(x=60,y=0)

# Creating a text label widget
Label(root, text="Enter password length:",font="Georgia ",bg = '#aed6dc').place(x=105,y=90)

# Creating a entry widget to take password length entered by the 
# user
Entry(root, textvariable=passlen,font="Geogia").place(x=290,y=90)

all_commands = lambda: [changeText(), generate()]
def changeText():  
    button['text'] = 'Password Generated'
button = Button(root,
	text = 'Generate Password',
	command = all_commands,bg='#ffffff', activebackground='#ff9a8d')  
button.place(x=290,y=130)     
Label(root,text="Password: ",font="Georgia",bg="#aed6dc").place(x=145,y=170)
# entry widget to show the generated password
Entry(root, textvariable=passstr,font = ("Geogia",24),bd=0,bg="#aed6dc",fg = "systembuttonface").place(x=290,y=170)
all_commands1 = lambda: [copytoclipboard()]
# button to call the copytoclipboard function
Button(root, text="Copy to clipboard", command=all_commands1,font = ("Helvetica",12), fg="#1e3d59").place(x=290,y=230)

# mainloop() is an infinite loop used to run the application when 
# it's in ready state 
root.mainloop()