import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import quandl
import plotly.figure_factory as ff
import matplotlib as mpl
import plotly.plotly as py

from pplots import *
from pcode import *

app=dash.Dash()

app.css.append_css({"external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.title="ApPlotly"

app.layout=html.Div([


	html.Div([html.H1(children="ApPlotly", style={"color":"maroon", "text-align":"center", "font-family":"cursive",
		"font-weight":"bold", "font-size":"60px",})],
		className="twelve columns"),


	html.Div([
			html.Div([dcc.Dropdown(
				id = 'dropdown',
				options=[
	            {'label': 'Simple scatter plot', 'value': 1},
	            {'label': 'Styled scatter plot', 'value': 2},
	            {'label': 'Multiple scatter plot', 'value': 3},
	            {'label': 'Simple line chart', 'value': 4},
	            {'label': 'Line with Scatter', 'value': 5},
	            {'label': 'Dashed/dotted lines', 'value': 6},
	            {'label': 'Simple pie chart', 'value': 7},
	            {'label': 'Styled pie chart', 'value': 8},
	            {'label': 'Donuts type pie chart', 'value': 9},
	            {'label': 'Simple bar chart', 'value': 10},
	            {'label': 'Grouped/stacked bar chart', 'value': 11},
	            {'label': 'Simple vertical histogram', 'value': 12},
	            {'label': 'Simple horizontal histogram', 'value': 13},
	            {'label': 'Overlaid histograms', 'value': 14},
	            {'label': 'Simple vertical box plot', 'value': 15},
	            {'label': 'Simple horizontal box plot', 'value': 16},
	            {'label': 'Simple table', 'value': 17},
	            {'label': 'Styled table', 'value': 18},
	            {'label': 'Pandas Scatter plot', 'value': 19},
	            {'label': 'Pandas Histogram (absolute values)', 'value': 20},
	            {'label': 'Pandas Histogram (percentage changes)', 'value': 21},
	            {'label': 'Pandas Box plot', 'value': 22},
	            {'label': 'Pandas Corr plot', 'value': 23}

	            ], placeholder='Please, select a plot'),
			
			html.Button(id='submit', n_clicks=0, children='Submit'),
			], className="four columns")]),

	html.Div([
			html.Div([
			dcc.Graph(id="plot1")],
			className="six columns"),

			html.Div([
			dcc.SyntaxHighlighter(id="syntax1")],
			className="six columns"),

			], className="twelve columns"),


	html.Div([
			html.Div("red"),
			html.Div([dcc.Slider(id = 'red_range', min=0, max=255, value=200)],
			className="twelve columns"),	
			], className="twelve columns"),
		
	html.Div([
			html.Div("blue"),
			html.Div([dcc.Slider(id = 'blue_range', min=0, max=255, value=200)],
			className="twelve columns"),	
			], className="twelve columns"),

	html.Div([
			html.Div("green"),
			html.Div([dcc.Slider(id = 'green_range', min=0, max=255, value=200)],
			className="twelve columns"),	
			
			], className="twelve columns")
])

    


#dropdown plot

@app.callback(
    Output(component_id='plot1', component_property='figure'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='dropdown', component_property='value'),
    State(component_id='red_range', component_property='value'),
	State(component_id='green_range', component_property='value'),
	State(component_id='blue_range', component_property='value')])
	

def update_graph(clicks, input_value1, red, green, blue):
	print(input_value1)
	color="rgba("+str(red)+","+str(green)+","+str(blue)+",0.5)"
	if input_value1==1:
		return make_sp1(color)
	if input_value1==2:
		return make_sp2(color)
	if input_value1==3:
		return make_sp3(color)
	if input_value1==4:
		return make_sl1(color)
	if input_value1==5:
		return make_sl2(color)
	if input_value1==6:
		return make_sl3(color)
	if input_value1==7:
		return make_pie1(color)
	if input_value1==8:
		return make_pie2(color)
	if input_value1==9:
		return make_pie3(color)
	if input_value1==10:
		return make_bar1(color)
	if input_value1==11:
		return make_bar2(color)
	if input_value1==12:
		return make_hist1(color)
	if input_value1==13:
		return make_hist2(color)
	if input_value1==14:
		return make_hist3(color)
	if input_value1==15:
		return make_box1(color)
	if input_value1==16:
		return make_box2(color)
	if input_value1==17:
		return make_t1(color)
	if input_value1==18:
		return make_t2(color)
	if input_value1==19:
		return make_ps1(color)
	if input_value1==20:
		return make_ph1(color)
	if input_value1==21:
		return make_ph2(color)
	if input_value1==22:
		return make_pb1(color)
	if input_value1==23:
		return make_pc1(color)
	

	return make_sp1(color)

#dropdown syntax

@app.callback(
    Output(component_id='syntax1', component_property='children'),
    [Input(component_id='submit', component_property="n_clicks")],
    [State(component_id='dropdown', component_property='value'),
    State(component_id='red_range', component_property='value'),
	State(component_id='green_range', component_property='value'),
	State(component_id='blue_range', component_property='value')])
	

def update_graph(clicks, input_value2, red, green, blue):

	color="rgba("+str(red)+","+str(green)+","+str(blue)+",0.5)"
	
	if input_value2==1:
		return code_sp1(color)
	if input_value2==2:
		return code_sp2(color)
	if input_value2==3:
		return code_sp3(color)
	if input_value2==4:
		return code_sl1(color)
	if input_value2==5:
		return code_sl2(color)
	if input_value2==6:
		return code_sl3(color)
	if input_value2==7:
		return code_pie1(color)
	if input_value2==8:
		return code_pie2(color)
	if input_value2==9:
		return code_pie3(color)
	if input_value2==10:
		return code_bar1(color)
	if input_value2==11:
		return code_bar2(color)
	if input_value2==12:
		return code_hist1(color)
	if input_value2==13:
		return code_hist2(color)
	if input_value2==14:
		return code_hist3(color)
	if input_value2==15:
		return code_box1(color)
	if input_value2==16:
		return code_box2(color)
	if input_value2==17:
		return code_t1(color)
	if input_value2==18:
		return code_t2(color)
	if input_value2==19:
		return code_ps1(color)
	if input_value2==20:
		return code_ph1(color)
	if input_value2==21:
		return code_ph2(color)
	if input_value2==22:
		return code_pb1(color)
	if input_value2==23:
		return code_pc1(color)

	return code_sp1(color)


if __name__ == '__main__':
    app.run_server()