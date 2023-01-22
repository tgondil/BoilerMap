import pandas as pd
import plotly.graph_objects as go
df = pd.read_excel('data.xlsx', header=3)
dfhw = pd.read_csv('heatwaves.csv')

import plotly.express as px

fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color_discrete_sequence=['#EF553B'], zoom=3, height=700, color='Total reported direct emissions', range_color=[0, 1_000_000])

carbon = px.scatter_mapbox(df.dropna(subset=['CO2 emissions (non-biogenic) ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='CO2 emissions (non-biogenic) ', zoom=3, height=700, range_color=[0, 500_000])
nitrogen = px.scatter_mapbox(df.dropna(subset=['Nitrous Oxide (N2O) emissions ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='Nitrous Oxide (N2O) emissions ', zoom=3, height=700)
methane = px.scatter_mapbox(df.dropna(subset=['Methane (CH4) emissions ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='Methane (CH4) emissions ', zoom=3, height=700)
hfc = px.scatter_mapbox(df.dropna(subset=['HFC emissions']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='HFC emissions', zoom=3, height=700)
sf = px.scatter_mapbox(df.dropna(subset=['SF6 emissions']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County", "Industry Sector"],
                        color='SF6 emissions', zoom=3, height=700)
hwfre = px.density_mapbox(dfhw, lat='Latitude', lon='Longitude', z='Intensity Change', radius=50, center=dict(lat=39.49, lon=41.43), zoom =3, mapbox_style="stamen-terrain",)

fig.add_trace(carbon['data'][0])
fig.add_trace(nitrogen['data'][0])
fig.add_trace(methane['data'][0])
fig.add_trace(hfc['data'][0])
fig.add_trace(sf['data'][0])
fig.add_trace(hwfre['data'][0])

fig.update_layout(mapbox_style="light", mapbox_accesstoken='pk.eyJ1IjoiYXNod2luZGVzaCIsImEiOiJjbGQ2Nm9jZ2UwZHhyM3FzZGhmZ2U5bGNrIn0.ShkpAMGCM3RNz0SX3If1CQ', margin={"r":0,"l":0,"b":0},)
# fig.update_traces(cluster=dict(enabled=True))

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            active=0,
            type = 'dropdown',
            y = 1,
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
                # dict(label="HeatWaves Frequency",
                #     method="update",
                #     args=[{"visible": [False, False, False, False, False, False, True]},
                #             {"title": "HeatWaves Frequency"}]),
            ]),
        ),
        go.layout.Updatemenu(
            active=0,
            type = 'dropdown',
            y=0.9,
            buttons=list([
                dict(label="HeatWaves",
                     method="update",
                     args=[{"visible": [False, False, False, False, False, False, True]},
                           {"title": "HeatWaves Frequency"}]),]))
    ]
)
fig.show()
