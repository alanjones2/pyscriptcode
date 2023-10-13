# Import libraries
import pandas as pd
import plotly.express as px
import js

header = """Global Temperature Change"""
subheader = "Global Temperature changes over the last few centuries"
description = """The graph shows the increase in temperature year on year.
The data spans the years 1880 to 2023 and includes temperature anomalies for each month of each year as well as average temperatures for groups of months such as the June through August.
"""
display(header, target="header")
display(subheader, target="subheader")
display(description, target="description")

df = pd.read_csv('./globaltemp.csv', skiprows=1)

period = 'JJA'
fig = px.bar(df, x='Year', y = period, color=period, title = "", 
       color_continuous_scale='inferno', template='plotly_white', width=700, height=400)

graphJSON = fig.to_json()
js.plot(graphJSON,"chart1")
