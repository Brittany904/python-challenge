import os
import csv
from pathlib import Path 

# Call the file/import it
budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

#open the csv file 
with open(budget_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    skip = next(csvreader)

    #create lists to calculate the required values
    num_month = []
    net_amount = []
    change_profit = []
    date_profit = ["Date"]
#create a loop to go through file rows 
    for row in csvreader:

        #add the months to the list to get total months
        num_month.append(row[0])

        #add up the profit/lossed column and add to list to later get sum
        net_amount.append(int(row[1]))

    #create loop to get the profit change/average

        #create a loop to get range of the net_amount and grab changes
    for e in range(len(net_amount)-1):
        #find out the change
        change_profit.append(net_amount[e+1]-net_amount[e])

    #create variable for avg change
    avg_profit = sum(change_profit)/len(change_profit)

    #calculate the greatest increase in profits and find position of max/get date
    in_profit = max(change_profit)

    #calculate the greatest decrease in profits and find postion of max/get date
    de_profit = min(change_profit)

    #print out the results
    print("Financial Analysis")
    print("------------------------------------")

    #print out the count of the months and total profit
    print(f'Total months:  {len(num_month)}')
    print(f'Total:  ${sum(net_amount)}')

    #printing the average and round to two decimal places
    print(f'Average Change:  ${round((avg_profit),2)}')

    #print out the incr/decr of profits and accompanying date
    print(f'Greatest increase in Profits:   (${in_profit})')
    print(f'Greatest Decrease in Profits: (${de_profit})')

    #print out to terminal and export file

out_file = Path("PyBank", "analysis", "PyBankanalysis.txt")

with open(out_file, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("------------------------------------")
    file.write("\n")
    #print out the count of the months and total profit
    file.write(f'Total months:  {len(num_month)}')
    file.write("\n")
    file.write(f'Total:  ${sum(net_amount)}')
    file.write("\n")
    #printing the average and round to two decimal places
    file.write(f'Average Change:  ${round((avg_profit),2)}')
    file.write("\n")
    #print out the incr/decr of profits and accompanying date
    file.write(f'Greatest increase in Profits:   (${in_profit})')
    file.write("\n")
    file.write(f'Greatest Decrease in Profits: (${de_profit})')
