import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) 
SHEET = GSPREAD_CLIENT.open('love_sandwiches') # Using the name given to the spreadsheet file


def get_sales_data():
    """
    Get Sales figures input from the user.
    """
    print("Please enter Sales Data from the last market")
    print("Data should be Six numbers, seperated by commas.")
    print("Example: 10,20,30,40,50,60")

    data_str = input("Enter your data here:")
    
    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted to int, or 
    if there are not exactly six values (6 items being sold,
    so 6 sales data to be recorded.)
    """
    try:
        # if length of input list is more than 6
        if len(values) != 6:
            # raise error
            raise ValueError(
            # format string response with amount of values input
            f"Exactly 6 values required, you provided {len(values)}"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")


get_sales_data()