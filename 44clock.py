from time import strftime
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title(" Digital Clock")

# Label for time display
label = tk.Label(root, font=("Arial", 60, "bold"), bg="black", fg="cyan")
label.pack(anchor="center")

# Function to update time
def time():
    string = strftime("%H:%M:%S %p")  # Hour:Minute:Second AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update every second

time()
root.mainloop()
