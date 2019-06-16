import os, csv

csv_path = os.path.join("..", "Resources", "election_data.csv")

voterid=[]
county=[]
candidate=[]
previous_poll=0

with open(csv_path, newline="", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print (csv_reader)

    csv_header = next(csv_reader)

    
    winner_name=int(0)


    for row in csv_reader:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
#print(voterid)
#print(county)
#print(candidate)

#int for total_votes?
total_votes= len(voterid)

print("Election Results")
print("-" * 20)
print(f"Total Votes: {total_votes}")
print("-" * 20)

# below created a dictionary. pulled keys (i) and values (candidategrp[i]) out of the dictionary.
from collections import Counter
candidategrp= Counter(candidate)
# #print(f"Candidate groups: {candidategrp}")
# #print(f"{candidategrp['Khan']}")
for i in candidategrp:
    print (i, candidategrp[i])
    
    candperc= int(candidategrp[i])
    percentage = (candperc/total_votes) * 100
    print(f"{percentage}")

for j in candidategrp:
    if previous_poll<candidategrp[i]:
        previous_poll=candidategrp[i]
        winner_name= j


print("-" * 20)

print(f"Winner: {winner_name}")


with open("Output.txt", "w", newline="") as output:
    
    #"print('total_votes= len(voterid)', file=<output_stream>)
    print >>output, 'print("Election Results")\n',
    # print >>output, 'print("-" * 20)\n'
    # print >>output, 'print(f"Total Votes: {total_votes}")\n'
    # print >>output, 'print("-" * 20)' 

