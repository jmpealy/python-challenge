#import os and csv
import os
import csv

#define and open budget data file to read from
budget_data=os.path.join("Resources","budget_data.csv")

#set reader
with open(budget_data,'r') as csvfile:
    budgetreader=csv.reader(csvfile,delimiter=",")
    
    #skip headers and first month using next functions as first month isn't useful for monthly change purposes
    header=next(budgetreader, None)
    first_month=next(budgetreader,None)

    #define changes list, greatest increases and decreases and set initial total pnl and pnl change conditions
    Changes=[]
    max_increase=["",0]
    max_decrease=["",0]
    TotalPnL=int(first_month[1])
    PriorMonthPnL=int(first_month[1])

    #loop through each row
    for row in budgetreader:
        #add new month to existing month count and set new month count
        #make sure to record current month
        current_month=row[0]
        #add new monthly pnl to existing PnL and set new total pnl
        #make sure to include month 1 in total pnl
        MonthlyPnL=int(row[1])
        TotalPnL=MonthlyPnL+TotalPnL
        #define monthly change variable and make sure to include month 1 pnl as the reference for the first 'monthly change
        Monthly_change=MonthlyPnL-PriorMonthPnL
        PriorMonthPnL=MonthlyPnL
        #add monthly change to list
        Changes.append(Monthly_change)
        #determine if this month's change is the greatest increase so far
        if Monthly_change>max_increase[1]:
            max_increase=[current_month,Monthly_change]
        #determine if this month's change is the greatest decrease so far
        if Monthly_change<max_decrease[1]:
            max_decrease=[current_month,Monthly_change]

    #define and round average change function
    average_change=sum(Changes)/len(Changes)
    average_change=round(average_change,2)
    
#build output set
output_set=f"\
Financial Analysis\n\
------------------------\n\
Total Months: ${len(Changes)+1}\n\
Total: ${TotalPnL}\n\
Average Change: ${average_change}\n\
Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n\
Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})"

#print the output set
print(output_set)

#define budget path
budget_output_path=os.path.join("analysis","analysis.txt")

#open csv writer and write file to path
with open(budget_output_path,'w') as output_file:
    output_file.write(output_set)
        









