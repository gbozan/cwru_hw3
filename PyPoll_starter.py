import csv
import os

# File paths for input and output
filepath = "Resources/election_data.csv"
file_to_output = "analysis/election_analysis.txt"

# Initialize variables
total_votes = 0
voting = {}
winner = ""
most_votes = 0

# Read the CSV file
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Count votes and track each candidate's votes
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate in voting:
            voting[candidate] += 1
        else:
            voting[candidate] = 1

# Start building the output
output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

# Calculate percentages and determine the winner
for candidate in voting:
    votes = voting[candidate]
    vote_percentage = (votes / total_votes) * 100
    output = output + f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

    if votes > most_votes:
        most_votes = votes
        winner = candidate

# Finalize the output with winner information
output = output + "-------------------------\n"
output = output + f"Winner: {winner}\n"
output = output + "-------------------------"

# Print and save results
print(output)
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
