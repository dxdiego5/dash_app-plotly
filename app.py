from dash import Dash, html, dcc
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
# import dash_core_components as dcc
import pandas as pd


FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY, FONT_AWESOME])

app.config["suppress_callback_exceptions"] = True
server = app.server
app.scripts.config.serve_locally = True