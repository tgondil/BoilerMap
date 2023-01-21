import pandas as pd
import plotly.graph_objects as go
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
df = pd.read_excel('data.xlsx', header=3)
df2 = pd.read_csv('death.csv',
                   dtype={"fips": str}, header = 4)

counties["features"][0]

import plotly.express as px

fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color_discrete_sequence=['#EF553B'], zoom=3, height=750, color='Total reported direct emissions')
carbon = px.scatter_mapbox(df.dropna(subset=['CO2 emissions (non-biogenic) ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='CO2 emissions (non-biogenic) ', zoom=3, height=750)
nitrogen = px.scatter_mapbox(df.dropna(subset=['Nitrous Oxide (N2O) emissions ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='Nitrous Oxide (N2O) emissions ', zoom=3, height=750)
methane = px.scatter_mapbox(df.dropna(subset=['Methane (CH4) emissions ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='Methane (CH4) emissions ', zoom=3, height=750)
hfc = px.scatter_mapbox(df.dropna(subset=['HFC emissions']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='HFC emissions', zoom=3, height=750)
sf = px.scatter_mapbox(df.dropna(subset=['SF6 emissions']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='SF6 emissions', zoom=3, height=750)
#death = px.choropleth_mapbox(df2, geojson=counties, locations=' FIPS', color='Average Annual Count', zoom=3, height=750,
#mapbox_style="carto-positron", center={"lat": 33.33012299999999, "lon": -81.08463033333332},)

#death.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

death = px.choropleth_mapbox(df2, geojson=counties, locations='fips', color='Count',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )


fig.add_trace(carbon['data'][0])
fig.add_trace(nitrogen['data'][0])
fig.add_trace(methane['data'][0])
fig.add_trace(hfc['data'][0])
fig.add_trace(sf['data'][0])

fig.update_layout(mapbox_style="light", mapbox_accesstoken='pk.eyJ1IjoiYXNod2luZGVzaCIsImEiOiJjbGQ2Nm9jZ2UwZHhyM3FzZGhmZ2U5bGNrIn0.ShkpAMGCM3RNz0SX3If1CQ', margin={"r":0,"t":0,"l":0,"b":0},)
# fig.update_traces(cluster=dict(enabled=True))

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            active=0,
            type = 'buttons',
            buttons=list([
                dict(label="Total Emissions",
                     method="update",
                     args=[{"visible": [True, False, False, False, False]},
                           {"title": "Total Pollution"}]),
                dict(label="Carbon",
                     method="update",
                     args=[{"visible": [False, True, False, False]},
                           {"title": "Carbon Pollution"}]),
                dict(label="Nitrogen",
                    method="update",
                    args=[{"visible": [False, False, True, False]},
                            {"title": "Nitrogen Pollution"}]),
                dict(label="Methane",
                    method="update",
                    args=[{"visible": [False, False, False, True]},
                            {"title": "Methane Pollution"}]),
                dict(label="HFC",
                    method="update",
                    args=[{"visible": [False, False, False, False, True]},
                            {"title": "HFC Pollution"}]),
                dict(label="SF6",
                    method="update",
                    args=[{"visible": [False, False, False, False, False, True]},
                            {"title": "SF6 Pollution"}]),
                dict(label="Age Adjusted Death Rate",
                     method="update",
                     args=[{"visible": [False, False, False, False, False, False]},
                           {"title": "Age Adjusted Death Rate"}]),
            ]),
        )
    ]
)
fig.show()
death.show()
