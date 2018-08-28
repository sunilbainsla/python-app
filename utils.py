def print_csv(rawsdata):
    for i, row in enumerate(rawsdata.values):
            if i<1:
                print(row)
            else:
                break
def addTotal(rawdata):
    headerVal=rawdata.iloc[0:0,1:37]
    myVal=0
    for i, row in enumerate(headerVal):
        myVal+=rawdata[row]
    return myVal