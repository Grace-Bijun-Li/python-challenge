# Import sys
import sys

# Import pathlib and csv
import pathlib
import csv

# Set path for file with pathlib.Path(), pointing to the budget_data.csv file saved in the Resources folder
csvpath = pathlib.Path("./Resources/budget_data.csv")

# Open the CSV using the `with` keyword
with open(csvpath) as csvfile:
    # Use csv.reader() to read the csvfile variable, setting the delimiter argument equal to ","
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Create a date_set variable to count only the unique dates
    date_set = set()

    # Setup a loop counter to count the number of rows
    row_counter = 0

    # Setup a profit/loss counter to count the total amount
    total_profit_loss = 0

    # Setup the following variables to take care of the monthly profit/losses changes
    last_month_amount = 0
    amount_change_sum = 0
    amount_change = 0

    # Set up the maximum increase/decrease variables to calculate the greatest increase in profits and the greatest decrease in losses
    max_increase = 0
    max_decrease = 0

    # Loop through each row in csvreader 
    for row in csvreader:

        # Use if function to count the number of unique months in the dataset
        if row[0] not in date_set:
            date_set.add(row[0])
            row_counter = row_counter + 1
        
        # Add the total amount of profit/loss over the entire period
        total_profit_loss = total_profit_loss + int(row[1])

        # For monthly amount changes:
        if row_counter > 1:
            # This is to calculate monthly amount changes
            amount_change = int(row[1]) - last_month_amount
            # This is to add up the monthly amount changes
            amount_change_sum = amount_change_sum + (int(row[1]) - last_month_amount)
            # To calculate max increase/decrease
            if amount_change > max_increase:
                max_increase = amount_change
                max_increase_date = str(row[0])
            if amount_change < max_decrease:
                max_decrease = amount_change
                max_decrease_date = str(row[0])


        # The last_month_amount will automatically be updated to the most recent "last month" in every for loop
        last_month_amount = int(row[1])




    # Analysis Output
    sys.stdout = open("./analysis/analysis.txt", "w")

    print("PyBank Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {row_counter}")
    print(f"Total Profits/Losses: ${total_profit_loss}")
    print(f"Average Change: ${round(amount_change_sum / (row_counter - 1), 2)}")
    print(f"Greatest Increase in Profits: {max_increase_date} (${round(max_increase)})")
    print(f"Greatest Decrease in Losses: {max_decrease_date} (${round(max_decrease)})")

    sys.stdout.close()