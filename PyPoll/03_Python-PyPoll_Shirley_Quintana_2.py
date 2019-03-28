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
outputFile = os.path.join("results", "electionResults.txt")

# variables
totalVotes = 0
candidateNameList = []
candidateVoteDict = {}
candidateTotal = 0
currentVote = 0
percentVotes = 0.00
winner = ""
winnerVoteCount = 0

# read in the csv file
with open(csvpath) as csvfile:

    #split the data in the file
    csvreader = csv.reader(csvfile, delimiter=",")

    # identify header row
    header = next(csvreader)
    #print(header)
    

   # count number of total votes
    for row in csvreader:
        totalVotes = totalVotes + 1

        candidateName = row[2]

        if candidateName not in candidateNameList:
            candidateNameList.append(candidateName)
            candidateVoteDict[candidateName]=0
    
        candidateVoteDict[candidateName] = candidateVoteDict[candidateName] + 1
        
    votesByCandidate = ''
    # new loop to find winner from dictionary
    for name in candidateVoteDict:
        countVote = candidateVoteDict.get(name)
        
        percentVotes = (countVote / totalVotes) * 100
        
        votesByCandidate = votesByCandidate + f"{name}: {percentVotes:.3f}% ({countVote})\n"
              
        #print(votesByCandidate)
        
        if countVote > winnerVoteCount:
            winnerVoteCount = countVote
            winner = name
        
        
    



output = (
f"Election Results\n"
f"-------------------------------------------------\n"
f"Total Votes: {totalVotes}\n"
f"-------------------------------------------------\n"
f"{votesByCandidate}"
f"--------------------------------------------------\n"
f"Winner: {winner}\n"
f"--------------------------------------------------\n"
)

print(output)

with open(outputFile, "w") as txtFile:
    txtFile.write(output)