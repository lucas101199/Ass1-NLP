import re
import sys

regex_exp = "([%$]|\w+\-\w+|\d+\.\d+|(\w+)*(\.[A-Z])+\.|[,;:.!?\"]|\w+)"
for line in sys.stdin:
    for token in re.findall(regex_exp, line.strip()):
        print(token[0])
