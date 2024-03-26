def loe_ankeet(fail:str)->any:
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    for line in fail:
        n=line.find(":")
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip)

    fail.close()
    return kus,vas
