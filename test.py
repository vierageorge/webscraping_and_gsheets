import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('sandbox_credentias.json', scope)
gc = gspread.authorize(credentials)
sheet = gc.open("Fondos_Colectivos_Bancolombia").sheet1
row = ["Row2","Row2","Row2","Row2","Row2","Row2","Row2","Row2","Row2","Row2","Row2","Row2",]
index = 2
sheet.insert_row(row, index)
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
