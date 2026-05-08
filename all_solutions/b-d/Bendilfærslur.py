line = input()


if line.count(".") > 0:
    line = line.split(".")
    new_line = ""
    for i in range(len(line)):
        new_line+= line[len(line)-i-1]
        if i != len(line)-1:
            new_line+="."
    
    
    print(new_line+".in-addr.arpa.")
