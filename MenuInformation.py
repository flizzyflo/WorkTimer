
from tkinter import messagebox

class MenuInformation:

    def show_menubar_information():
        messagebox.showinfo("About this application...", 
                            f"""This application was programmed in Python 3.10.2 by Florian Lübke.\nThis project is explicitly seen as freeware and can be provided to anyone who is interested in it.\nEnjoy tracking your work-time!""")

    def show_version_information(current_version_number: str):
        messagebox.showinfo("Changelog & Version information", 
        f"""-Current Version: {current_version_number}: Massive refactoring of the whole application. Made code more efficient and easier to maintain. Implementation of PomodoroClass.
        \n-Version 1.2: Added the possibility to export tracking into a .txt file which is stored at ones desktop. 
        \n Accessible via 'File -> Export working time to .txt. Changed the color-style of the application. Implemented the Pomodoro-Setting Checkbox to prepare for possible Pomodoro Counter update.'
        \n-Version 1.1: Added more interaktive Buttons and a light-system with yellow and red warning lightning to indicate whether one works too long. Merged the Start and Stop Button to an interactive button.
        \n-Version 1.0: Initial creation of the whole application.""")