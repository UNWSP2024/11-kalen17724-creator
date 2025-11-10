import tkinter as tk 

class GUI:
    def __init__(self):
        self.main_window = tk.Tk()

        self.label = tk.Label(self.main_window, 
                                text = "If you're ready to lose you've already lost.", 
                                borderwidth = 5, 
                                relief = 'groove')
        self.label.pack(ipadx=20, ipady=20)

        tk.mainloop()
gui = GUI() 
