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

#code
def code_sp1(color):
  s1='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import numpy as np
  random_x1 = np.random.randn(1000)
  random_y1 = np.random.randn(1000)

  trace1 = go.Scatter(x = random_x1, y = random_y1, mode = 'markers', name = 'markers',
                      marker = dict(size = 10, color='''+color+'''))

  data1 = [trace1]
  f1 = dict(data=data1)'''
  return s1

def code_sp2(color):
  s2='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import numpy as np
  random_x2 = np.random.randn(1000)
  random_y2 = np.random.randn(1000)

  trace2 = go.Scatter(x = random_x2, y = random_y2, mode = 'markers', name = 'markers',
                      marker = dict(size = 10, color='''+color+'''))

  layout2  = dict(title = "Scatter", xaxis = dict(title = "X title", showgrid=False, showline=False, zeroline=False),
                  yaxis = dict(title = "Y title", showgrid=False, showline=False, zeroline=False))

  data2 = [trace2]
  f2 = dict(data=data2,layout=layout2)'''
  return s2

def code_sp3(color):
  s3='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import numpy as np
  random_x3 = np.random.randn(1000)
  random_y3 = np.random.randn(1000)

  trace3_1 = go.Scatter(x = random_x3, y = random_y3, mode = 'markers', name = 'markers_1', marker = dict( size = 10,
  					color='''+color+'''))

  trace3_2 = go.Scatter(x = random_x3-5, y = random_y3, mode = 'markers', name = 'markers_2', marker = dict(
  					color="rgba(152,0,0,0.5)"))

  layout3  = dict(title = "Multiple Scatter", xaxis = dict(title = "X title", showgrid=False, showline=False,
  				zeroline=False), yaxis = dict(title = "Y title", showgrid=False, showline=False, zeroline=False))

  data3 = [trace3_1, trace3_2]
  f3 = dict(data=data3,layout=layout3)'''
  return s3


def code_sl1(color):
  l1='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  random_x4 = np.linspace(0,1,1000)
  random_y4 = np.random.randn(1000)

  trace4 = go.Scatter(x = random_x4, y = random_y4, mode = 'lines', name = 'lines', marker = dict(size = 10,
          			color='''+color+'''))

  data4 = [trace4]
  f4 = dict(data=data4)'''
  return l1

def code_sl2(color):
  l2='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import numpy as np
  random_x5_scatter = np.random.randn(1000)
  random_x5_line = np.linspace(0,1,1000)
  random_y5 = np.random.randn(1000)

  trace5_1 = go.Scatter(x = random_x5_line, y = random_y5, mode = 'markers+lines', name = 'markers and lines',
      				marker = dict(size = 10, color='''+color+'''))

  trace5_2 = go.Scatter(x = random_x5_scatter, y = random_y5-5, mode = 'markers', name = 'markers only',
      				marker = dict(color="rgba(255,165,0,0.5)"))

  layout5 = dict(title = "Line and Scatter", xaxis = dict(title = "X title", showgrid=False, showline=False,
               zeroline=False), yaxis = dict(title = "Y title", showgrid=False, showline=False, zeroline=False))

  data5 = [trace5_1, trace5_2]
  f5 = dict(data=data5,layout=layout5)'''
  return l2

def code_sl3(color):
  l3='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import numpy as np
  random_x6_scatter = np.random.randn(1000)
  random_x6_line = np.linspace(0,1,1000)
  random_y6 = np.random.randn(1000)

  trace6_1 = go.Scatter(x = random_x6_line, y = random_y6, mode = 'lines', name = 'dashed line',
      line = dict(width = 4, color='''+color+''', dash="dash"))

  trace6_2 = go.Scatter(x = random_x6_scatter, y = random_y6-5, mode = 'lines', name = 'dotted line',
      line = dict(width = 8, color="rgba(255,165,0,0.5)", dash="dot"))

  layout6 = dict(title = "Line and Scatter", xaxis = dict(title = "X title", showgrid=False, showline=False,
               zeroline=False), yaxis = dict(title = "Y title", showgrid=False, showline=False,
               zeroline=False))

  data6 = [trace6_1, trace6_2]
  f6 = dict(data=data6, layout=layout6)'''
  return l3

def code_pie1(color):
  p1='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  labels1 = ['HTML/CSS','Python','SQL','Other']
  values1 = [15,50,15,20]

  trace7 = go.Pie(labels=labels1, values=values1)

  data7 = [trace7]
  f7 = dict(data=data7)'''
  return p1

def code_pie2(color):
  p2='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  labels2 = ['HTML/CSS','Python','SQL','Other']
  values2 = [15,50,15,20]
  colors2 = ['#FEBFB3', '''+color+''', '#96D38C', '#D0F9B1']

  trace8 = go.Pie(labels=labels2, values=values2, hoverinfo='label+percent', textinfo='percent', 
                 textfont=dict(size=20), marker=dict(colors=colors2))

  data8 = [trace8]
  f8 = dict(data=data8)'''
  return p2

def code_pie3(color):
  p3='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  labels3 = ['HTML/CSS','Python','SQL','Other']
  values3 = [15,50,15,20]
  colors3 = ['#FEBFB3', '''+color+''', '#96D38C', '#D0F9B1']

  trace9 = go.Pie(labels=labels3, values=values3, hoverinfo='label+percent', textinfo='value', 
                 textfont=dict(size=20), marker=dict(colors=colors3), hole = 0.4,)

  data9 = [trace9]
  f9 = dict(data=data9)'''
  return p3

def code_bar1(color):
  b1='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  x_values10 = ['HTML/CSS','Python','SQL','Other']
  y_values10 = [15,50,15,20]

  trace10 = go.Bar(x=x_values10, y=y_values10)

  data10 = [trace10]
  f10 = dict(data=data10)'''
  return b1

def code_bar2(color):
  b2='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  x_values11 = ['HTML/CSS','Python','SQL','Other']
  y_values11_1 = [15,50,15,20]
  y_values11_2 = [15,50,5,35]

  trace11_1 = go.Bar(x=x_values11, y=y_values11_1, name="Coverage")
  trace11_2 = go.Bar(x=x_values11, y=y_values11_2, name="Difficulty")

  layout11 = dict(barmode = 'group')
  #layout11 = dict(barmode = 'stack')

  data11 = [trace11_1,trace11_2]
  f11 = dict(data=data11,layout=layout11)'''
  return b2

def code_hist1(color):
  h1='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  x_values12 = np.random.randn(500)
  trace12 = go.Histogram(x=x_values12)

  data12 = [trace12]
  f12 = dict(data=data12)'''
  return h1

def code_hist2(color):
  h2='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import numpy as np
  y_values13 = np.random.randn(500)
  trace13 = go.Histogram(y=y_values13)

  data13 = [trace13]
  f13 = dict(data=data13)'''
  return h2

def code_hist3(color):
  h3='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import numpy as np
  x_values14 = np.random.randn(500)

  trace14_1 = go.Histogram(x=x_values14)
  trace14_2 = go.Histogram(x=x_values14+2)

  layout14 = dict(barmode='overlay')

  data14 = [trace14_1,trace14_2]
  f14 = dict(data=data14, layout=layout14)'''
  return h3

def code_box1(color):
  bp1='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import numpy as np
  y_values15 = np.random.randn(500)

  trace15_1 = go.Box(y=y_values15)
  trace15_2 = go.Box(y=y_values15+2)

  data15 = [trace15_1,trace15_2]
  f15 = dict(data=data15)'''
  return bp1

def code_box2(color):
  bp2='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import numpy as np
  x_values16 = np.random.randn(500)

  trace16_1 = go.Box(x=x_values16)
  trace16_2 = go.Box(x=x_values16+2)

  data16 = [trace16_1,trace16_2]
  f16 = dict(data=data16)'''
  return bp2

def code_t1(color):
  t1='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  header17 = dict(values=['Percentage', 'Letter grade'])
  cells17 = dict(values=[ [90-100, 80-90, 70-80, 60-70], ["A", "B", "C", "D"] ])
  trace17 = go.Table(header=header17, cells=cells17)

  data17 = [trace17]
  f17 = dict(data=data17)'''
  return t1

def code_t2(color):
  t2='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  header18 = dict(values=['Percentage','Letter grade'],
                align = ['left','center'],
                font = dict(color = 'white', size = 12),
                fill = dict(color='#119DFF'))
  cells18 = dict(values=[["90-100", "80-90", "70-80", "60-70"],
                       ["A", "B", "C", "D"]],
               align = ['left','center'],
               fill = dict(color=["yellow","white"]))
  trace18 = go.Table(header=header18, cells=cells18)

  data18 = [trace18]
  layout18 = dict(width=500, height=300)
  f18 = dict(data=data18, layout=layout18)'''
  return t2

def code_ps1(color):
  ps1='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import pandas as pd
  x_values19 = pd.to_datetime(qdata_2017.index.values)
  y_values19 = qdata_2017.Volume
  trace19 = go.Scatter(x=x_values19,y=y_values19,mode="markers")

  data19 = [trace19]
  f19 = dict(data=data19)'''
  return ps1

def code_ph1(color):
  ph1='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import pandas as pd
  trace20 = go.Histogram(x=qdata.Open)

  data20 = [trace20]
  f20 = dict(data=data20)'''
  return ph1

def code_ph2(color):
  ph2='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import pandas as pd
  trace21 = go.Histogram(x=qdata.Open.pct_change())

  data21 = [trace21]
  f21 = dict(data=data21)'''
  return ph2

def code_pb1(color):
  pb1='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import pandas as pd
  trace22 = go.Box(x=qdata.Open.pct_change())

  data22 = [trace22]
  f22 = dict(data=data22)'''
  return pb1

def code_pc1(color):
  pc1='''
  from plotly.offline import plot, iplot
  import plotly.graph_objs as go
  from plotly.offline import init_notebook_mode
  init_notebook_mode(connected=True)

  import pandas as pd
  data_scoped = qdata[["Open","Volume"]]
  corr_matrix_list = data_scoped.corr().values.tolist()
  x_axis23 = data_scoped.corr().columns
  y_axis23 = data_scoped.corr().index.values

  trace23 = go.Heatmap(x=x_axis23 ,y=y_axis23, z=corr_matrix_list, colorscale='Viridis')

  data23 = [trace23]
  f23 = dict(data=data23)'''
  return pc1