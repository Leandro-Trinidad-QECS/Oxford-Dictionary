
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
    lines_seen = set()
    url1 = letter + ".txt"
    outFile = open(url1,"w+")
    url = letter + "_text.txt"
    for line in open(url,"r"):
        if line not in lines_seen:
            outFile.write(line)
            lines_seen.add(line)
    print(letter + " Finished")
outFile.close()
