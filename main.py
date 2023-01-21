import pandas as pd
import plotly.express as px

# Read data from an xlsx file
df = pd.read_excel('data.xlsx', header=3)

fig = px.scatter_geo(df, lat="Latitude", lon="Longitude", scope='usa')
fig.show()