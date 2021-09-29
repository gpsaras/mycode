#!/usr/bin/env python3
## Ask user for name of file to be read in
filename = input("What is the name of file to be read in?:")

## create file object in "r"ead mode
with open(filename, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
## print the length of the file
print(len(configlist))

