# import os and csv
import os
import csv
import statistics

# path to collect data from csv file
csvpath = os.path.join(".", "budget_data.csv")
outputFile = os.path.join("analysis", "budget_analysis.txt")

# variables
totalRevenue = 0
revenueChange = 0.00
monthCount = 0
percentChange = 0.00
avgRevChange = 0
totalRevChange = 0.00
greatestIncrease = 0.00
greatestDecrease = 0.00
previousRevenue = 0.00
currentRevenue = 0.00


# read in the csv file
with open(csvpath, newline="") as csvfile:

    # split the data in the file
    csvreader = csv.reader(csvfile, delimiter=',')

    # identify header row
    header = next(csvreader)
    #print(header)
    #print(header[0],header[1])

    firstDataRow = next(csvreader)
    #print(firstDataRow[1])
    
    monthCount = monthCount + 1
    totalRevenue = totalRevenue + int(firstDataRow[1])
    previousRevenue = int(firstDataRow[1])

    #print(totalRevenue)

    # count number of months
    for row in csvreader:
        
        monthCount = monthCount + 1
        
        #calculate the total revenue
        currentRevenue = int(row[1])
        currentDate = str(row[0])
        totalRevenue = totalRevenue + currentRevenue
        
        revenueChange = currentRevenue - previousRevenue
                
        totalRevChange = totalRevChange + revenueChange

        percentChange = percentChange + 1
    
        
                
        #calculate revenue change for each month
        if monthCount > 1:

            revenueChange = currentRevenue - previousRevenue
            totalRevChange = totalRevChange + revenueChange
            percentChange = percentChange + 1
       
        
        if revenueChange >= 0:
            if revenueChange > greatestIncrease:
                greatestIncrease = revenueChange
                greatRevDate = currentDate
            
       
        elif revenueChange < 0:

            if revenueChange < greatestDecrease:

                greatestDecrease = revenueChange
                greatRevDecreaseDate = currentDate
                
               
        # store the current revenue
        previousRevenue = currentRevenue

        # #calculate the average revenue change
        avgRevChange = totalRevChange / percentChange
      



output = (
f"Financial Analysis\n"
f"------------------------------------------------------\n"
f"Total Months:  {monthCount}\n"
f"Total: ${totalRevenue}\n"
f"Average Revenue Change: ${avgRevChange:.2f}\n"
f"Greatest Increase in Profits: {greatRevDate} ${greatestIncrease}\n"
f"Greatest Decrease in Profits: {greatRevDecreaseDate} ${greatestDecrease}\n"
)

print(output)

with open(outputFile, "w") as txtFile:
    txtFile.write(output)
