test_page_frame = None

def switch_to_test_page(cur_page):
    cur_page.pack_forget()
    test_page_frame.pack()

def test_page_init():
    global test_page_frame

    test_page_frame = tk.Frame(gui.root)

    choice_test = tk.Button(test_page_frame, text="choice test", command=lambda: ctp.switch_to_choice_test_page(test_page_frame), font=gui.custom_font)
    choice_test.pack(pady=10)

    spell_test = tk.Button(test_page_frame, text="spell test", command=lambda: stp.switch_to_spell_test_page(test_page_frame), font=gui.custom_font)
    spell_test.pack(pady=10)

    back_btn = tk.Button(test_page_frame, text="back", command=lambda: fp.switch_to_first_page(test_page_frame), font=gui.custom_font)
    back_btn.pack(pady=10)

import tkinter as tk
import gui.gui as gui
import gui.choice_test_page as ctp
import gui.spell_test_page as stp
import gui.first_page as fp
