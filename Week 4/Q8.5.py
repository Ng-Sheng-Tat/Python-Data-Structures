fname = "mbox-short.txt"
count = 0
fh = open(fname)
for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        count += 1
        curline = line.split()

        print(curline[1])

print("There were", count, "lines in the file with From as the first word")
