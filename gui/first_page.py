first_page_frame = None

def switch_to_first_page(cur_page):
    cur_page.pack_forget()
    first_page_frame.pack()

def first_page_init():
    global first_page_frame

    first_page_frame = tk.Frame(gui.root)
    # first_page_frame.pack()

    adding_word_btn = tk.Button(first_page_frame, text="add words", command=lambda: awp.switch_to_add_word_page(first_page_frame), font=gui.custom_font)
    adding_word_btn.pack(pady=10)

    testing_btn = tk.Button(first_page_frame, text="test", command=lambda: tp.switch_to_test_page(first_page_frame), font=gui.custom_font)
    testing_btn.pack(pady=10)

    calendar_btn = tk.Button(first_page_frame, text="calendar", command=lambda: cp.switch_to_calendar_page(first_page_frame), font=gui.custom_font)
    calendar_btn.pack(pady=10)

import tkinter as tk
import gui.gui as gui
import gui.add_word_page as awp
import gui.test_page as tp
import gui.calendar_page as cp
from tkinter import messagebox
