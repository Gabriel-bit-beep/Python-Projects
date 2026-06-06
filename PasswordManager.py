# making a password generator
import random
# generating the dictonary to save the passwords with the websies the user wants to save
passwordManager = {

}

def createPassword(userLength):
    string = "123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()<>?:"
    password = ""
    for i in range(userLength):
        password += random.choice(string)
    return password

def updateManager(saved, password):
    global passwordManager
    passwordManager[saved] = password

def checkPassword(saved, password):
    specialChar = '!@#$%^&*()'
    if len(password) < 8 and len(password) > 24:
        print('Invalid password, Please try again \n\n')
        return
    

    for i in range(len(password)):
        if password[i] in specialChar:
            print('Password Accepted')
            updateManager(saved, password)
            return
    
    print('Password invalid, please try again \n\n')


def viewPasswords():
    global passwordManager

    if len(passwordManager) == 0:
        print('Currently nothing saved, Create a new Password')
        return

    for key, values in passwordManager.items():
        print(f'{key}: \"{values}\"')


print('Welcome to your password Manager! \nWhat would you like to do today? \n\n\n')

while True:
    print('1. Generate New Password? \n2. View Current Passwords \n3. Create New Password \n4. Quit')
    userInput = int(input('Enter: '))

    match userInput:
        case 1:
            try:
                userLength = int(input('Enter the length of which you would like the password to be: '))
                password = createPassword(userLength)
                print('where would you like to save this password to? ')
                saved = input('Enter: ')
                updateManager(saved, password)
            except ValueError:
                print('Invalid Choice, Please try again')

        case 2:
            print('Here\'s a list of your passwords saved: ')
            viewPasswords()

        case 3:
            print('Enter the password, must be a minimum length of 8 and at most 24, must contain special character')
            userInput = input('Enter: ')
            print('Where would you like to save this password to?')
            saved = input('Enter: ')
            checkPassword(saved, userInput)

    
        case 4:
            print('Thanks for stopping by!\n\n')
            break
        
        case _:
            print('Not a valid option, Please try again \n\n')
        
