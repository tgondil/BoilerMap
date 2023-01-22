import pandas as pd
import plotly.graph_objects as go
df = pd.read_excel('data.xlsb')
dfhw = pd.read_csv('heatwaves.csv')

import plotly.express as px

fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color_discrete_sequence=['#EF553B'], zoom=3, height=800, color='Total reported direct emissions', range_color=(0, 1_000_000))

carbon = px.scatter_mapbox(df.dropna(subset=['CO2 emissions (non-biogenic) ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='CO2 emissions (non-biogenic) ', zoom=3, height=800, range_color=[0, 500_000])
nitrogen = px.scatter_mapbox(df.dropna(subset=['Nitrous Oxide (N2O) emissions ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='Nitrous Oxide (N2O) emissions ', zoom=3, height=800)
methane = px.scatter_mapbox(df.dropna(subset=['Methane (CH4) emissions ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='Methane (CH4) emissions ', zoom=3, height=800)
hfc = px.scatter_mapbox(df.dropna(subset=['HFC emissions']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='HFC emissions', zoom=3, height=800)

fig.add_trace(carbon['data'][0])
fig.add_trace(nitrogen['data'][0])
fig.add_trace(methane['data'][0])
fig.add_trace(hfc['data'][0])
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls

username = 'tgondil'
api_key = 'EU50O1jwO3ZIpIRQL7k8'

fig.update_layout(mapbox_style="light", mapbox_accesstoken='pk.eyJ1IjoiYXNod2luZGVzaCIsImEiOiJjbGQ2Nm9jZ2UwZHhyM3FzZGhmZ2U5bGNrIn0.ShkpAMGCM3RNz0SX3If1CQ', margin={"r":0,"l":0,"b":0},)
# fig.update_traces(cluster=dict(enabled=True))

fig.update_coloraxes(colorbar_orientation="h", colorbar_yanchor="top", colorbar_y=0)

fig.update_layout(
    updatemenus=[   
        go.layout.Updatemenu(
            active=0,
            type = 'dropdown',
            y = 1.1,
            x = 0.5,
            buttons=list([
                dict(label="Total Emissions",
                     method="update",
                     args=[{"visible": [True, False, False, False, False]},
                           {"title": "Total Pollution", "coloraxis.cmin": 0, "coloraxis.cmax": 1_000_000}]),
                dict(label="Carbon",
                     method="update",
                     args=[{"visible": [False, True, False, False]},
                           {"title": "Carbon Pollution","coloraxis.cmin": 0, "coloraxis.cmax": 500_000}]),
                dict(label="Nitrogen",
                    method="update",
                    args=[{"visible": [False, False, True, False]},
                            {"title": "Nitrogen Pollution", "coloraxis.cmin": 0, "coloraxis.cmax": 5_000}]),
                dict(label="Methane",
                    method="update",
                    args=[{"visible": [False, False, False, True]},
                            {"title": "Methane Pollution", "coloraxis.cmin": 0, "coloraxis.cmax": 100_000}]),
                dict(label="HFC",
                    method="update",
                    args=[{"visible": [False, False, False, False, True]},
                            {"title": "HFC Pollution", "coloraxis.cmin": 0, "coloraxis.cmax": 100_000}]),
            ]),
        ),
    ]
)

py.plot(fig, filename = 'heat waves', auto_open = True)

fig.show()
