import pandas as pd
import plotly.graph_objects as go
df = pd.read_excel('data.xlsx', header=3)

import plotly.express as px

fig = px.scatter_mapbox(df.dropna(subset=['CO2 emissions (non-carbiogenic) ', 'Nitrous Oxide (N2O) emissions ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County"],
                        color_discrete_sequence=['#EF553B'], zoom=3, height=750)

carbon = px.scatter_mapbox(df.dropna(subset=['CO2 emissions (non-biogenic) ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County"],
                        color='CO2 emissions (non-biogenic) ', zoom=3, height=750)
nitrogen = px.scatter_mapbox(df.dropna(subset=['Nitrous Oxide (N2O) emissions ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County"],
                        color='Nitrous Oxide (N2O) emissions ', zoom=3, height=750)
methane = px.scatter_mapbox(df.dropna(subset=['Nitrous Oxide (N2O) emissions ']), lat="Latitude", lon="Longitude", hover_name="City", hover_data=["State", "County"],
                        color='Methane (CH4) emissions ', zoom=3, height=750)

fig.add_trace(figcar['data'][0])
fig.add_trace(fignit['data'][0])

fig.update_layout(mapbox_style="light", mapbox_accesstoken='pk.eyJ1IjoiYXNod2luZGVzaCIsImEiOiJjbGQ2Nm9jZ2UwZHhyM3FzZGhmZ2U5bGNrIn0.ShkpAMGCM3RNz0SX3If1CQ', margin={"r":0,"t":0,"l":0,"b":0},)
fig.update_traces(cluster=dict(enabled=True))

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            active=0,
            type = 'buttons',
            buttons=list([
                dict(label="Carbon",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title": "Carbon Pollution"}]),
                dict(label="Nitrogen",
                    method="update",
                    args=[{"visible": [True, False]},
                            {"title": "Nitrogen Pollution"}]),
            ]),
        )
    ]
)
fig.show()
