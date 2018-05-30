import gspread
from oauth2client.service_account import ServiceAccountCredentials

def insert_row_gsheets(row, index = 2):
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('sandbox_credentias.json', scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open("Fondos_Colectivos_Bancolombia").sheet1
    sheet.insert_row(row, index)
