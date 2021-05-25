# -*- coding: utf-8 -*-
"""
Created on Mon May 24 2021

@author: Priya Sundararaj
"""
    
import csv

#The total votes
totalVotes = 0

#Dictionary that holds candidates and their votes
candidateVotesDict = {}

#Read the Election_Data.csv and get the data
with open ("Resources\Election_data.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
  
    for row in csv_reader:
        totalVotes += 1
        
        #Add dictionary entry for every candidate and increment the votes for each candidate
        if row[2] in candidateVotesDict:
            candidateVotesDict[row[2]] = candidateVotesDict[row[2]]+1        
        else:
            candidateVotesDict[row[2]] = 1    
    
csvfile.close()

#Write to the Report.txt file
with open("Analysis\Report.txt", 'w') as textFile:
    print("Election Results", file = textFile)
    print("-" * 30, file = textFile)
    print("Total Votes: ", totalVotes, file = textFile)
    print("-" * 30, file = textFile)

    #for each for the keys(candidates) in the dictionary calculate the percentage of votes and print
    for key in candidateVotesDict.keys():
        percent = candidateVotesDict[key]/totalVotes *100
        print(f"{key}: {'{:.3f}%'.format(percent)} ({candidateVotesDict[key]})", file = textFile)        
    
    #The winner is the candidate(key) with maximum votes(values)
    winner = max(candidateVotesDict, key = candidateVotesDict.get)
    print("-" * 30, file = textFile)
    print(f"Winner: {winner}", file = textFile)
    print("-" * 30, file = textFile)
textFile.close()

#Read from Report.txt file and print the output to terminal
with open("Analysis\Report.txt", 'r') as textFile:
    print(textFile.read())
textFile.close()
    