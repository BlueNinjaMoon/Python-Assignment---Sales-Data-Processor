import csv
file_path = "sales.csv"

line = 0

def read_sales(entry):
    """
    Reads and processes source records.
    """
    validate_sale(entry)

def validate_sale(entry:dict):
    """
    Validates required fields and values.
    """
    line_num = 0
    with open("errors.log", "w") as file:
        file.write("Top")
    for line in entry:
        if line == "":
            errorline = "Customer"
            invalid_reason = "No line."
        
        elif line["Qty"].isdigit() != True:
            errorline = "Qty"
            invalid_reason = "Quantity isn't digit/int."
        
        elif int(line["Qty"]) < 0:
            errorline = "Qty"
            invalid_reason = "Quantity isn't higher than 0."

        elif line["Qty"] == "":
            errorline = "Qty"
            invalid_reason = "There is no quantity."
            
        elif line["Price Total"].replace(".","").isdigit() != True:
            errorline = "Price Total"
            invalid_reason = "Price Total not digit."

        elif float(line["Price Total"]) < 0:
            errorline = "Price Total"
            invalid_reason = "Price Total not higher than 0."
            
        log_error(f"Line {line_num} | {invalid_reason} | {line[errorline]}")
        line_num += 1
    



def update_summary() :
    """
    Accumulates item totals.
    """

def log_error(error):
    """
    Records invalid data and error details.
    """
    with open("errors.log", "a", newline="") as file:
        file.write(f"\n{error}")

def save_summary(entry:dict):
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
    with open(file_path, "r", newline="") as file: 
        dictreader = csv.DictReader(file)
        read_sales(dictreader)
        
        
    
main()