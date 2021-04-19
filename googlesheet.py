import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

googlesheet_creds = os.environ.get('googlesheet_creds')
googlesheet_sheetId = os.environ.get('googlesheet_sheetId')
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(googlesheet_creds,scope)

client = gspread.authorize(creds)
workbook = client.open_by_key(googlesheet_sheetId)  # sheet id

sheet = workbook.worksheet("your worksheet")

data = pd.DataFrame(sheet.get_all_records())
print(data)

sheet.update_cell(2, 2, 'your value')
