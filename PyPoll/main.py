#import os and csv
import os
import csv

#define and open budget data file to read from
votes_file = os.path.join("Resources","election_data.csv")

#set reader
with open(votes_file,'r') as csvfile:
    voting_data = csv.reader(csvfile,delimiter=",")

    #skip header row
    first_row = next(voting_data, None)
    
    #define 'total votes' list and set initial vote counts
    total_votes= []
    other_votes = []
    candidate_1 = "Charles Casper Stockham"
    candidate_2 = "Diana DeGette"
    candidate_3 = "Raymon Anthony Doane"
    candidate_1_votes = 0
    candidate_2_votes = 0
    candidate_3_votes = 0

    #start for loop
    for i in voting_data:
        #add vote data to total votes list
        total_votes.append(i[2])
        #add votes for candidate 1
        if i[2] == candidate_1:
            candidate_1_votes += 1
        #add votes for candidate 2
        elif i[2] == candidate_2:
            candidate_2_votes += 1
        #add votes for candidate 3
        elif i[2] == candidate_3:
            candidate_3_votes += 1
        else: 
           other_votes.append(i)
    
    #check if other candidates got votes
    if len(other_votes) != 0:
        print("There are other candidates who received votes.")
    else:
        ""
    #calculate percentage of votes for Charles
    candidate_1_perc = (candidate_1_votes/len(total_votes))*100
    candidate_1_perc = round(candidate_1_perc,3)
    #calculate percentage of votes for Charles
    candidate_2_perc = (candidate_2_votes/len(total_votes)*100)
    candidate_2_perc = round(candidate_2_perc,3)
    #calculate percentage of votes for Charles
    candidate_3_perc = (candidate_3_votes/len(total_votes)*100)
    candidate_3_perc = round(candidate_3_perc,3)
    #determine the winner and winnder votes
    if candidate_1_votes > candidate_2_votes and candidate_1_votes > candidate_3_votes:
        winner = candidate_1
        winner_votes = candidate_1_votes
    elif candidate_2_votes > candidate_1_votes and candidate_2_votes > candidate_3_votes:
        winner = candidate_2
        winner_votes = candidate_2_votes
    elif candidate_3_votes > candidate_1_votes and candidate_3_votes > candidate_2_votes:
        winner = candidate_3_votes
        winner_votes = candidate_3_votes
    else:
        print("There was no winner.")

#define the election printout
election_printout = f'\
Election Results\n\
----------------------\n\
Total Votes: {len(total_votes)}\n\
----------------------\n\
{candidate_1}: {candidate_1_perc}% ({candidate_1_votes})\n\
{candidate_2}: {candidate_2_perc}% ({candidate_2_votes})\n\
{candidate_3}: {candidate_3_perc}% ({candidate_3_votes})\n\
----------------------\n\
Winner: {winner}\n\
----------------------'
#print the election printout
print(election_printout)

#define election path
election_printout_path=os.path.join("analysis","analysis.txt")

#open csv writer and write file to path
with open(election_printout_path,'w') as output_file:
    output_file.write(election_printout)
