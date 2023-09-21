import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('filename.json', scope) # type your json file name here

# Authenticate with Google Sheets API
gc = gspread.authorize(credentials)

# Open the Google Sheets document by its title
spreadsheet = gc.open('title')

# Select the worksheet by its title
worksheet = spreadsheet.worksheet('Sheet1')  # Replace 'Sheet1' with your sheet name

# Extract data from your CSV file
import pandas as pd
csv_file = 'pagedata.csv'
data = pd.read_csv(csv_file)

# Convert the data to a list of lists
data_values = data.values.tolist()

# Append the data to Google Sheets
worksheet.append_rows(data_values)

print("Data appended to Google Sheets successfully!")

