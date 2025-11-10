import tkinter as tk
from tkinter import messagebox

# Function to display name and address
def show_info():
    name = "Kalen Collins" 
    address = "14265 271st Ave" 
    city_state_zip = "Harmony MN 55939"
    info = f"Name: {name}\nAddress: {address}\n{city_state_zip}"
    messagebox.showinfo("Personal Info", info)

# Create main window
window = tk.Tk()
window.title("Program #2 - Show Info")

# Create buttons
show_button = tk.Button(window, text="Show Info", command=show_info)
quit_button = tk.Button(window, text="Quit", command=window.quit)

# Layout buttons
show_button.pack(pady=10)
quit_button.pack(pady=10)

# Run the GUI loop
window.mainloop()
