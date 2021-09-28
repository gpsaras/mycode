#!/usr/bin/env python3

message = 'Your grade is an:  '
## Ask the user to enter a numeric score
score = int(input("What is your score?"))

# returns a letter grade from a score input by the user
if score >= 90:
    message = message + 'A'
elif score >= 80:
    message = message + 'B'
elif score  >= 70:
    message = message + 'C'
elif score  >= 60:
    message = message + 'D'
else:
    message = message + 'F'
print(message)

