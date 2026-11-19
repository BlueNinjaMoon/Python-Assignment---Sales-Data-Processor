import csv

file_path = "sales.csv"

def read_sales():
    """
    Reads and processes source records.
    """
    with open(file_path, "r", newline="") as file: 
        dictreader = csv.DictReader(file)
        valid = validate_sale(dictreader)

    summary = []
    for dict in valid:
        valid_sub = [dict["Item"],dict["Qty"],dict["Price Total"]]
        summary.append(valid_sub)
    full_qty = []
    full_total = []
    index = 0

    full_qtyKey = 0
    full_totalKey = 0

    full_qtyMon = 0
    full_totalMon = 0

    full_qtyMou = 0
    full_totalMou = 0

    full_qtyWeb = 0
    full_totalWeb = 0

    full_qtyHea = 0
    full_totalHea = 0

    for list in summary:
        item = list[0]
        item_in_sum = summary[index][0]
        if item == item_in_sum:
            if item == "Keyboard":
                full_qtyKey += int(list[1])
                full_totalKey += float(list[2])
            elif item == "Monitor":
                full_qtyMon += int(list[1])
                full_totalMon += float(list[2])
            elif item == "Mouse":
                full_qtyMou += int(list[1])
                full_totalMou += float(list[2])
            elif item == "Webcam":
                full_qtyWeb += int(list[1])
                full_totalWeb += float(list[2])
            elif item == "Headset":
                full_qtyHea += int(list[1])
                full_totalHea += float(list[2])
        index += 1
    print(f"Headset| Amount: {full_qtyHea} | Price Total: {full_totalHea:.2f}")
    print(f"Keyboard| Amount: {full_qtyHea} | Price Total: {full_totalHea:.2f}")
    print(f"Monitor| Amount: {full_qtyHea} | Price Total: {full_totalHea:.2f}")
    print(f"Mouse| Amount: {full_qtyHea} | Price Total: {full_totalHea:.2f}")
    print(f"Webcam| Amount: {full_qtyHea} | Price Total: {full_totalHea:.2f}")
        

    
    


def validate_sale(entry:dict):
    """
    Validates required fields and values.
    Customer and Item must not be blank;
    Qty must be a positive integer;
    Price Total must be a nonnegative number;
    all four fields must exist – empty strings for name or product will be considered invalid.
    Skips invalid records after logging them.
    """
    with open("errors.log", "w", newline="") as file:
        file.write(f"|---ERROR_LOG---|\n")
    
    line_num = 1
    valid = []
    for line in entry:
        errorline = ""
        invalid_reason = ""
        if line == "":
            errorline = "Customer"
            invalid_reason = "No line."
        elif line["Qty"].isdigit() != True:
            errorline = "Qty"
            invalid_reason = "Quantity isn't digit/int."
        elif int(line["Qty"]) < 1:
            errorline = "Qty"
            invalid_reason = "Quantity isn't higher than 0."
        elif line["Price Total"].replace(".","").isdigit() != True:
            errorline = "Price Total"
            invalid_reason = "Price Total not digit."
        elif float(line["Price Total"]) < 0:
            errorline = "Price Total"
            invalid_reason = "Price Total not higher than 0."        
        elif line["Customer"] == "":
            errorline = "Customer"
            invalid_reason = "Customer missing."
        elif line["Item"] == "":
            errorline = "Item"
            invalid_reason = "Item missing."
        elif line["Price Total"] == "":
            errorline = "Price Total"
            invalid_reason = "Price Total missing."
        elif line["Qty"] == "":
            errorline = "Qty"
            invalid_reason = "There is no quantity."
        if errorline != "":
            log_error(f"Line {line_num} | {line[errorline]} | {invalid_reason}")
        else:
            valid.append(line)
        line_num += 1
    return valid
    



def update_summary(entry) :
    """
    Accumulates item totals.
    """

def log_error(error):
    """
    Records invalid data and error details.
    """
    with open("errors.log", "a", newline="") as file:
        file.write(f"{error}\n")

def save_summary(entry:dict):
    """
    Writes grouped sales CSV. 
    """


def display_totals(totals):
    """
    Prints final totals.
    """




def main():
    """
    Coordinates the program and runs it.
    """
    valid = read_sales()
    
        
    
main()