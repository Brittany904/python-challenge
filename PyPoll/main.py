import os
import csv
from pathlib import Path 

#call the file and import it
election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

#open the file
with open(election_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    skip = next(csvreader)

#declare the necessary variables
    tot_votes = []
    first_cand = 0
    sec_cand = 0
    third_cand = 0

#loop to go through each row and grab data

    for row in csvreader:

        #add the ballot id to list to get total votes
        tot_votes.append(row[0])

        #create if statement that evaluates the candidate name and adds up vote
        if row[2] == "Charles Casper Stockham":
            first_cand +=1
        elif row[2] == "Diana DeGette":
            sec_cand +=1
        elif row[2] == "Raymon Anthony Doane":
            third_cand +=1

#calculate the percentage of votes
first_perc = (first_cand/len(tot_votes)) * 100
sec_perc = (sec_cand/len(tot_votes)) * 100
third_perc = (third_cand/len(tot_votes)) * 100


#print the analysis
print("Election Results")
print("---------------------------")

#print out the total of the votes
print(f'Total Votes:  {len(tot_votes)}')
print("---------------------------")
print(f'Charles Casper Stockham: {first_perc:.3f}%  ({first_cand})')
print(f'Diana DeGette: {sec_perc:.3f}%  ({sec_cand})')
print(f'Raymon Anthony Doane: {third_perc:.3f}%  ({third_cand})')
print("---------------------------")
print("Winner: Diana DeGette")


#output/export the text file
out_file = Path("PyPoll", "analysis", "PyPollanalysis.txt")

with open(out_file, "w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("---------------------------")
    file.write("\n")

    #print out the total of the votes
    file.write(f'Total Votes:  {len(tot_votes)}')
    file.write("\n")
    file.write("---------------------------")
    file.write("\n")
    file.write(f'Charles Casper Stockham: {first_perc:.3f}%  ({first_cand})')
    file.write("\n")
    file.write(f'Diana DeGette: {sec_perc:.3f}%  ({sec_cand})')
    file.write("\n")
    file.write(f'Raymon Anthony Doane: {third_perc:.3f}%  ({third_cand})')
    file.write("\n")
    file.write("---------------------------")
    file.write("\n")
    file.write("Winner: Diana DeGette")