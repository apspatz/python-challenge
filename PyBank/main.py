import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

def AvgMonth(Month):
    total = 0
    
    for i in Month:
        total += int(i)
    
    Ave = total/len(Month)
    return Ave


with open(csvpath,newline='')as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    Header = next(csvreader, None)
    
    Months = []
    TotalDollars = 0
    MonthbyMonth = []
    PreviousMonthProfit = 0
    BigGain = 0
    BigLoss = 0

    for row in csvreader:
        # Create Months list
        Months.append(row[0])

        # Count Profits/Losses
        TotalDollars += int(row[1])
        MonthbyMonth.append(int(row[1])-PreviousMonthProfit)
        PreviousMonthProfit = int(row[1])        
        
        # Compare Profits/Losses
        if int(row[1]) > BigGain:
            BigGain = int(row[1])
            GainMonth = row[0]
        
        if int(row[1]) < BigLoss:
            BigLoss = int(row[1])
            LossMonth = row[0]


#Output
    print("Financial Analysis")
    print("--------------------------")    
    print(f"Months: {len(Months)}")
    print(f"Total Profits: ${TotalDollars}")
    print(f"Average Monthly Profit: ${round(AvgMonth(MonthbyMonth),2)}")
    print(f"Largest Profit Month: {GainMonth}; Profit: ${BigGain}")
    print(f"Largest Loss Month: {LossMonth}; Profit: ${BigLoss}")

    f= open("Bank.txt","w+")
    f.write("Financial Analysis" "\n")
    f.write("--------------------------" "\n")    
    f.write(f"Months: {len(Months)}" "\n")
    f.write(f"Total Profits: ${TotalDollars}" "\n")
    f.write(f"Average Monthly Profit: ${round(AvgMonth(MonthbyMonth),2)}" "\n")
    f.write(f"Largest Profit Month: {GainMonth}; Profit: ${BigGain}" "\n")
    f.write(f"Largest Loss Month: {LossMonth}; Profit: ${BigLoss}" "\n")
    f.close()