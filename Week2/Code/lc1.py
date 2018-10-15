birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

# (2) Now do the same using conventional loops (you can shoose to do this 
# before 1 !). 

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS.

##1## list comprehensions ##

birds_latinname = [item[0] for item in birds]
print (birds_latinname)

birds_commonname = [item[1] for item in birds]
print (birds_commonname)

birds_bodymass = [item[2] for item in birds]
print (birds_bodymass)

##2## loops ##

# latin name of species
birds_latin_loops = set()
for item in birds:
    if item[0]:
        birds_latin_loops.add(item[0])
print(birds_latin_loops)

# common names of species in "birds" list of tuples
birds_common_loops = set()
for item in birds:
    if item[1]:
        birds_common_loops.add(item[1])
print(birds_common_loops)

# body mass of birds
birds_mass_loops = set()
for item in birds:
    if item[2]:
        birds_mass_loops.add(item[2])
print(birds_mass_loops)