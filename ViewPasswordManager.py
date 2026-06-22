import tkinter as tk
from tkinter import ttk
import random

# have a global dictonary to store all the users saved passwords and websites to save it into
passwordManager = {}

#define a function to delete all the widgets once a new option has been chosen
def clearContent():
    for widgets in contentFrame.winfo_children():
        widgets.destroy()

# this creates a random generated password based on the users length of password
def createPassword():
    string = "123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()<>?:"
    password = ""
    for i in range(16):
        password += random.choice(string)
    return password

# this function just updates the global dictonary to save new passwords and where they want to be saved
def updateManager(saved, password):
    global passwordManager
    passwordManager[saved] = password

# this checks the new users password and checks to ensure it's valid
def checkPassword(saved, password):
    specialChar = '!@#$%^&*()'
    if len(password) < 8 or len(password) > 24:
        return False
    for i in range(len(password)):
        if password[i] in specialChar:
            updateManager(saved, password)
            return True
    return False

# just creates a new label for each websites and password stores in the dictonary.
def viewPasswords():
    global passwordManager
    if len(passwordManager) == 0:
        tk.Label(contentFrame, text='Currently nothing saved, Create a new Password').pack()
        return
    for key, value in passwordManager.items():
        tk.Label(contentFrame, text=f'Saved: {key}: "{value}"').pack()


def changePassword():
    global passwordManager

    if len(passwordManager) == 0:
        tk.Label(contentFrame, text='You currently don\'t have anything saved at the moment').pack()
        return

    tk.Label(contentFrame, text='Select The website you would like to change the password to').pack()

    combo = ttk.Combobox(contentFrame, values=list(passwordManager.keys()))
    combo.pack(pady=5)

    def select(event):
        selected_item = combo.get()
        tk.Label(contentFrame,text='What would you like your new password to be?').pack()
        entry = tk.Entry(contentFrame)
        entry.pack(pady=5)

        def save():
            newPassword = entry.get()
            valid = checkPassword(selected_item,newPassword)

            if valid == True:
                tk.Label(contentFrame, text='Successfully saved new Password').pack()
            else:
                tk.Label(contentFrame, text='Invalid password, Must have a special char and must be > 8 and < 24').pack()

        tk.Button(contentFrame, text='Save', command=save).pack(pady=5)
    
    combo.bind('<<ComboboxSelected>>', select)


# this will build the ui for the password that the user chooses to create.
def createPasswordUI():
    label = tk.Label(contentFrame, text='Password Must be at least 8 char, and must have a special char')
    label.pack()
    entry = tk.Entry(contentFrame)
    entry.pack(pady=5)
    label2 = tk.Label(contentFrame, text='Where would you like to save this password to?')
    label2.pack()
    entry2 = tk.Entry(contentFrame)
    entry2.pack(pady=6)
    label3 = tk.Label(contentFrame, text='')
    label3.pack()

    # this is a function within a function, we do this to just check to see once the button to save the password in the dictonary
    # we must then check to see if it's valid
    def generate():
        password = entry.get()
        saved = entry2.get()
        if checkPassword(saved, password):
            label3.config(text='Password saved successfully!')
        else:
            label3.config(text='Invalid password! Min 8 chars, max 24, needs a special char.')

    tk.Button(contentFrame, text="Save Password", command=generate).pack(pady=5)

# generates the labels and buttons
def generatePasswordUI():
    label2 = tk.Label(contentFrame, text='Where would you like to save this password to?')
    label2.pack()
    entry2 = tk.Entry(contentFrame)
    entry2.pack(pady=6)
    label3 = tk.Label(contentFrame, text='')
    label3.pack()

    # for the button to generate the generated password for the user
    def generate():
        try:
            newPassword = createPassword()
            updateManager(entry2.get(), newPassword)
            label3.config(text=f'Generated: \"{newPassword}\"')
        except ValueError:
            label3.config(text='Please enter a valid number!')

    tk.Button(contentFrame, text="Generate", command=generate).pack(pady=5)

# this is for the box UI so that the user can select what they would like to do
def select(event):
    selected_item = combo_box.get()

    #call first to select a new Ui and get rid of old widgets.
    clearContent()

    if selected_item == 'Generate new Password':
        generatePasswordUI()
    elif selected_item == 'Create New Password':
        createPasswordUI()
    elif selected_item == 'View Passwords':
        viewPasswords()
    elif selected_item == 'Change Password':
        changePassword()
    elif selected_item == 'Quit':
        root.destroy()

# basic set up for the ui page.
root = tk.Tk()
root.geometry("500x500")

tk.Label(root, text='Welcome To Password Manager!\n').pack()
tk.Label(root, text='What would you like to do today?').pack()

combo_box = ttk.Combobox(
    root,
    values=['Generate new Password', 'Create New Password', 'View Passwords', 'Change Password', 'Quit']
)
combo_box.pack(pady=5)
combo_box.bind('<<ComboboxSelected>>', select)

# building a sepereate root so that with some ui's we can get rid of them to make space for the new ui
contentFrame = tk.Frame(root)
contentFrame.pack()

root.mainloop()