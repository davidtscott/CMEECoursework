#!/usr/bin/env python3
# Date: Nov 2018

"""

""" 

__appname__ = '[xxxx in python]'
__author__ = 'David Scott (david.scott18@imperial.ac.uk)'
__version__ = '0.0.1'
__license__ = "License for this code/program" 

##packages 
import re 

# always include r infront of regex

# create a string
my_string = "a given string"

# find a space in the string (\s)
match = re.search(r'\s', my_string)
print(match) # tells if match was found

# to view match 
match.group()


### another example 
# searches for numeric characters (d)
match = re.search(r'd', my_string)
print(match)


### if statement to know if pattern was matched

MyStr = 'an example' # create a new string

# match any alphanumeric character (w) and 
#       match white space (\s), zero or more times (*)
# i.e any letter followed by a space 
match = re.search(r'\w*\s', MyStr) 

if match:
    print('found a match:', match.group())
else:
    print('did not find a match')


### more examples of regexes 
match = re.search(r'2' , "it takes 2 to tango") # matches number '2' in string
match.group()

match = re.search(r'\d' , "it takes 2 to tango") # \d numeric integer 
match.group()

# match numeric integer (\d) and anything that follows
match = re.search(r'\d.*' , "it takes 2 to tango") 
match.group()

# match white space, alphanumeric character 1 to 3 times, following by a white space
#   i.e any word with 1 to 3 letters
match = re.search(r'\s\w{1,3}\s', 'once upon a time')
match.group()

# match white space then alphanumeric character zero or more times, 
# match end of string
match = re.search(r'\s\w*$', 'once upon a time')
match.group()

### more compact syntex 
# directly return matched group 
# appends .group() to the result

# match letter zero or more times, then white space, 
# then numeric zero or time then a numeric
re.search(r'\w*\s\d.*\d', 'take 2 grams of H20').group()

# match start of a string (^), any number of letters (\w*),
# then any number of any character (.*) followed by space (\s)
re.search(r'^\w*.*\s', 'once upon a time').group()

## blackbird example re.findall ####

# use ? to terminate *, + and {} at first found instance of pattern
re.search(r'^\w*.*?\s', 'once upon a time').group()

## to illustrate, match a HTML tag
# + is 'greedy'
re.search(r'<.+>', 'This is a <EM.first</EM> test').group()
# + is 'lazy'
re.search(r'<.+?>', 'This is a <EM>first</EM> test').group()

###
# use \ before . t find a literal .
re.search(r'\d*\.?\d*','1432.75+60.22i').group()

# match any characer lister ([ATGC]) as many times (+)
re.search(r'[AGTC]+', 'the sequence ATTCGT').group()

# 
re.search(r'\s+[A-Z]{1}\w+\s\w+', 'The bird-shit frog''s name is Theloderma asper').group()

### search email address 
MyStr = 'David Scott, david.scott18@imperial.ac.uk, Systems biology and ecological theory'
match = re.search(r"[\w\s]+,\s[\w\.@]+,\s[\w\s&]+",MyStr)
match.group()
# [\w\s] ensures any combination of word characters and spaces is found


MyStr = 'David Scott, d-scott@imperial.ac.uk, Systems biology and ecological theory'
match = re.search(r"[\w\s]+,\s[\w\.-]+@[\w\.-]+,\s[\w\s&]+",MyStr)
match.group()

### grouping regex patterns 
MyStr = 'David Scott, d.scott@imperial.ac.uk, Systems biology and ecological theory'
match = re.search(r"[\w\s]+,\s[\w\.-]+@[\w\.-]+,\s[\w\s&]+",MyStr)
match.group()

# without grouping regex 
match.group(0)

# create groups - used for extractign specific patterns 
match = re.search(r"([\w\s]+),\s([\w\.-]+@[\w\.-]+),\s([\w\s&]+)",MyStr)
if match:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

##### find all matches 
# re.findall() 
# returns al lmatches as list of strings 

MyStr = "Samraat Pawar, s.pawar@imperial.ac.uk,\
 Systems biology and ecological theory; Another academic,\
  a-academic@imperial.ac.uk, Some other stuff thats equally boring; \
  Yet another academic, y.a_academic@imperial.ac.uk,\
   Some other stuff thats even more boring"

emails = re.findall(r'[\w\.-]+@[\w\.-]+', MyStr)
for email in emails:
    print(email)

### finding in files 
f = open('../Data/TestOaksData.csv', 'r')
found_oaks = re.findall(r"Q[\w\s].*\s", f.read())

found_oaks

for name in found_oaks:
    print(name.replace(",",""))

### groups within multiple matches 
MyStr = "Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and ecological theory; Another academic, a.academic@imperial.ac.uk, Some other stuff thats equally boring; Yet another academic, y.a.academic@imperial.ac.uk, Some other stuff thats even more boring"

found_matches = re.findall(r"([\w\s]+),\s([\w\.-]+@[\w\.-]+)", MyStr)
found_matches

for item in found_matches:
    print(item)

#### Extracting text from wbpages 
import urllib3 

conn = urllib3.PoolManager() # open a connection
r = conn.request('GET', 'https://www.imperial.ac.uk/silwood-park/academic-staff/') 
webpage_html = r.data #read in the webpage's contents

type(webpage_html)

My_Data  = webpage_html.decode()
#print(My_Data)

pattern = r"Dr\s+\w+\s+\w+"
regex = re.compile(pattern) # example use of re.compile(); you can also ignore case  with re.IGNORECASE 
for match in regex.finditer(My_Data): # example use of re.finditer()
    print(match.group())

### replacing text 
New_Data = re.sub(r'\t'," ", My_Data) # replace all tabs with a space
print(New_Data)
