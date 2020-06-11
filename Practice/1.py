#!/usr/bin/env python3

__author__ = "Jugal Kishore"
__version__ = "1.0"


# Display numbers divisible by 7 but not 5 in the range 2000, 3200
print("Number(s) divisible by 7 but not 5 in the range 2000, 3200 -\n")
number = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        number.append(str(i))
print(",".join(number))
