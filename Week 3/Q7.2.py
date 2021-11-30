# Use the file name mbox-short.txt as the file name
fname = "mbox-short.txt"
with open(fname, 'r') as fh:
    count = 0
    val = 0
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        line = line.strip()
        val += float(line[-6:])
        count += 1
print("Average spam confidence:", val/count)
