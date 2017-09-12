## open file 'mbox-short.txt', find the 'From' lines and extract the hour from
## the sent time. build a histogram with k:v where we hav the hour 0-23 and the 
## number of emails sent in each hour.
name = input("Enter a file name: ")
from_lines = [line.strip("\n") for line in open(name, 'r')
             if line.startswith("From ")]
hour_gram = {}
tuples_list = []

for line in from_lines:
    timepiece = line.split()[5]
    hour = timepiece.split(":")[0]
    hour_gram[hour] = hour_gram.get(hour, 0) + 1

for key in hour_gram:
    tuples_list.append((key, hour_gram[key]))

sorted_tuples_list = sorted(tuples_list)

for item in sorted_tuples_list:
    print(item[0], item[1])