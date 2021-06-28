import plotly.figure_factory as pf
import pandas as pd
import csv
import statistics
import random
import plotly.graph_objects as pg

df=pd.read_csv("studentMarks.csv")
tem=df["Math_score"].tolist()

fig=pf.create_distplot([tem],["Math Score"])
fig.show()

mean=statistics.mean(tem)
sd=statistics.stdev(tem)
median=statistics.median(tem)
mode=statistics.mode(tem)
print(mean,median,mode,sd)

def randommean(counter):
    data=[]
    for i in range (0,counter):
        randomindex=random.randint(0,len(tem)-1)
        value=tem[randomindex]
        data.append(value)
    mean=statistics.mean(data)
    return mean
meanlist=[]
for i in range(0,1000):
    setofmean=randommean(100)
    meanlist.append(setofmean)
sd=statistics.stdev(meanlist)
mean=statistics.mean(meanlist)
print("mean: ",mean)

#fig=pf.create_distplot([meanlist],["STUDENT MARKS"],show_hist=False)
#fig.add_trace(pg.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean of sample"))
#fig.show()

sd1start,sd1end=mean-sd,mean+sd
sd2start,sd2end=mean-(2*sd),mean+(2*sd)
sd3start,sd3end=mean-(2*sd),mean+(3*sd)

df=pd.read_csv("data1.csv")
tem1=df["Math_score"].tolist()
mean1=statistics.mean(tem1)
sd1=statistics.stdev(tem1)

df=pd.read_csv("data2.csv")
tem2=df["Math_score"].tolist()
mean2=statistics.mean(tem2)
sd2=statistics.stdev(tem2)

df=pd.read_csv("data3.csv")
tem3=df["Math_score"].tolist()
mean3=statistics.mean(tem3)
sd3=statistics.stdev(tem3)

fig=pf.create_distplot([meanlist],["STUDENT MARKS"],show_hist=False)
fig.add_trace(pg.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean of sample"))
fig.add_trace(pg.Scatter(x=[mean1,mean1],y=[0,0.20],mode="lines",name="mean of student with tablet"))
fig.add_trace(pg.Scatter(x=[mean2,mean2],y=[0,0.20],mode="lines",name="mean of student getting extra classes"))
fig.add_trace(pg.Scatter(x=[mean3,mean3],y=[0,0.20],mode="lines",name="mean of student with fun Sheets to practise"))

fig.add_trace(pg.Scatter(x=[sd1end,sd1end],y=[0,0.20],mode="lines",name="sd1end"))
fig.add_trace(pg.Scatter(x=[sd2end,sd2end],y=[0,0.20],mode="lines",name="sd2end"))
fig.add_trace(pg.Scatter(x=[sd3end,sd3end],y=[0,0.20],mode="lines",name="sd3end"))
fig.show()
zscore=(mean1-mean)/sd
print("Zscore: " ,zscore)

zscore1=(mean2-mean)/sd
print("Zscore: " ,zscore1)

zscore2=(mean3-mean)/sd
print("Zscore: " ,zscore2)
