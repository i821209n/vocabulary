# import tkinter as tk
# from tkinter import messagebox

# def greet_user(entry_widget):
#     user_name = entry_widget.get()
#     if user_name:
#         greeting = f"Hello, {user_name}! Welcome to the GUI."
#         messagebox.showinfo("Greeting", greeting)
#     else:
#         messagebox.showwarning("Warning", "Please enter your name.")

# def main():
#     root = tk.Tk()
#     root.title("Welcome GUI")

#     # Create and place widgets
#     label = tk.Label(root, text="Enter your name:")
#     label.pack(pady=10)

#     name_entry = tk.Entry(root)
#     name_entry.pack(pady=5)

#     greet_button = tk.Button(root, text="Greet", command=lambda: greet_user(name_entry))
#     greet_button.pack(pady=10)

#     root.mainloop()

# if __name__ == "__main__":
#     main()

import tkinter as tk
from tkinter import messagebox
from tkinter import font

name_entry = None
page_1_frame = None
page_2_frame = None
name_entry_page_2 = None

def greet_user():
    user_name = name_entry.get()
    if user_name:
        greeting = f"Hello, {user_name}! Welcome to Page 1."
        messagebox.showinfo("Greeting", greeting)
    else:
        messagebox.showwarning("Warning", "Please enter your name.")

def switch_to_page_2():
    page_1_frame.pack_forget()
    page_2_frame.pack()

def greet_user_page_2():
    user_name = name_entry_page_2.get()
    if user_name:
        greeting = f"Hello, {user_name}! Welcome to Page 2."
        messagebox.showinfo("Greeting", greeting)
    else:
        messagebox.showwarning("Warning", "Please enter your name.")

def switch_to_page_1():
    page_2_frame.pack_forget()
    page_1_frame.pack()

def main():
    global name_entry, page_1_frame, page_2_frame, name_entry_page_2

    root = tk.Tk()
    root.title("Page Switching GUI")

    window_width = 800
    window_height = 600
    root.geometry(f"{window_width}x{window_height}")

    custom_font = font.Font(size=20)

    # Page 1
    page_1_frame = tk.Frame(root)
    page_1_frame.pack()

    label = tk.Label(page_1_frame, text="Enter your name:", font=custom_font)
    label.pack(pady=10)

    name_entry = tk.Entry(page_1_frame, font=custom_font, width=60)
    name_entry.pack(pady=5)

    greet_button = tk.Button(page_1_frame, text="Greet Page 1", command=greet_user, font=custom_font)
    greet_button.pack(pady=10)

    switch_button = tk.Button(page_1_frame, text="Switch to Page 2", command=switch_to_page_2, font=custom_font)
    switch_button.pack(pady=5)

    # Page 2
    page_2_frame = tk.Frame(root)

    label_page_2 = tk.Label(page_2_frame, text="Enter your name:")
    label_page_2.pack(pady=10)

    name_entry_page_2 = tk.Entry(page_2_frame)
    name_entry_page_2.pack(pady=5)

    greet_button_page_2 = tk.Button(page_2_frame, text="Greet Page 2", command=greet_user_page_2)
    greet_button_page_2.pack(pady=10)

    switch_button_page_2 = tk.Button(page_2_frame, text="Switch to Page 1", command=switch_to_page_1)
    switch_button_page_2.pack(pady=5)

    # Show Page 1 initially
    page_1_frame.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
