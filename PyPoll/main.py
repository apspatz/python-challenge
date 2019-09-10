import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

def FindWinner(names, percents):
    win = float(percents[0])
    winner = names[0]
    
    for count in percents:
        if float(count) > win:
            win = float(count)
            winner = names[count.index()]

    return winner

count = 0
candidates = []
candcount = []
candpercent = []


with open(csvpath,newline='')as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader, None)

# Count votes
    for row in csvreader:
        count +=1
         
        if row[2] not in candidates:
            candidates.append(row[2])
            candcount.append(1)
        else:
            votefor = candidates.index(row[2])
            candcount[votefor] += 1

# Calculate percentages        
    for votes in candcount:
        percent = float(votes/count * 100)
        candpercent.append(percent)

# Find winner
    winner = FindWinner(candidates, candcount)

#Output 
    print("Election Results")
    print("--------------------------")    
    print(f"Total Votes: {count}")
    print("--------------------------")  
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {round(candpercent[i],2)}% ({candcount[i]} votes)")
    print("--------------------------")
    print(f"{winner} is the winner.")
    
    f= open("Election.txt","w+")
    f.write("Election Results" "\n")
    f.write("--------------------------" "\n")    
    f.write(f"Total Votes: {count}" "\n")
    f.write("--------------------------" "\n") 
    for i in range(len(candidates)):
        f.write(f"{candidates[i]}: {round(candpercent[i],2)}% ({candcount[i]} votes)\n")
    f.write("--------------------------\n")
    f.write(f"{winner} is the winner.")
    f.close()       
    