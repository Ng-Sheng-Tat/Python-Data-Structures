# Use words.txt as the file name
fh = open("words.txt")
for line in fh:
    print(line.rstrip().upper())
