# 3 columns - voter ID, county, candidate
# 1. total # of votes cast
# 2. complete list of candidates who received votes
# 3. % of votes each candidate won
# 4. total number of votes each candidate won
# 5. winner of the election based on popular vote

import os
import csv



# path to collect csv file
csvpath = os.path.join(".","election_data.csv")

# read in the csv file
with open(csvpath) as csvfile:

    #split the data in the file
    csvreader = csv.reader(csvfile, delimiter=",")

    # store elements of file in lists
    totalVotes = []
    candidateName = []
    candidateTotal = []
    

    # identify header row
    header = next(csvreader)

   # count number of total votes
    for row in csvreader:
        totalVotes.append(str(row[0]))
        count_votes = str(len(totalVotes))
    
# get unique candidate names list *****TODO need to format names
        if str(row[2]) not in candidateName:
            candidateName.append(str(row[2])) # how do I list the names out individually?
        


#-----------------------------------------------------
# percent of votes each candidate won
# candidateTotal = str(row[2])
# def getPercentages(candidateTotal):
#     
#     candidateTotal = (candidateName / count_votes) * 100
# print(candidateTotal) # ***this gave me one candidate name and no %***

   




    
            













#-----------------------------------------------------------------
# results should look like this:
#
print("Election Results")
print("--------------------------------------")
print("Total Votes: " + count_votes) 
print(f"Candidate Name:" , candidateName)

#---format????   print(f"Candidate Name: {str(candidateName).format[]}")
#--------------------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# Winner: Khan
#----final script should print and be exported to a text file with the results