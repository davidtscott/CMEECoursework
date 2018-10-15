import csv
import sys
import doctest

#Define function
def is_an_oak(oakname):
    ## doctests within module
    """ Returns True if name starts with 'quercus', 
        otherwise returns False.
        
    >>> is_an_oak('Quercus robur')
    True
        
    >>> is_an_oak('Fraxinus excelsior')
    False

    >>> is_an_oak('Quercusstartswithaq fancythat')
    False

    """
    oakname = oakname.lower() #bug, quercus missing a u
    # Take string, split on space, then take index [0] of the generated list.
    oakindex = oakname.split(" ")
    if len(oakindex[0]) != 7:
        return False
    return oakname.startswith('quercus')
        

def main(argv): 
    f = open('../Data/TestOaksData.csv','r')
    g = open('../Data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    next(taxa) #excludes header
    csvwrite = csv.writer(g)
    csvwrite.writerow(['Genus', 'species']) #adds header to new csv
    oaks = set()
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0]):   #bug above interupted code here. 
        #did not recognise any oaks due to misspelling 
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

doctest.testmod()