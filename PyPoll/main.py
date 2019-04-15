import os
import csv

PyrollCSV = os.path.join('election_data.csv')

with open(PyrollCSV, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    countyCorrey = 0
    countKhan = 0
    countLi = 0
    countOTooley = 0
    totalCount = 0
    for row in csvreader:
        canddidate = row[2]
        totalCount +=1
    
        if (canddidate == "Correy"):
            countyCorrey +=1
        elif (canddidate == "Khan"):
            countKhan +=1
        elif (canddidate == "Li"):
            countLi +=1
        elif (canddidate == "O'Tooley"):
            countOTooley +=1
    
    
    Correypercent = round((countyCorrey/totalCount) * 100,2)
    Khanpercent = round((countKhan/totalCount) * 100,2)
    Lipercent = round((countLi/totalCount) * 100,2)
    OTooleypercent = round((countOTooley/totalCount) * 100,2)
    
    candidate_list = {countyCorrey:"Correy", countKhan:"Khan", countLi:"Li", countOTooley:"O'Tooley"}
    max = 0
    for count in candidate_list:
        if (count > max):
            max = count
    
    winner = candidate_list[max]
    
    print("Election Results")
    print("---------------------------")
    print(f'Total Votes: {totalCount}')
    print("---------------------------")
    print(f'Khan: {Khanpercent}% ({countKhan})')
    print(f'Correy: {Correypercent}% ({countyCorrey})')
    print(f'Li: {Lipercent}% ({countLi})')
    print(f'O\'Tooley: {OTooleypercent}% ({countOTooley})')
    print("---------------------------")
    print(f'Winner: {winner}')
    print("---------------------------")