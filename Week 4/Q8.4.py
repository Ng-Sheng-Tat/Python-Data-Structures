fname = "romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    xs = line.split()
    for x in xs:
        if x not in lst:
            lst.append(x)

lst.sort()
print(lst)
