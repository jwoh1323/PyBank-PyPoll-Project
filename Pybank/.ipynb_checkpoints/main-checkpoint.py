import os
import csv

PybankCSV = os.path.join('budget_data.csv')

with open(PybankCSV, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
           
    count = 0
    total = 0
    largest_change = 0 
    smallest_change = 0
    total_change = 0
    largest_date = ''
    smallest_date = ''
    
    for row in csvreader:
        total = total + int(row[1])
        count +=1
    
    csvfile.seek(0)
    header = next(csvreader)
    current_row = next(csvreader)
    current_value = int(current_row[1])
    
    for row in csvreader:
        change = int(row[1]) - current_value
        current_value = int(row[1])
        total_change += change
        
        averagechange = round(total_change/(count-1),2)
        
        if(change > largest_change):
            largest_change = change
            largest_date = row[0]
            
        elif (change < smallest_change):
            smallest_change = change
            smallest_date = row[0]
    
    print("Financial Analysis")
    print("---------------------------")
    print(f'Total Months: {count}')
    print(f'Total: ${total}')
    print(f'Average Change: {averagechange}')
    print(f'Greast Increase in Profit: {largest_date} (${largest_change})')
    print(f'Greatest Decrease in Profits: {smallest_date} (${smallest_change})')