import csv
with open('height-weight.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    number=filedata[i][1]
    newdata.append(float(number))
n=len(newdata)
sum=0
for x in newdata:
    sum=sum+x
mean=sum/n
print(mean)    