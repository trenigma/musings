## open the file 'mbox-short.txt', find the lines containing 
## "X-DSPAM-Confidence:" and slice the numeric value from the end.
## convert the values to floats and give back an average
fname = input('Enter file name: ')
fh = open(fname)
count = 0
tot = 0
fin = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    num = float(line[21:])
    tot = num + tot
    fin = tot / count
print("Average spam confidence:", fin)
