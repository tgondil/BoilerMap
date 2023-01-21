import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Read data from an xlsx file
df = pd.read_excel('data.xlsx', header=3)

# Create a scatter map
fig = px.scatter_geo(df, lat="Latitude", lon="Longitude", scope='usa', color = 'Total reported direct emissions', hover_name= 'Facility Name')

# Add a button to switch between showing carbon and nitrogen pollution

print(fig.to_dict())

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            active=0,
            type='buttons',
            buttons=list([
                dict(label="Carbon",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title": "Carbon Pollution"}]),
                dict(label="Nitrogen",
                     method="update",
                     args=[{"visible": [False, True]},
                           {'marker': df.loc[:,"Nitrous Oxide (N2O) emissions "]},
                           {"title": "Nitrogen Pollution"}]),
            ]),
        )
    ]
)

fig.show()
