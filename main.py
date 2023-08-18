import gui.gui as gui
import sheets.sheets as sheets

def main():
    sheets.sheets_init()
    print("sheets init done")
    
    gui.gui_init()
    print("gui init done")

if __name__ == "__main__":
    main()