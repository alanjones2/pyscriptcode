# Import libraries
import pandas as pd
import plotly.express as px
import js

header = """World CO2 Emissions over Time"""
subheader = "CO2 Emissions tracked over the period 1850 to 2020"
description = """The graph shows the annual emissions of Carbon Dioxide, in tonnes, emitted globally
"""
display(header, target="header")
display(subheader, target="subheader")
display(description, target="description")

df = pd.read_csv('./hadcrutworld.csv')

#plot('Annual CO₂ emissions')

fig = px.line(df, x="Year", y='Annual CO₂ emissions',
              width=1200, height=600,
              template="plotly_white")

graphJSON = fig.to_json()
js.plot(graphJSON,"chart1")
