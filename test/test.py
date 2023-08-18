import pygsheets

auth_file = "google_key.json"
gc = pygsheets.authorize(service_file = auth_file)

# setting sheet
sheet_url = "https://docs.google.com/spreadsheets/d/1X8eoI34Mj5ULdyJ03lhBuhW1yPFmj7ZfkwUCdJDDN9M/" 
sheet = gc.open_by_url(sheet_url)

sheet_test01 = sheet.worksheet_by_title("test01")

# add a new worksheet
worksheet = sheet.add_worksheet(title="test02", rows=1000, cols=20)

# read
A1 = sheet_test01.cell('A1')
print(A1)
print(A1.value)

# write
sheet_test01.update_value('A2', "test_A2") # 單一個
sheet_test01.update_values('B2', [['A', 'B', 'C', 'D']]) # 橫的
sheet_test01.update_values('A3', [['3'],['4'],['5'],['6']]) # 直的

# insert
col = 1
sheet_test01.insert_cols(col, number=3) # add 2, 3, 4 (B, C, D)

row = 1
sheet_test01.insert_rows(row, number=3) # add 2, 3, 4

# insert with values
values = [['M', 'N', 'O']] # matrix
insert_rows = 1 # add start from 2
sheet_test01.insert_rows(insert_rows, number=1, values=values) 


# append
values = [['X', 'Y', 'Z']] # matrix
sheet_test01.append_table(values=values) 


class google_sheet_helper:
    def __init__(self, sheet_name = "work01"):
        # setting sheet        
        self.working_sheet = global_sheet.worksheet_by_title(sheet_name)

    def write(self, position = "A1", content = "test"):    
        self.working_sheet.update_value(position, content)

    def read(self, position = "A1"):
        content = self.working_sheet.cell(position)
        print(content)
        print(content.value)

    def append(self, values = []):
        self.working_sheet.append_table(values=values) 

    def insert(self, insert_rows = 1, values = []): # insert_rows = 1, start from 2
        self.working_sheet.insert_rows(insert_rows, number=1, values=values) 
