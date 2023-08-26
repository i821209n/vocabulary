import pygsheets
import datetime

global_sheet = None
add_word_sheet= None
word_id = 0

def sheets_init():
    global global_sheet

    auth_file = "google_key.json"
    gc = pygsheets.authorize(service_file = auth_file)

    # setting sheet
    sheet_url = "https://docs.google.com/spreadsheets/d/1X8eoI34Mj5ULdyJ03lhBuhW1yPFmj7ZfkwUCdJDDN9M/" 
    global_sheet = gc.open_by_url(sheet_url)

    add_word_sheet_init()

class google_sheet:
    def __init__(self, sheet_name):
        try:
            self.working_sheet = global_sheet.worksheet_by_title(sheet_name)
        except:
            self.working_sheet = global_sheet.add_worksheet(title=sheet_name, rows=1000, cols=20)
        self.title = sheet_name

    def write(self, position = "A1", content = "test"):    
        self.working_sheet.update_value(position, content)

    def read(self, position):
        # print(position)
        content = self.working_sheet.cell(position)
        # print(content)
        return content.value

    def append(self, values = []):
        try:
            self.working_sheet.append_table(values=values) 
        except:
            print("append fail")

    def insert(self, insert_rows = 1, values = []): # insert_rows = 1, start from 2
        self.working_sheet.insert_rows(insert_rows, number=1, values=values) 

    def get_title(self) -> str:
        return self.title
    
    def get_col(self, row_num):
        return self.working_sheet.get_col(row_num)

def add_word_sheet_init():
    global add_word_sheet, word_id
    current_time = datetime.datetime.now()
    sheet_title = "word"+str(current_time.year)+str(current_time.month).zfill(2)
    print(f"file name:{sheet_title}")   
    if(add_word_sheet != None and sheet_title == add_word_sheet.get_title()):
        print("sheet title is equal")
    else:
        print("sheet title is not equal")
        add_word_sheet = google_sheet(sheet_title)
        print("get working sheet title:", add_word_sheet.get_title())

    # Get all the values of the desired column (e.g., column A)
    column_values = add_word_sheet.get_col(1)  # Replace 1 with the column number you want (1 for column A, 2 for column B, and so on)
    # Get the last cell value (last element of the list)
    for value in column_values:
        if (value == ""):
            break
        word_id = int(value)
    print(f"word id: {word_id}")

def save_word(word, definition, sentence):
    global word_id  
    if(add_word_sheet != None):
        word_id += 1
        ready_to_save = [word_id, word, definition, sentence]
        add_word_sheet.append(ready_to_save)       
    else:
        print("add word sheet has not initialized")

def get_word_num():
    return word_id

def get_word(id):
    return add_word_sheet.read("B"+str(id))

def get_definition(id):
    return add_word_sheet.read("C"+str(id))

def get_example(id):
    return add_word_sheet.read("D"+str(id))