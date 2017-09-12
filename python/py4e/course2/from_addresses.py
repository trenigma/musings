## find all the lines with 'From' at the beginning, keep a count. split
## then print the lines along with a count
han = open('mbox-short.txt')
count = 0
for line in han:
    if not line.startswith("From ") : continue
    count = count + 1
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[1])
print("There were", count, "lines in the file with From as the first word")