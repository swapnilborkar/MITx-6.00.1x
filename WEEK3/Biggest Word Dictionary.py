def biggest(aDict):
    if aDict!={}:
        r=aDict.keys()[0]
        i=0
        for k in aDict:
            if len(aDict[k])>i:
                r=k
                i=len(aDict[k])
        return r