import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Read data from an xlsx file
df = pd.read_excel('data.xlsx', header=3)

# Group the data by 'State' and calculate the sum of 'CO2 emissions (non-biogenic)' for each group
df_grouped = df.groupby('State')['CO2 emissions (non-biogenic) '].sum().reset_index()

# Create a Choropleth map of the United States
fig = px.choropleth(df_grouped,
                    locations='State',  # Column containing the state names
                    locationmode='USA-states',  # Set the location mode to USA-states
                    color='CO2 emissions (non-biogenic) ',  # Column containing the data to be plotted
                    color_continuous_scale='Viridis',  # Color scale to use
                    title='CO2 emissions (non-biogenic) by State',
                    scope='usa')
fig.show()