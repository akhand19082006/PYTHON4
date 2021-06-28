from collections import Counter
import csv
with open('height-weight.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    number=filedata[i][1]
    newdata.append(float(number))
data=Counter(newdata)
moderange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,accourance in data.items():
    if 50 < float(height) < 60:
        moderange["50-60"]+=accourance
    elif 60 < float(height) < 70:
        moderange["60-70"]+=accourance
    elif 70 < float(height) < 80:
        moderange["70-80"]+=accourance
a,b=0,0
for range,occourance in moderange.items():
    if occourance>b:
        a,b=[int(range.split("-")[0]),int(range.split("-")[1])],occourance
mode=float((a[0]+a[1])/2)
print(mode)