import pandas as pd
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls
dfhw = pd.read_csv('heatwaves.csv')

import plotly.express as px

username = 'mlavrenk'
api_key = 'flp8Ee4Nhl0cInQtZ6rt'

chart_studio.tools.set_credentials_file(username=username, api_key= api_key)

fig = px.density_mapbox(dfhw, lat='Latitude', lon='Longitude', z='Change', radius=50, center=dict(lat=39.49, lon=-98.95734), zoom =3, mapbox_style="stamen-terrain",)
fig.update_layout(mapbox_style="light", mapbox_accesstoken='pk.eyJ1IjoiYXNod2luZGVzaCIsImEiOiJjbGQ2Nm9jZ2UwZHhyM3FzZGhmZ2U5bGNrIn0.ShkpAMGCM3RNz0SX3If1CQ', margin={"r":0,"l":0,"b":0,"t":0},)
duration = px.density_mapbox(dfhw.dropna(subset=['Duration Change']), lat='Latitude', lon='Longitude', z='Duration Change', radius=50, center=dict(lat=39.49, lon=-98.95734), zoom =3, mapbox_style="stamen-terrain", labels={'Duration Change'})
fig.add_trace(duration['data'][0])

fig.update_coloraxes(colorbar_yanchor="top", colorbar_xanchor="left", colorbar_x=0, colorbar_y=1)

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            active=0,
            type = 'dropdown',
            y = 1,
            x=0.7,
            buttons=list([
                dict(label="Intensity Change in Heat Waves",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title": "Intensity Change"}]),

                dict(label="Duration Change in Heat Waves",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title": "Duration Change"}]),
                          ]),
        ),
    ]
)

py.plot(fig, filename = 'heat waves2', auto_open = True)

fig.show()