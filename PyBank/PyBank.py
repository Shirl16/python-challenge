# 1. calc total number of months
#-----------------------------------------------------------------------------------------
# import os and csv
import os
import csv
import statistics

# path to collect data from csv file
csvpath = os.path.join(".", "budget_data.csv")

# read in the csv file
with open(csvpath, newline="") as csvfile:
    
    # split the data in the file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # store elements of file in lists
    monthList =[]
    profitLoss = []
    pL_change = []
    great_increase = []
    great_decrease = []
    
        
    # identify header row
    header = next(csvreader)

    # count number of months
    for row in csvreader:
     
      monthList.append(str(row[0]))
      count_months = str(len(monthList))

       
  # sum total of profit and loss
      profitLoss.append(int(row[1]))
      totalPL = sum(profitLoss)

#-----------------------------------------------------------
  # average change of profit loss
      













       
    
    
    #output table
    #----------------------------------------------------------------------------------------
    print("Financial Analysis")
    print("------------------------------------------------")
    print("Total Months: " + count_months)
    print("Total:      ","${}".format(totalPL))  
    #------------TODO
    # print("Average Change:" ) #$-2315.12
    # print("Greatest Increase in Profits: ") #Feb-2012 ($1926159)
    # print("Greatest Decrease in Profits: ") #Sep-2013 ($-2196167)
    # ---then print table to text file
