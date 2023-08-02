#import
import tkinter as tk
from tkinter import font

#variables
root = None
custom_font = None
first_page_frame = None
add_word_page_frame = None
test_page_frame = None
calendar_page_frame = None

def switch_to_adding_word_page():
    first_page_frame.pack_forget()
    add_word_page_frame.pack()

def switch_to_testing_page():
    first_page_frame.pack_forget()
    test_page_frame.pack()

def switch_to_calendar_page():
    first_page_frame.pack_forget()
    calendar_page_frame.pack()

def switch_to_first_page(cur_page):
    cur_page.pack_forget()
    first_page_frame.pack()

def save_word():
    print("save the word!!")

def first_page_init():
    global first_page_frame

    first_page_frame = tk.Frame(root)
    first_page_frame.pack()

    adding_word_btn = tk.Button(first_page_frame, text="add words", command=switch_to_adding_word_page, font=custom_font)
    adding_word_btn.pack(pady=10)

    testing_btn = tk.Button(first_page_frame, text="test test", command=switch_to_testing_page, font=custom_font)
    testing_btn.pack(pady=10)

    calendar_btn = tk.Button(first_page_frame, text="calendar", command=switch_to_calendar_page, font=custom_font)
    calendar_btn.pack(pady=10)

def add_word_page_init():
    global add_word_page_frame

    add_word_page_frame = tk.Frame(root)
    add_word_page_frame.pack()

    word_label = tk.Label(add_word_page_frame, text="Enter a word:", font=custom_font)
    word_label.pack(pady=10)

    definition_label = tk.Label(add_word_page_frame, text="Enter the definition:", font=custom_font)
    definition_label.pack(pady=10)

    sentence_label = tk.Label(add_word_page_frame, text="Enter a example:", font=custom_font)
    sentence_label.pack(pady=10)

    save_btn = tk.Button(add_word_page_frame, text="save", command=save_word, font=custom_font)
    save_btn.pack(pady=10)

    back_btn = tk.Button(add_word_page_frame, text="back", command=lambda: switch_to_first_page(add_word_page_frame), font=custom_font)
    back_btn.pack(pady=10)

def gui_init():
    global root, custom_font

    root = tk.Tk()
    root.title("Vocabulary Application")

    window_width = 800
    window_height = 600
    root.geometry(f"{window_width}x{window_height}")

    custom_font = font.Font(size=20)

    # first page
    first_page_init()
    # add word page 
    add_word_page_init()

    # Show Page 1 initially
    first_page_frame.pack()

    root.mainloop()