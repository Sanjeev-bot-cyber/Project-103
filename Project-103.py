import pandas as pd
import plotly.express as px
df = pd.read_csv("Copy+of+data+-+data.csv")
f = px.scatter(df, x = "date", y = "cases", color = "country")
f.show()