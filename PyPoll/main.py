import os
import csv

election_data = os.path.join("..", "Resources", "election_data.csv")

# Lists to store data
ID = []
county = []
candidate = []

candidate_vote = []
candidate_percantage = []

total_vote = 0



# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    for row in csvreader:
        # The total number of votes cast
        total_vote = total_vote + 1
        
        # A complete list of candidates who received votes
        if row[2] not in candidate:
            candidate.append(row[2])
            
            
        
        # The percentage of votes each candidate won
        
        
        # The total number of votes each candidate won
        
        
        # The winner of the election based on popular vote.



        
