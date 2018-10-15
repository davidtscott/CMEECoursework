# These are the two sequences to match
#seq2 = "ATCGCCGGATTACGGG"
#seq1 = "CAATTCGGAT"

import csv 

with open('../Data/align_seqs.csv', 'r') as csvfile:
    DNAseqs = csv.reader(csvfile)
    for row in DNAseqs:
        seq1 = row[0]
        seq2 = row[1]

# assign the longest sequence s1, and the shortest to s2
# l1 is the length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

# function that computes a score
# by returning the number of matches 
# starting from arbitrary startpoint
def calculate_score(s1, s2, l1, l2, startpoint):
    # startpoint is the point at which we want to start
    matched = "" # contains string for alignement
    score = 0
    for i in range(l2):
        #pdb.set_trace()
        if (i + startpoint) < l1:
            # if its matching the character
            if s1[i + startpoint] == s2[i]:
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # build some formatted output
    print("." * startpoint + matched)        
    print("." * startpoint + s2) 
    print(s1)
    print(score) 
    print("")

    return score

calculate_score(s1, s2, l1, l2, 0)
calculate_score(s1, s2, l1, l2, 1)
calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score)
my_best_align = None
my_best_score = -1

for i in range(l1):
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2
        my_best_score = z

print(my_best_align)
print(s1)
print("Best score:", my_best_score)

g = open('../Results/align_seqs.csv','w')
csvwrite = csv.writer(g)
csvwrite.writerow(['Best alignment', 'Best score']) #adds header
csvwrite.writerow([my_best_align, my_best_score])
csvwrite.writerow([s1])
