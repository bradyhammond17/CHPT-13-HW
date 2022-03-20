
import tkinter
import tkinter.messagebox
from turtle import bgcolor

from click import command


class PizzaGUI:
    def __init__(self):
        #set up main window
        self.main_window = tkinter.Tk()
        self.main_window.geometry("400x200")
        self.main_window.title("Pizza Order")
        self.main_window.configure(bg="Blue")

        #create and pack frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.left_frame = tkinter.Frame(self.main_window)
        self.right_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.top_frame.pack(side="top")
        self.top_frame.configure(bg="Yellow")

        self.left_frame.pack(side="left")
        self.left_frame.configure(bg="Red")

        self.right_frame.pack(side="right")
        self.right_frame.configure(bg="Red")

        self.bottom_frame.pack(side="bottom")

        self.title_label = tkinter.Label(self.top_frame, text ="Brady's Pizzas")
        self.title_label.pack()
        self.title_label.configure(bg="Yellow")
        
        #create and pack name entry label and box
        self.name_label = tkinter.Label(self.top_frame, text="Enter your name:")
        self.name_entry = tkinter.Entry(self.top_frame, width=10)

        self.name_label.pack(side="left")
        self.name_label.configure(bg="Yellow")
        self.name_entry.pack(side="left")

        #create and pack checkboxes for toppings
        self.topping_label = tkinter.Label(self.left_frame, text="Choose your topping(s)")
        self.topping_label.pack()
        self.topping_label.configure(bg="Red")

        self.mushrooms_var = tkinter.IntVar()
        self.mushrooms = tkinter.Checkbutton(self.left_frame, text="Mushrooms ($0.59)", variable=self.mushrooms_var)
        self.mushrooms.pack()
        self.mushrooms.configure(bg="Red")

        self.pep_var = tkinter.IntVar()
        self.pepperoni = tkinter.Checkbutton(self.left_frame, text="Pepperoni ($0.69)", variable=self.pep_var)
        self.pepperoni.pack()
        self.pepperoni.configure(bg="Red")

        self.sausage_var = tkinter.IntVar()
        self.sausage = tkinter.Checkbutton(self.left_frame, text="Sausage ($0.79)", variable=self.sausage_var)
        self.sausage.pack()
        self.sausage.configure(bg="Red")

        self.mushrooms_var.set(0)
        self.pep_var.set(0)
        self.sausage_var.set(0)

        #create and pack radio buttons for crust
        self.radio_var = tkinter.IntVar()

        self.crust_label = tkinter.Label(self.right_frame, text="Choose your crust")
        self.crust_label.pack()
        self.crust_label.configure(bg="Red")

        self.thin_button = tkinter.Radiobutton(self.right_frame, text="Thin Crust ($10)", variable=self.radio_var, value=10)
        self.thin_button.pack()
        self.thin_button.configure(bg="Red")

        self.deep_button = tkinter.Radiobutton(self.right_frame, text="Deep Dish ($11)", variable=self.radio_var, value=11)
        self.deep_button.pack()
        self.deep_button.configure(bg="Red")

        self.thin_button.select()

        #create and pack calculate and quit buttons
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy, bg="Red")
        self.quit_button.pack(side="bottom")

        self.calc_button = tkinter.Button(self.main_window, text="Calculate Order", command= self.calculate, bg="Green")
        self.calc_button.pack(side="bottom")

       
        tkinter.mainloop()

        #create calculate function
    def calculate(self):
        total = 0
        if self.mushrooms_var.get() == 1:
            total += .59
        if self.pep_var.get() == 1:
            total += .69
        if self.sausage_var.get() == 1:
            total += .79
        total += self.radio_var.get()
        tkinter.messagebox.showinfo("Total", self.name_entry.get() + ", your total is $" + str(total))
        

pizza_gui = PizzaGUI()
