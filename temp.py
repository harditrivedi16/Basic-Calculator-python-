

import tkinter as tk
print(tk.TkVersion)

def display_text():
    text_field.delete(0, tk.END)  # Clear any existing text
    text_field.insert(0, "Hello World")  # Insert 'Hello World'

# Set up the main window
root = tk.Tk()
root.title("Hello World App")

# Create a text field with customized font and background color
text_field = tk.Text(root, width=20, font=("Arial", 14), bg="lightblue")
text_field.pack(pady=10)

# Create a button
button = tk.Button(root, text="Click Me", command=display_text, font=("Arial", 12))
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
