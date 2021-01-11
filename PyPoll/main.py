# Import sys
import sys

# Import pathlib and csv
import pathlib
import csv

# Set path for file with pathlib.Path(), pointing to the election_data.csv file saved in the Resources folder
csvpath = pathlib.Path("./Resources/election_data.csv")

# Open the CSV using the `with` keyword
with open(csvpath) as csvfile:
    # Use csv.reader() to read the csvfile variable, setting the delimiter argument equal to ","
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)

    # Create a date_set variable to count only the unique Voter IDs
    voter_set = set()

    # Setup a loop counter to count the number of rows
    row_counter = 0

    candidate_dict = dict()

    # Loop through each row in csvreader 
    for row in csvreader:

        # Use if function to count the number of unique Voter IDs in the dataset
        if row[0] not in voter_set:
            voter_set.add(row[0])
            row_counter = row_counter + 1
        
        # Set up dict key to pick up candidate name
        candidate_name = row[2]
        # Use if function to count the total number of votes for each candidate
        if candidate_name not in candidate_dict:
            candidate_dict[candidate_name] = 1
        else:
            candidate_dict[candidate_name] = candidate_dict[candidate_name] + 1
        


    # Analysis Output
    sys.stdout = open("./analysis/analysis.txt", "w")

    print("PyPoll Election Results")
    print("-------------------------")
    print(f"Total Votes: {row_counter}")
    print("-------------------------")
    
    # Set winner_percent variable to determine the winner of PyPoll
    winner_percent = 0

    # Use for loop & if function to get each candidate's result and determine the winner
    for key in candidate_dict:
        percent = round(candidate_dict[key]/row_counter * 100, 3)
        
        if percent > winner_percent:
            winner_percent = percent
            winner_key = key

        print(key + ": " + str(percent) + "% (" + str(candidate_dict[key]) +")")

    print("-------------------------")
    print("Winner: " + winner_key)
    print("-------------------------")
