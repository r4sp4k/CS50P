# TLSC (Tax Limit Sum Counter)
#### Video Demo: https://youtu.be/AEwW81bWLcs
#### Description:
In Slovakia, for self-employed individuals (known as "živnostníci") the deadline for submitting the income tax return is March 31st of the following year. The tax payment is due on the same date as the submission of the tax return. The threshold for mandatory VAT registration in Slovakia is €49,790 in turnover during the preceding 12 consecutive months. Once this threshold is reached, registration as a VAT payer is required. After registration, VAT must be charged on sales, and VAT on purchases can be reclaimed. If turnover does not exceed this limit, VAT registration is not required but can be done voluntarily. In order to avoid additional taxation (VAT) a self-employed individual should track incomes for the past year on the monthly basis to make sure the sum of €49,790 is not reached. Getting over this limit slightly for the past fiscal year would mean additional taxation and lower total income which is not desirable.

## The script
The tlsc script helps with tracking incomes within last twelve months in order to provide financial situation overview and remaining amount of possible future incomes that can be obtained without reaching the sum of €49,790.

### Script features:
- **Tracking Income:** The script records monthly income entries, allowing the user to specify amounts and dates.<br />
- **Tax Year Adjustment:** It considers a tax year starting on April 1st, and adjusts calculations based on this.<br />
- **Income Limit:** It calculates the remaining amount that can be earned within a year before reaching a set income limit, beyond which extra taxes will be incurred.<br />
- **Data Persistence:** Income data is saved in a CSV file, and it creates a backup before overwriting it.<br />

### Modules used:
All modules used are part of Python's standard library and do not need to be installed via pip.<br />

- **csv:** Provides functionality to read from and write to CSV files.<br />
- **datetime:** Supplies classes for manipulating dates and times.<br />
- **shutil:** Offers high-level file operations, used for backing up csv file.<br />
- **os:** Provides a check if csv file on a specified pathalready exists before doing the backup.<br />

### Functions used:
**1. main():**<br />
**Tax Year and Tax Day Calculation:** Determines the current tax year based on today's date. The tax year starts on April 1st. If today's date is after April 1st, the tax year is incremented by 1.<br />
**Backup:** If an incomes.csv file exists, it creates a backup named old-incomes.csv.<br />
**Read Data:** Reads the existing income data from the CSV file (if it exists) and stores it in a dictionary.<br />
**User Interaction:** Prompts the user to enter income amounts, allowing multiple entries. After each entry, the user can choose to add more amounts or to stop.<br />
**Print Information:** Displays the number of days remaining until the next tax day, lists all recent incomes (within the past year), and calculates the remaining sum that can be earned before hitting the limit.<br />
**Write Data:** Saves the income data to incomes.csv.<br />

**2. read_from_csv(filename):**<br />
**Purpose:** Reads income data from a specified CSV file.<br />
**Functionality:** Clears the current incomes dictionary and then populates it with data from the file, where each row corresponds to a year, month, and income amount.<br />

**3. write_to_csv(filename):**<br />
**Purpose:** Writes the current income data to a specified CSV file.<br />
**Functionality:** Writes the header row, followed by each entry in the incomes dictionary, formatted as year, month, and amount.<br />

**4. get_twelve_months_ago():**<br />
**Purpose:** Calculates the date exactly one year ago from today.<br />
**Functionality:** If today's month is January, it adjusts the year back by one and sets the month to December. Otherwise, it just decrements the year.<br />

**5. get_remaining_sum():**<br />
**Purpose:** Calculates the remaining income that can be earned before reaching a predefined limit.<br />
**Functionality:** Sums all incomes recorded in the past 12 months and subtracts this total from the limit (49790). Returns the remaining amount that can be earned.<br />

**6. print_recent_incomes():**<br />
**Purpose:** Prints all income entries from the past 12 months.<br />
**Functionality:** Iterates through the incomes dictionary and prints entries where the date is within the last 12 months.<br />

**7. get_amount():**<br />
**Purpose:** Prompts the user to input an income amount and specifies the date it was earned.<br />
**Functionality:** The user can choose whether the income was earned in the current month or another month. If another month is chosen, the user must specify the year and month. The income is then added to the incomes dictionary, either updating an existing entry or creating a new one.<br />

### Flow of Execution:
1. The script starts by calling main().<br />
2. It determines the current tax year and the number of days until the next tax day.<br />
3. It checks for existing income data, creating a backup if needed, and then loads the data.<br />
4. The user is prompted to enter income amounts.<br />
5. The script calculates the remaining income that can be earned before hitting the limit and displays relevant information.<br />
6. Finally, it saves the updated income data to the CSV file.<br />
