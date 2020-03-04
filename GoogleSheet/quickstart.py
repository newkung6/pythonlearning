import gspread , sys
from oauth2client.service_account import ServiceAccountCredentials

#fix
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)

client = gspread.authorize(creds)

#inputData on console
# info = input("Insertdata(splitby\".\"):")
# Check = info.split('.')

# #input command
Check = sys.argv
del Check[0]

print(Check)
#set Sheet
sheet = client.open('Test').sheet1
lastcol = (len(sheet.col_values(1))+ 1)

sheet.insert_row(Check,lastcol)


#access data
# print( sheet.get_all_records())
# print(sheet.row_values(2))
# print(sheet.col_values(1))
# print(sheet.cell(2,1).value)

# insert data
# sheet.insert_row([Name,SSS,Income],2)
# sheet.insert_row([Name,SSS,Income],lastcol)

# delete row
#sheet.delete_row(4)

#update cell
#sheet.update_cell(3,1,"Bobcat")

#findcell and list
# cell_list =sheet.findall("1300")
# for cell in cell_list:
#     print(cell.value)
#     print(cell.row)
#     print(cell.col)