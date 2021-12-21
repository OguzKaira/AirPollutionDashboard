import dash
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output

# Read CSV File
data = pd.read_csv("death-rates-from-air-pollution.csv")

# Getting Column from Dataset
data = data.iloc[:, 0:4]

# Delete Irevelent Column
data = data.drop(["Code"], axis=1)

# Delete NA Rows
data = data.dropna()

# Change Column Names
data = data.rename({"Entity": "Country", "Year": "Year",
                   "Air pollution (total) (deaths per 100,000)": "Deaths"}, axis=1)

# initialising dash app
app = dash.Dash()

# Empty Graph
def populationGraph():

    graph = go.Figure()

    # Return Plot
    return graph


# Layout of your web app
app.layout = html.Div(id="ScatterDashboard", children=[
    html.H2(id="H2", children="POPULATION DASHBOARD", style={'textAlign': 'center'}),
    dcc.Dropdown(id='dropdown',
                 options=[
                    {'label': 'United Kingdom (UK)', 'value': 'United Kingdom'},
                    {'label': 'United States (US)', 'value': 'United States'},
                    {'label': 'United Arab Emirates (UAE)', 'value': 'United Arab Emirates'},
                ]),
                dcc.Graph(id="scatterPlot", figure=populationGraph())])


# Apply User Choice to Graph
@app.callback(Output(component_id='scatterPlot', component_property='figure'),
              [Input(component_id='dropdown', component_property='value')])
def graph_update(dropdown_value):
    targetRow = data[data['Country'] == '{}'.format(dropdown_value)]
    fig = go.Figure([go.Scatter(x=targetRow.Year, y=targetRow.Deaths)
                     ])

    fig.update_layout(title='Pollution Deaths in {}'.format(dropdown_value),
                      xaxis_title='Country',
                      yaxis_title='Dates'
                      )
    return fig


# Start Local Server
if __name__ == '__main__':
    app.run_server()
