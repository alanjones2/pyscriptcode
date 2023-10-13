# Import libraries
import pandas as pd
import plotly.express as px
import js

header = """Global Temperature Change and CO2 Emissions"""
subheader = "Global Temperature and CO2 emissions changes over the last few centuries"
description = """The graph shows the increase in temperature year on year.
The data spans the years 1880 to 2023 and includes temperature anomalies for each month of each year as well as average temperatures for groups of months such as the June through August.
The CO2 emissions data spans a similar period of time and you can see a correlation between the two sets of data.
"""
display(header, target="header")
display(subheader, target="subheader")
display(description, target="description")

df = pd.read_csv('./globaltemp.csv', skiprows=1)

period = 'JJA'
fig = px.bar(df, x='Year', y = period, color=period, title = "", 
       color_continuous_scale='inferno', template='plotly_white', width=600, height=400)

graphJSON = fig.to_json()
js.plot(graphJSON,"chart1")

df = pd.read_csv('./hadcrutworld.csv')

#plot('Annual CO₂ emissions')

fig = px.line(df, x="Year", y='Annual CO₂ emissions',
              width=600, height=400,
              template="plotly_white")

graphJSON = fig.to_json()
js.plot(graphJSON,"chart2")
