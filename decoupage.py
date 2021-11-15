import re
import sys

f = open(sys.argv[1], "r")
# out = open(sys.argv[2], "w")
line_full = []
for line in f:
    line_full.append(line.split())
    if len(line_full) == 3:
        if not line_full[0][0].isupper():
            if re.search("[.!?]", line_full[1][0]):
                if re.search("[A-Z]+[a-z]*$", line_full[2][0]):
                    print(line_full)
        line_full[0] = line_full[1]
        line_full[1] = line_full[2]
        line_full.pop(2)
