import dash
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc

# Read CSV File
data = pd.read_csv("PollutionDataset.csv")

# initialising dash app
app = dash.Dash()

# Population Bar Function
def populationBar():

    graph = go.Figure([go.Scatter(x = data["Country"] , y = data["Deaths"])])

    graph.update_layout(title = "Deaths Caused by Pollution",
                        xaxis_title = 'Countries',
                        yaxis_title = 'Deaths'
                       )
    # Return Plot
    return graph

# Add Html Code and Graph in Layout
app.layout = html.Div(id = "BarDashboard", children = [
        html.H2(id = "H2", children = "POPULATION DASHBOARD", style = {'textAlign':'center'}), dcc.Graph(id = "scatterPlot", figure = populationBar())])

# Start Local Server
if __name__ == '__main__': 
    app.run_server()
