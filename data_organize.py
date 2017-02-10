lines_seen = set() 
outfile = open("data_voltaire.txt", "w")
for line in open("data.txt", "r"):
    if line not in lines_seen: 
        outfile.write(line)
        lines_seen.add(line)
outfile.close()