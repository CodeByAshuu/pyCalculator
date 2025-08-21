import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.configure(bg="#1E1E2F")  # Dark background

# Function to update time
def time():
    current_time = strftime('%H:%M:%S %p')  # 24-hour: %H:%M:%S, 12-hour: %I:%M:%S %p
    label.config(text=current_time)
    label.after(1000, time)  # Update every second

# Clock label
label = tk.Label(root, font=('Helvetica', 48, 'bold'), bg="#1E1E2F", fg="#E6E6FA")  # Soft lavender text
label.pack(anchor='center')

# Date label
date_label = tk.Label(root, font=('Helvetica', 18), bg="#1E1E2F", fg="#B0C4DE")  # Light steel blue
date_label.pack(anchor='s', pady=10)

def update_date():
    current_date = strftime('%A, %d %B %Y')
    date_label.config(text=current_date)
    date_label.after(60000, update_date)  # Update once per minute

# Start the clock
time()
update_date()
root.mainloop()
