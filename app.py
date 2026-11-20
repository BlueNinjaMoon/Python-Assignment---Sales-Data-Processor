import csv

files_created = []

def read_sales():
    """
    Reads and processes source records.
    """
    file_path = "sales.csv"
    with open(file_path, "r", newline="") as file: 
        dictreader = csv.DictReader(file)
        returns = validate_sale(dictreader)
        valid = returns[0]
        errors = returns[1]

    summary = []
    for dict in valid:
        valid_sub = [dict["Item"],dict["Qty"],dict["Price Total"]]
        summary.append(valid_sub)
    return update_summary(summary),errors

def validate_sale(entry:dict):
    """
    Validates required fields and values.
    Customer and Item must not be blank;
    Qty must be a positive integer;
    Price Total must be a nonnegative number;
    all four fields must exist – empty strings for name or product will be considered invalid.
    Skips invalid records after logging them.
    """
    file_path = "errors.log"
    with open(file_path, "w", newline="") as file:
        file.write(f"|---ERROR_LOG---|\n")
    
    line_num = 1
    valid = []
    errors = 0
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
            errors += 1
        else:
            valid.append(line)
        line_num += 1
    files_created.append(file_path)
    return valid,errors

def update_summary(entry) :
    """
    Accumulates item totals.
    """
    full = []
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

    for list in entry:
        item = list[0]
        item_in_sum = entry[index][0]
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

    full.append([[f"HeadsetAmount: {full_qtyHea}"],[f"Price Total: {full_totalHea:.2f}"]])
    full.append([[f"KeyboardAmount: {full_qtyKey}"], [f"Price Total: {full_totalKey:.2f}"]])
    full.append([[f"MonitorAmount: {full_qtyMon}"], [f"Price Total: {full_totalMon:.2f}"]])
    full.append([[f"MouseAmount: {full_qtyMou}"],[f"Price Total: {full_totalMou:.2f}"]])
    full.append([[f"WebcamAmount: {full_qtyWeb}"], [f"Price Total: {full_totalWeb:.2f}"]])
    save_summary(full)
    return full

def log_error(error):
    """
    Records invalid data and error details.
    """
    file_path = "errors.log"
    with open(file_path, "a", newline="") as file:
        file.write(f"{error}\n")

def save_summary(entry:list):
    """
    Writes grouped sales CSV with entry. 
    """
    file_path = "sales_summary.csv"
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in entry:
            writer.writerow(row)
    files_created.append(file_path)



def display_totals(priceqty, errors):
    """
    Prints final totals.
    """
    finalqty = 0
    finalprice = 0.0
    for total in priceqty:
        numindex = total[0][0].find(" ")
        qty = int(total[0][0][numindex+1:])
        price = float(total[1][0][numindex+1:])
        finalqty += qty
        finalprice += price

    print("Sales Processing Complete")
    print("-------------------------")
    print(f"Total Items Sold: {finalqty}")
    print(f"Sales Subtotal: ${finalprice}")
    print(f"Invalid Records: {errors}")
    print(f"Files Created: {files_created[0]}, {files_created[1]}")

        




def main():
    """
    Coordinates the program and runs it.
    """
    returns = read_sales()
    priceqty = returns[0]
    errors = returns[1]
    display_totals(priceqty,errors)
    
        
    
main()