from tkinter import *

window = Tk()
window.title("My First GUI in Python")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# side = "bottom/left", expand=True
my_label.pack()
# configure label
my_label.config(text="My Label")

# Entry

input = Entry(width=15)
input.pack()


# Button


def button_clicked():
    print("I am clicked")
    new_label = input.get()
    my_label.config(text=new_label)


button = Button(text="Click Me", command=button_clicked)
button.pack()


#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

'''
POSITIONING LAYOUT
1) PACK()
Starts from top center(default) of the page and packs each element below each other
We can change the starting point using "side=left/top/right/bottom" argument
For example, if I select left, Pack() puts all the elements in order from left to right

2) PLACE()
Place is all about precise positioning.
my_label.place(x=0, y=0) => Top-left corner

3) GRID()
Divides the window into grids as "row and columns"
my_label.grid(column=0, grid=0)
button.grid(column=1, grid=1)
entry.grid(column=2, grid=2)

!!!We can not mix  GRID() and PACK()

=> We also can add "PADDING" to our layout using window.config(padx=10, pady=15)


'''



'''
# *args
# *args means we can add unlimited arguments to a method
# Returns a tuple
def add(*args):
    return sum(args)

total = add(4, 8, 3, 5, 6)
print(total)

# **kwargs
# using **kwargs we name the arguments as "key and value" pairs
# Returns a dictionary


def PersonnelInfo(**kwargs):
    print(kwargs)


PersonnelInfo(name="John", surname="Doe", age=45)

'''


# DAY_27 PROJECT => Mile to KM Converter GUI
from tkinter import *
win = Tk()
win.title("Mile to Km. Converter")
win.minsize(width=300, height=250)
win.config(padx=2, pady=15)
mile = Entry(width=5)
mile.place(x=160, y=30)


def button_click():
    mile_value = float(mile.get())
    km_value = mile_value * 1.6
    label3.config(text=km_value)


button = Button(text="Convert", command=button_click)
button.place(x=150, y=110)

label1 = Label(text="Miles") # Miles
label1.place(x=160, y=60)

label2 = Label(text="is equal to") # is equal to
label2.place(x=100, y=80)

label3 = Label(text="") # Empty at the start.
label3.place(x=170, y=80)

label4 = Label(text="Km.") # Km
label4.place(x=210, y=80)

win.mainloop()
