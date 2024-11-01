import secrets
import string
# GUI module I am using
import tkinter as tk
# This is used to make the slider horizontal
from tkinter import HORIZONTAL
# The two lines below were found on
# https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp
# They are used to stop the GUI from being blurry on Windows
from ctypes import windll
# Calling the below line here before creating the window
# Means the size of things in the window isn't shrunk
# it takes the parameter 2 as this makes sure it doesn't
# go blurry again if you have multiple monitors.
windll.shcore.SetProcessDpiAwareness(2)

# This function generates a password
# It takes in 4 parameters which are set using the buttons
# on the GUI
# It uses the secrets module to generate a password
# this is a more secure way of generating a password
# compared to using the random module
def gen_password(length, use_upper, use_numbers, use_symbols):
    # This is a string of all the lowercase letters
    characters = string.ascii_lowercase
    if use_upper:
        # Adds uppercase letters to the characters string
        # if the user checks the Upper Case box
        characters += string.ascii_uppercase
    if use_numbers:
        # Adds numbers to the characters string
        # if the user checks the Numbers box
        characters += string.digits
    if use_symbols:
        # Adds symbols to the characters string
        # if the user checks the symbols box
        characters += string.punctuation

    # This line picks random letters from the characters string and joins
    # them together to make the password. It does this for the chosen
    # password length (slider in GUI up to 60 characters)
    password = ''.join(secrets.choice(characters) for i in range(length))

    return password

# This class is the GUI for the password generator
# It includes a title, 3 checkbuttons for upper case, numbers and symbols
# A slider to choose the length of the password
# A button to generate the password
# A button to copy the password to the clipboard
# A label to display the generated password
class MyGUI:

    # This initialises the GUI
    def __init__(self):

        # tk.Tk() creates the window
        self.root = tk.Tk()
        # This sets the title of the window
        self.root.title("Password Generator")
        # This sets the size of the window
        self.root.geometry("1200x600")
        # This sets the background colour of the window
        self.root.configure(bg="light cyan")

        # This creates a label with the text "Password Generator", it
        # has other parameters that you can see below
        self.label = tk.Label(self.root, text="Password Generator", font=("Arial", 18), bg="light cyan")
        # This line puts the label in the window without this line the label
        # would not appear in the window
        self.label.pack(padx=10, pady=10)

        # This variable will store the value of the check_upper_case checkbutton
        # It is set to 0 if the checkbutton is not checked and 1 if it is checked
        self.check_Include_Upper_Case = tk.IntVar()
        # This variable will store the value of the check_numbers checkbutton
        # It is set to 0 if the checkbutton is not checked and 1 if it is checked
        self.check_Include_Numbers = tk.IntVar()
        # This variable will store the value of the check_symbols checkbutton
        # It is set to 0 if the checkbutton is not checked and 1 if it is checked
        self.check_Include_Symbols = tk.IntVar()

        # This variable will store the value of the slider
        # Which is the length of the password
        self.length_slider = tk.IntVar()

        # This creates a checkbutton with the text "Upper Case"
        self.check_upper_case = tk.Checkbutton(self.root, text="Upper Case", font=("Arial", 16), variable=self.check_Include_Upper_Case, bg="PaleTurquoise1")
        self.check_upper_case.pack(padx=10, pady=10)

        # Same logic as above
        self.check_numbers = tk.Checkbutton(self.root, text="Numbers", font=("Arial", 16), variable=self.check_Include_Numbers, bg="PaleTurquoise1")
        self.check_numbers.pack(padx=10, pady=10)

        # Same logic as above
        self.check_symbols = tk.Checkbutton(self.root, text="Symbols", font=("Arial", 16), variable=self.check_Include_Symbols, bg="PaleTurquoise1")
        self.check_symbols.pack(padx=10, pady=10)

        # This creates a slider with the text "Length of Password"
        # You can see activebackground is set to the same colour as the background
        # This is so the slider doesn't change colour when you click on it
        self.length_slider = tk.Scale(self.root, from_=1, to=60, font=("Arial", 16), orient=HORIZONTAL, bg="PaleTurquoise1", activebackground="PaleTurquoise1")
        self.length_slider.pack(padx=10, pady=10)

        # This creates a button with the text "Generate Password"
        # You can see activebackground is used again to keep the colour the same
        # when you click on it
        self.generate_pass_button = tk.Button(self.root, text="Generate Password", font=("Arial", 18), command=self.generate_password, bg="teal", activebackground="teal")
        self.generate_pass_button.pack(padx=10, pady=10)

        # This creates a button with the text "Copy"
        self.copy_button = tk.Button(self.root, text="Copy", font=("Arial", 18), command=self.copy_to_clipboard, bg="light blue", activebackground="light blue")
        self.copy_button.pack(padx=10, pady=10)

        # This creates a label with the text ""
        # This is where the generated password will be displayed
        self.output_password_label = tk.Label(self.root, text="", font=("Arial", 16), bg="PaleTurquoise1")
        self.output_password_label.pack(padx=10, pady=10)

        # This line makes the window appear
        self.root.mainloop()

    # This function generates the password
    def generate_password(self):
        # These lines get the values of the checkbuttons
        include_upper = self.check_Include_Upper_Case.get() == 1
        include_numbers = self.check_Include_Numbers.get() == 1
        include_symbols = self.check_Include_Symbols.get() == 1
        # This line gets the value of the slider which is the length of the password
        length_slider = self.length_slider.get()
        # This line generates the password using the parameters above
        # as they are passed into the gen_password function
        password = gen_password(length_slider, include_upper, include_numbers, include_symbols)
        # This line sets the text of the output_password_label to the generated password
        self.output_password_label.config(text=password)

    # This function copies the generated password to the clipboard
    def copy_to_clipboard(self):
        # This line gets the text of the output_password
        password = self.output_password_label.cget("text")
        # This line clears the clipboard in case something else is on it
        self.root.clipboard_clear()
        # This line adds the password to the clipboard
        self.root.clipboard_append(password)
        # This line updates the window
        self.root.update()

# This line creates an instance of the MyGUI class
# This is what makes the GUI appear
MyGUI()
