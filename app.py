import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from purav import load_data


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

df = load_data()

fig = px.bar(df, x='Dates', y='Up-Time', color='Up-Time', labels={'Up-Time':'Up Time (Hours)'})

app.layout = html.Div(children=[
    html.H1(children='Hello Purav'),

    html.Div(children='''
        Here's you data visualised as you described.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)