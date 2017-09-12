## open the file 'mbox-short.txt', build a dictionary of senders. split the
## 'From' lines and store the addresses in the dict. find the top sender and print
## their address along with the number of times their address showed up as a sender
name = input("Enter a file name: ")
froms = [line.strip('\n') for line in open(name, 'r')
         if line.startswith("From ")]
froms_dict = {}

for line in froms:
    words = line.split()
    froms_dict[words[1]] = froms_dict.get(words[1], 0) + 1

most = 0
topdog = None
for person in froms_dict:
    if froms_dict[person] > most:
        most = froms_dict[person]
        topdog = person

print(topdog, froms_dict[topdog])
