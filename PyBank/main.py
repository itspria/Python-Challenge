# -*- coding: utf-8 -*-
"""
Created on Sun May 23 2021

@author: Priya Sundararaj
"""

def GetMaxIncrease(dateRange, changeInProfitLoss):
    '''    
    Parameters
    ----------
    dateRange : List of str
        List of dates.
    changeInProfitLoss : List of int
        List of change in profit\loss.

    Returns
    -------
    str
        The text of max value of the change in profi\loss and corresponding date.

    '''
    maxValue = max(changeInProfitLoss)
    index = changeInProfitLoss.index(maxValue)
    monthValue = dateRange[index+1]
    
    return (f"{monthValue} (${maxValue})")
    
def GetMinDecrease(dateRange, changeInProfitLoss):
    '''    
    Parameters
    ----------
    dateRange : List of str
        List of dates.
    changeInProfitLoss : List of int
        List of change in profit\loss.

    Returns
    -------
    str
        The text of min value of the change in profi\loss and corresponding date.

    '''
    minValue = min(changeInProfitLoss)
    index = changeInProfitLoss.index(minValue)
    monthValue = dateRange[index+1]
    
    return (f"{monthValue} (${minValue})")

#main script
import csv

#The net total amount of Profit\Losses over entire period
total = 0

#The changes in Profit\Losses over the entire period
changeInProfitLoss = []

#The list of date read from the csv file
dateRange = []

#The total number of months
monthCount = 0

#The profit\loss amount for each month
amount = 0

#Read the Budget_Data.csv and get the data
with open ("Resources\Budget_data.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    
    index = 1
    
    for row in csv_reader:
        
        #if first row skip calculating the change in value
        if index > 1:
            changeInProfitLoss.append(int(row[1]) - amount)
        
        monthCount += 1
        total += int(row[1])
        amount = int(row[1])
        index += 1
        dateRange.append(row[0])
csvfile.close()
        
#Add the analysis results to a text file
with open ("Analysis\FinancialAnalysis.txt", 'w') as textFile:
    print("Financial Analysis", file = textFile)
    print('-' * 26, file = textFile)
    print("Total Months: ", monthCount, file = textFile)
    print(f"Total: ${total}", file = textFile)
    print("Average Change: $",'{:.2f}'.format(sum(changeInProfitLoss)/len(changeInProfitLoss)), file = textFile)
    print("Greatest Increase in Profits: ", GetMaxIncrease(dateRange, changeInProfitLoss), file = textFile)
    print("Greatest Decrease in Profits: ", GetMinDecrease(dateRange, changeInProfitLoss), file = textFile)
textFile.close()     

#Read from FinancialAnalysis.txt file and print the output
with open("Analysis\FinancialAnalysis.txt", 'r') as textFile:
    print(textFile.read())
textFile.close()       


    
    
    