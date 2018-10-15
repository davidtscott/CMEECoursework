import sys 
import csv 

def fasta_input(fastafile):
    with open(fastafile, 'r') as f1: #'with' closes the file automatically
        f1str = "" #creates blank string
        counter = 0 #counter 
        for line in f1: 
            if counter:  #if counter 0 (header) skip it
                f1str += line.replace("\n", "") # if not, so this
            counter += 1
    return f1str


# assign the longest sequence s1, and the shortest to s2
# l1 is the length of the longest, l2 that of the shortest

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


def main(argv):
    if len(argv) >= 3:
        seq1 = fasta_input(sys.argv[1])
        seq2 = fasta_input(sys.argv[2])
    else:
        seq1 = fasta_input('../Data/fasta/407228326.fasta')
        seq2 = fasta_input('../Data/fasta/407228412.fasta')
    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:
        s1 = seq1
        s2 = seq2
    else:
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swap the two lengths


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

    g = open('../Results/align_seqs_fasta.csv','w')
    csvwrite = csv.writer(g)
    csvwrite.writerow(['Best score is',my_best_score]) #adds header
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)