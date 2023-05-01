import os
import csv

# Set the file path for the election data
election_data = os.path.join("Resources", "election_data.csv")

# Initialize empty lists to store data
ID = []
county = []
candidate = []
candidate_vote = []
candidate_percentage = []
Winner = []
total_vote = 0

# Open the CSV file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    # Loop through each row in the CSV file
    for row in csvreader:
        # Count the total number of votes cast
        total_vote = total_vote + 1
        
        # Add the candidate's name and vote to the candidate and candidate_vote lists
        if row[2] not in candidate:
            candidate.append(row[2])
            candidate_vote.append(1)
        else:
            candidate_vote[candidate.index(row[2])] = candidate_vote[candidate.index(row[2])] + 1        
    
    # Calculate the percentage of votes each candidate won
    for i in candidate_vote:
        candidate_percentage.append(round((i/total_vote)*100,3))
    
    # Find the winner of the election based on popular vote
    Winner = candidate[candidate_vote.index(max(candidate_vote))]

# Print out the results to the console
print("Election Results")
print("")
print("-------------------------")
print("")
print(f"Total Votes: {str(total_vote)}")
print("")
print("-------------------------")
print("")
for j in range(len(candidate)):
    print(f"{candidate[j]}: {str(candidate_percentage[j])}% ({str(candidate_vote[j])})")
    print("")
print("-------------------------")
print("")
print(f"Winner: {Winner}")
print("")
print("-------------------------")

# Write the results to a text file
with open('result.txt', 'w') as txtfile:
    txtfile.write("Election Results")
    txtfile.write("\n\n")
    txtfile.write("-------------------------")
    txtfile.write("\n\n")
    txtfile.write(f"Total Votes: {str(total_vote)}")
    txtfile.write("\n\n")
    txtfile.write("-------------------------")
    txtfile.write("\n\n")
    for k in range(len(candidate)):
        txtfile.write(f"{candidate[k]}: {str(candidate_percentage[k])}% ({str(candidate_vote[k])})")
        txtfile.write("\n\n")
    txtfile.write("-------------------------")
    txtfile.write("\n\n")
    txtfile.write(f"Winner: {Winner}")
    txtfile.write("\n\n")
    txtfile.write("-------------------------")
