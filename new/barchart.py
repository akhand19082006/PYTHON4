import pandas as pd
import plotly.express as ps
df=pd.read_csv("data.csv")
fig=ps.bar(df,x="Country",y="InternetUsers")
fig.show()