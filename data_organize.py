lines_seen = set() 
outfile = open("data_voltaire.txt", "w")
for line in open("data.txt", "r"):
    if line.split("|")[0] not in lines_seen: 
        outfile.writelines(line)
        lines_seen.add(line.split("|")[0])
outfile.close()