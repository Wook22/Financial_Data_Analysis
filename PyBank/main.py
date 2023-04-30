import os
import csv

# Set the file path for the budget data
budget_data = os.path.join("..", "Resources", "budget_data.csv")

# Create empty lists to store data
year = []
day = []
date = []
profit = []
increase = []
inc_date = []
inc_index = []
decrease = []
dec_date = []
dec_index = []

# Initialize variables for calculations
total_month = 0
total_amount = 0
average_change = 0

# Open the CSV file and read the data using the csv module
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    csvheader = next(csvreader)
    
    # Loop through each row in the CSV file
    for row in csvreader:
        # Extract the date, year, and day from the current row
        date.append(row[0])
        split_date = row[0].split("-")
        year.append(split_date[0])
        day.append(split_date[1])
        
        # Extract the profit/loss value from the current row
        profit.append(row[1])
        
        # Increment the total month count and total amount variables
        total_month = total_month + 1
        total_amount = total_amount + int(row[1])
    
    # Calculate the average change in profit/loss over the entire period
    average_change = sum(profit) / len(profit)
        
    # Find the greatest increase and decrease in profit/loss over the entire period
    increase = max(profit)
    inc_index = profit.index(increase)
    inc_date = date[inc_index]
    decrease = min(profit)
    dec_index = profit.index(decrease)
    dec_date = date[dec_index]
    
# Print out the results to the console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_month)}")
print(f"Total: ${str(total_amount)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {inc_date} (${str(increase)})")
print(f"Greatest Decrease in Profits: {dec_date} (${str(decrease)})")

# Write the results to a text file
with open('result.txt', 'x') as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Months: {str(total_month)}")
    txtfile.write("\n")
    txtfile.write(f"Total: ${str(total_amount)}")
    txtfile.write("\n")
    txtfile.write(f"Average Change: ${str(round(average_change,2))}")
    txtfile.write("\n")
    txtfile.write(f"Greatest Increase in Profits: {inc_date} (${str(increase)})")
    txtfile.write("\n")
    txtfile.write(f"Greatest Decrease in Profits: {dec_date} (${str(decrease)})")
