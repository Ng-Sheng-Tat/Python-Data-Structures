name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
count = 0
fh = open(name)
mylist = []
counts = {}
for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        count += 1
        curline = line.split()

        mylist.append(curline[5])
mylist.sort()
# print(mylist)
for key in mylist:
    # print(key)
    if key[:2] in counts:
        counts[key[:2]] = counts[key[:2]] + 1
    else:
        counts[key[:2]] = 1
# print(counts)
for key, val in counts.items():
    print(key + " " + str(val))
