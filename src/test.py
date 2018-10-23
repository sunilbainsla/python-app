from calendar import monthrange

def getNoOfDays(daterange1):
    mylist = daterange1.split('-')
    year=int(mylist[0])
    month=int(mylist[1].strip('0'))
    return monthrange(year,month)[1]

ss=getNoOfDays('2018-08-01')
round(87446.4797963877/781200)
print(int(ss())