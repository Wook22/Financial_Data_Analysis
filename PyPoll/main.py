import os
import csv

election_data = os.path.join("..", "Resources", "election_data.csv")

# Lists to store data
ID = []
County = []
Candidate = []

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    
