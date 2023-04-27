import os
import csv

budget_data = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data
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


total_month = 0
total_amount = 0
value = 0
average_change = 0


# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    
    for row in csvreader:
        # Add Date
        date.append(row[0])
        
        # Split the date into year and day
        split_date = row[0].split("-")
        year.append(split_date[0])
        day.append(split_date[1])
        

        # Add Profit
        profit.append(row[1])
        
        # Add count total months
        total_month = total_month + 1
        
        # Add all total amount
        total_amount = total_amount + int(row[1])
    
    #Average 
    average_change = sum(profit)/len(profit)
        
    #Greatest Increase
    increase = max(profit)
    inc_index = profit.index(increase)
    inc_date = date[inc_index]

    #Greatest Decrease
    decrease = min(profit)
    dec_index = profit.index(decrease)
    dec_date = date[dec_index]
    


#Displaying information
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_month)}")
print(f"Total: ${str(total_amount)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {inc_date} (${str(increase)})")
print(f"Greatest Decrease in Profits: {dec_date} (${str(decrease)})")

        
finalScript = "result.txt"

with open(finalScript, "w") as txtfile:
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
    
    
