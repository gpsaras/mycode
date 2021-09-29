#!/usr/bin/env python3
## create file object in "r"ead mode

Counter = 0
with open("vlanconfig.cfg", "r") as configfile:
    ## read file line by line

# Reading from file
    Content = configfile.read()
    CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

print("This is the number of lines in the file")
print(Counter)
    
## file was just auto closed (no more indenting)


