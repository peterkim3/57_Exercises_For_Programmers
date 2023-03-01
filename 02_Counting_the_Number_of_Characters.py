# inputString = input("What is the input string? ")
# if not len(inputString) == 0:
#     print(f"{inputString} has {len(inputString)} characters")
# else:
#     print(f"Please enter something into the program!")

    
"""
Challenges
Implement this program using a graphical user interface
and update the character counter every time a key is
pressed. If your language doesn’t have a particularly
friendly GUI library, try doing this exercise with HTML
and JavaScript instead.
"""

from tkinter import *

window = Tk()
window.title("My GUI Window")  # 윈도우 이름

def button_pressed():
    label_inputStr["text"] = f"The Length of input String is : {len(entry.get())}"
    label_inputStr["bg"] = "burlywood1"
    label_lenStr["text"] = entry.get()
    label_lenStr["bg"] = "burlywood1"
    entry.delete(0, END)
    
entry = Entry(
    master=window, fg="black", bg="yellow", width=30, justify=CENTER, font=("Arial", 25)
)

label_lenStr = Label(window, text="The Length of the Input String", font=("Arial", 25))
label_inputStr = Label(window, text="Input String will be displayed", font=("Arial", 25))

button = Button(
    master=window,
    text="Enter",
    bg="white",
    fg="blue",
    width=80,
    height=2,
    command=button_pressed,
)

label_lenStr.pack()
label_inputStr.pack()
button.pack()
entry.pack()
    
window.mainloop()