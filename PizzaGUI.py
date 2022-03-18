import tkinter
import tkinter.messagebox


class PizzaGUI:
    def __init__(self):
        #set up main window
        self.main_window = tkinter.Tk()
        self.main_window.geometry("300x200")
        self.main_window.title("Pizza Order")
        
        #create and pack frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.right_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        #create and pack name entry label and box
        self.name_label = tkinter.Label(self.top_frame, text="Enter your name:")
        self.name_entry = tkinter.Entry(self.bottom_frame, width=10)

        self.name_label.pack(side="top")
        self.name_entry.pack(side="right")

        #create and pack checkboxes for toppings
        self.mushrooms_var = tkinter.IntVar()
        self.mushrooms = tkinter.Checkbutton(self.top_frame, text='Mushrooms', variable=self.mushrooms_var)
        self.mushrooms.pack()

        #create and pack calculate and quit buttons
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        self.quit_button.pack(side="bottom")
        tkinter.mainloop()


pizza_gui = PizzaGUI()
