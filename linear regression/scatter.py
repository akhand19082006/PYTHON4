import pandas as pd
import plotly.express as ps
df=pd.read_csv("data.csv")
fig=ps.scatter(df,x="Population",y="Per capita",color="Country",size="Percentage",size_max=60)
fig.show()