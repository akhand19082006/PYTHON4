import pandas as pd 
import plotly.express as ps 
df=pd.read_csv("line_chart.csv")
fig=ps.line(df,x="Year",y="Per capita income",color="Country",title='Chart')
fig.show() 
