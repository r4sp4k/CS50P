import csv
import datetime
import shutil
import os

tday = datetime.date.today()
incomes = {}

def main():
    # Modify the date so taxyear is +1 only after March 31st
    taxyear = tday.year + 1 if tday > datetime.date(tday.year, 3, 31) else tday.year

    taxday = datetime.date(taxyear, 3, 31)
    till_taxday = taxday - tday

    # Backup file if it exists
    source_file = 'incomes.csv'
    dest_file = 'old-' + source_file
    if os.path.exists(source_file):
        shutil.copy(source_file, dest_file)

    # Read data from CSV file if it exists
    if os.path.exists(source_file):
        read_from_csv(source_file)

    print("====================================================")
    print(f"Today is {tday.day}.{tday.month}.{tday.year}, there are {till_taxday.days} days till Tax day.")
    print("====================================================")

    # Get income amounts
    while True:
        get_amount()
        while True:
            add_another = input("Add another amount? (Y/N): ").upper()
            if add_another in ["Y", "N"]:
                break
            else:
                print("Please type Y or N")
        if add_another == "N":
            break

    print("====================================================")
    print("Incomes:")
    print_recent_incomes()

    to_limit = get_remaining_sum()
    if to_limit > 0:
        print("====================================================")
        print(f"Remaining amount to limit is: {to_limit}")
        print("====================================================")
    else:
        print("====================================================")
        print(f"Limit was reached, extra taxes have to be paid.")
        print("====================================================")

    # Write data to 'incomes.csv'
    write_to_csv('incomes.csv')

# Read the data from a CSV file
def read_from_csv(filename):
    incomes.clear()
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            date_key = f"{row['year']} {row['month']}"
            incomes[date_key] = float(row['amount'])

# Write the data to a CSV file
def write_to_csv(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["year", "month", "amount"])
        writer.writeheader()
        for record in incomes:
            year, month = record.split()
            amount = incomes[record]
            writer.writerow({"year": year, "month": month, "amount": amount})

def get_twelve_months_ago():
    return tday.replace(year=tday.year - 1) if tday.month > 1 else tday.replace(year=tday.year - 1, month=tday.month + 11)

def get_remaining_sum():
    total = 0
    limit_amount = 49790
    twelve_months_ago = get_twelve_months_ago()

    for date_key, amount in incomes.items():
        year, month = map(int, date_key.split())
        income_date = datetime.date(year, month, 1)
        
        if income_date >= twelve_months_ago and income_date <= tday:
            total += amount
    
    return limit_amount - total

def print_recent_incomes():
    twelve_months_ago = get_twelve_months_ago()

    for date_key, value in incomes.items():
        year, month = map(int, date_key.split())
        income_date = datetime.date(year, month, 1)
        
        if income_date >= twelve_months_ago and income_date <= tday:
            print(f"Date: {date_key}, Amount: {value}")

def get_amount():
    while True:
        try:
            amount = float(input("Add amount: "))
        except ValueError:
            print("You have to specify a number")
        else:
            break

    while True:
        is_today = input("Is the income in the current month? (Y/N): ").upper()
        if is_today == "Y":
            date_key = f"{tday.year} {tday.month}"
            break
        elif is_today == "N":
            while True:
                try:
                    specify_year = int(input(f"Input year ({tday.year - 1} - {tday.year}): "))
                    if specify_year < (tday.year - 1) or specify_year > tday.year:
                        print(f"Year must be between {tday.year - 1} and {tday.year}. Please enter a valid year.")
                        continue
                    specify_month = int(input(f"Input month (1 - 12): "))
                    if specify_month < 1 or specify_month > 12:
                        print("Month must be between 1 and 12. Please enter a valid month.")
                        continue
                    
                    # Check if the date is in the future
                    if datetime.date(specify_year, specify_month, 1) > tday:
                        print("The specified date is in the future. Please enter a valid date.")
                    else:
                        break
                except ValueError:
                    print("Please enter a number for the year and month.")

            date_key = f"{specify_year} {specify_month}"
            break
        else:
            print("Please type Y or N.")

    if date_key in incomes:
        incomes[date_key] += amount
    else:
        incomes[date_key] = amount        
    return f"Date: {date_key}, Amount: {amount}"

if __name__ == "__main__":
    main()