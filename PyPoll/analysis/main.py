#Create script to analyze election data
import os
import pandas as pd

#File location
election_data_csv = os.path.join("..", "Resources", "election_data.csv")
df = pd.read_csv(election_data_csv)

#List to store data
Unique_Candidates = []
Candidate_Results = []

#Count total number of votes
Total_Votes = len(df)

#Create list of unique candadates who received votes
Unique_Candidates = df.iloc[:,2].unique()

#Calculate votes and percentages for each candidate
Candidate_Votes = df.iloc[:,2].value_counts()
Candidate_Percentages = (Candidate_Votes / Total_Votes) * 100

#Prepare list of results by candadate (name, percentage votes, vote count)
for Candidate in Unique_Candidates:
    Votes = Candidate_Votes.get(Candidate, 0)
    Percentage = Candidate_Percentages.get(Candidate, 0)
    Candidate_Results.append(f"{Candidate}: {Percentage: .3f}% ({Votes})")
    
#Determine Winner based on maximum votes
Winner = Candidate_Votes.idxmax()

#Prepare election result analysis summary to be printed to .txt
election_analysis = (
    "Election Results\n"
    "--------------------------\n"
    f"Total Votes: {Total_Votes}\n"
    "--------------------------\n"
    + "\n".join(Candidate_Results) + "\n"
    "--------------------------\n"
    f"Winner: {Winner}\n"
    "--------------------------"
)

#Print election results to terminal
print(election_analysis)

#Export results to text file
output_file = os.path.join("..", "analysis", "election_analysis.txt")
with open(output_file, "w") as file:
    file.write(election_analysis)
