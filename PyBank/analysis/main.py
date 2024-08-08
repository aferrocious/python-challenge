#Create script to analyze Profit/Losses of budget data
import os
import csv
import pandas as pd

#File location
budget_csv = os.path.join("..", "Resources", "budget_data.csv")
df = pd.read_csv(budget_csv)

#List to store data
Profit_Change = []

#Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)

    for row in csv_reader:
        #Count total number of month
        Total_Months = len(df)
        
        #Convert string to integers
        #Find net total amount of "Profit/Losses" over entire period
        df['Profit/Losses'] = df['Profit/Losses'].astype(int)
        Total_Profit = df['Profit/Losses'].sum()
        
        #Calculate changes in "Profit/Losses" for each month
        for i in range(1,len(df)):
            change = df['Profit/Losses'][i] - df['Profit/Losses'][i-1]
            Profit_Change.append(change)
        
    #Calculate average change in "Profit/Losses" over entire period
    Average_Change = sum(Profit_Change)/ len(Profit_Change)
       
    #Find greatest increase in profits (date and amount)
    Greatest_Increase = max(Profit_Change)
    Greatest_Increase_Index = Profit_Change.index(Greatest_Increase) +1
    Greatest_Increase_Month = df.loc[Greatest_Increase_Index, 'Date']
    
    #Find greatest decrease in profits (date and amount)
    Greatest_Decrease = min(Profit_Change)
    Greatest_Decrease_Index = Profit_Change.index(Greatest_Decrease) +1
    Greatest_Decrease_Month = df.loc[Greatest_Decrease_Index, 'Date']
         
#Prepare financial analysis summary to be printed to .txt
financial_analysis = (
    "Financial Analysis\n"
    "-----------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Total: ${Total_Profit}\n"
    f"Average Change: ${round(Average_Change,2)}\n"
    f"Greatest Increase in Profits: {Greatest_Increase_Month} (${Greatest_Increase})\n"
    f"Greatest Decrease in Profits: {Greatest_Decrease_Month} (${Greatest_Decrease})\n"
    )

#Print financial analysis to terminal
print(financial_analysis)

#Export results to text file
output_file = os.path.join("..", "analysis", "financial_analysis.txt")
with open(output_file, "w") as file:
    file.write(financial_analysis)

