from utils import textDisplay, options, file

#Get database (.txt file) If it doesn't exist, create one
databaseConnection = file.checkExistence(forceCreation=True)

#The options that will be displayed and their exec functions
menuOptions = [
    {
        "title": "Show registered people",
        "exec": options.showPeopleTab
    },
    {
        "title": "Register a new person",
        "exec": options.showRegisterPersonTab
    },
    {
        "title": "Leave system",
        "exec": ()
    }
]


#Main
if(databaseConnection):
    print("\033[92mSuccessfully connected to the database!\033[m")
    options.accessMenu(menuOptions)
else:
    textDisplay.line("THE PROGRAM WASN'T ABLE TO ACCESS THE DATABASE")
