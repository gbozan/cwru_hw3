import csv
import os

# File paths for the input CSV and output text file
filepath = "Resources/budget_data.csv"
file_to_output = "analysis/budget_analysis.txt"

# Initialize variables for tracking financial metrics
months = 0
net_amt = 0
total_change = 0
max_change = 0
min_change = 0
max_month = ""
min_month = ""
last_month_profit = 0
curr_month_profit = 0

# Read and process the CSV data
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)  # Skip header

    for row in csvreader:
        months += 1
        net_amt += int(row[1])

        # Calculate monthly change, track max/min changes
        if months != 1:
            curr_month_profit = int(row[1])
            change = curr_month_profit - last_month_profit
            total_change += change
            last_month_profit = curr_month_profit  
            
            if change > max_change:
                max_change = change
                max_month = row[0]
            if change < min_change:
                min_change = change
                min_month = row[0]
        else:
            last_month_profit = int(row[1])

# Compute the average change in profits/losses
avg_change = total_change / (months - 1)

# Create the output summary
output = f"""
Financial Analysis
----------------------------
Total Months: {months}
Total: ${net_amt}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})
"""
print(output)

# Write summary to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
