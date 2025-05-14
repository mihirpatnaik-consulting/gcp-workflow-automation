import os
import gspread
from google.oauth2.service_account import Credentials

# Set up Google Cloud credentials
creds = Credentials.from_service_account_file(
    "path/to/your/service-account-key.json",
    scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
)
client = gspread.authorize(creds)

# Open a Google Sheet (replace with your sheet name)
sheet = client.open("InventoryData").sheet1  # Replace with your Google Sheet name

# Simulate a CRM (using a local file for simplicity)
def update_crm(data, crm_file="crm_data.txt"):
    with open(crm_file, "w") as f:
        for row in data:
            f.write(f"Product: {row[0]}, Stock: {row[1]}\n")

# Sync data from Google Sheet to CRM
def sync_sheet_to_crm():
    # Fetch data from Google Sheet
    data = sheet.get_all_values()[1:]  # Skip header row
    if not data:
        print("No data found in Google Sheet.")
        return
    
    # Update CRM
    update_crm(data)
    print("Data synced successfully!")

if __name__ == "__main__":
    try:
        sync_sheet_to_crm()
    except Exception as e:
        print(f"Error: {str(e)}")