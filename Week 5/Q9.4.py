fname = "mbox-short.txt"
count = 0
fh = open(fname)
mylist = []
counts = {}
for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        count += 1
        curline = line.split()

        mylist.append(curline[1])
for key in mylist:
    # print(key)
    if key in counts:
        counts[key] = counts[key] + 1
    else:
        counts[key] = 1

dummy = list(counts.items())
# print(type(dummy))
maxnum = 0
for x in dummy:
    if x[1]>maxnum:
        maxnum = x[1]
        index = dummy.index((x[0], maxnum))
# print(index)
# print(maxnum)
print(dummy[index][0], dummy[index][1])

## Submitted Code
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
count = 0
mylist = []
counts = {}
for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        count += 1
        curline = line.split()

        mylist.append(curline[1])
for key in mylist:
    # print(key)
    if key in counts:
        counts[key] = counts[key] + 1
    else:
        counts[key] = 1

dummy = list(counts.items())
# print(type(dummy))
maxnum = 0
for x in dummy:
    if x[1]>maxnum:
        maxnum = x[1]
        index = dummy.index((x[0], maxnum))
# print(index)
# print(maxnum)
print(dummy[index][0], dummy[index][1])
