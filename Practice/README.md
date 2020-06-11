Progress
---

- [x] Question 1  | Level 1

Question:

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Solution:

```
print("Number(s) divisible by 7 but not 5 in the range 2000, 3200 -\n")
number = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        number.append(str(i))
print(",".join(number))
```
- [ ] Question 2  | Level 1
- [ ] Question 3  | Level 1
- [ ] Question 4  | Level 1
- [ ] Question 5  | Level 1
- [ ] Question 6  | Level 2
- [ ] Question 7  | Level 2
- [ ] Question 8  | Level 2
- [ ] Question 9  | Level 2
- [ ] Question 10 | Level 2
