import csv
file_path = "sales.csv"

line = 0

def read_sales():
    """
    Reads and processes source records.
    """
    with open(file_path, "r", newline="") as file: 
        dictreader = csv.DictReader(file)

    validate_sale(dictreader)

    return dictreader

def validate_sale(entry):
    """
    Validates required fields and values.
    """
    for line in entry:
        
    



def update_summary() :
    """
    Accumulates item totals.
    """

def log_error(error):
    """
    Records invalid data and error details.
    """
    with open("errors.log", "w"):
        csv.writer(error)

def save_summary():
    """
    Writes grouped sales CSV. 
    """

def display_totals():
    """
    Prints final totals.
    """



def main():
    """
    Coordinates the program and runs it.
    """
    dictreader = read_sales()
    display_totals()
main()