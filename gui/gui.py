#variables
root = None
custom_font = None

def gui_init():
    global root, custom_font

    root = tk.Tk()
    root.title("Vocabulary Application")

    window_width = 800
    window_height = 600
    root.geometry(f"{window_width}x{window_height}")

    custom_font = font.Font(size=20)

    # first page
    fp.first_page_init()
    # add word page 
    awp.add_word_page_init()
    # test page
    tp.test_page_init()
    # choice test page
    ctp.choice_test_page_init()

    # Show first page initially
    fp.first_page_frame.pack()

    root.mainloop()

# import
import tkinter as tk
import sheets.sheets as sheets
import gui.first_page as fp
import gui.add_word_page as awp
import gui.test_page as tp
import gui. choice_test_page as ctp
from tkinter import font
from tkinter import messagebox
