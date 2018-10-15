# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.

rainfall_big = [item for item in rainfall if item[1] > 100.0]
print(rainfall_big)

# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm.

rainfall_small = [item for item in rainfall if item[1] < 50.0]
print(rainfall_small)

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 

rainfall_b = set()
for rain in rainfall:
    if rain[1] > 100.0:
        rainfall_b.add(rain)   
print(rainfall_b)

rainfall_s = set()
for rain in rainfall:
    if rain[1] < 50.0:
        rainfall_s.add(rain)
print(rainfall_s)

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
