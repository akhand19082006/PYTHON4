import pandas as pd
import plotly.express as ps
df=pd.read_csv("data2.csv")
fig=ps.scatter(df,x="student_id",y="level",color="attempt",size="attempt")
fig.show()