from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import quandl
import plotly.figure_factory as ff
import matplotlib as mpl
import plotly.plotly as py
import quandl

qdata = quandl.get("WIKI/AAPL", authtoken = "9vAJtSzhfwk-z4ikxWiB")
qdata_2017 = qdata["2017"]

#scatter1
def make_sp1(color):
    
    random_x1 = np.random.randn(1000)
    random_y1 = np.random.randn(1000)

    trace1 = go.Scatter(
        x = random_x1,
        y = random_y1,
        mode = 'markers',
        name = 'markers',
        marker = dict(
            size = 10,
            color=color
        )
    )

    data1 = [trace1]
    f1 = dict(data=data1)
    return f1


#scatter2
def make_sp2(color):
    random_x2 = np.random.randn(1000)
    random_y2 = np.random.randn(1000)

    trace2 = go.Scatter(
        x = random_x2,
        y = random_y2,
        mode = 'markers',
        name = 'markers',
        marker = dict(
            size = 10,
            color=color))

    layout2  = dict(title = "Scatter",
                   xaxis = dict(
                 title = "X title",
                 showgrid=False,
                 showline=False,
                 zeroline=False
             ),
                   yaxis = dict(
                 title = "Y title",
                 showgrid=False,
                 showline=False,
                 zeroline=False
             )
                  )


    data2 = [trace2]
    f2 = dict(data=data2,layout=layout2)
    return f2

#scatter3
def make_sp3(color):
    random_x3 = np.random.randn(1000)
    random_y3 = np.random.randn(1000)

    trace3_1 = go.Scatter(
        x = random_x3,
        y = random_y3,
        mode = 'markers',
        name = 'markers_1',
        marker = dict(
            size = 10,
            color=color
        )
    )

    trace3_2 = go.Scatter(
        x = random_x3-5,
        y = random_y3,
        mode = 'markers',
        name = 'markers_2',
        marker = dict(
            color="rgba(255,165,0,0.5)"
        )
    )

    layout3  = dict(title = "Multiple Scatter",
                   xaxis = dict(
                 title = "X title",
                 showgrid=False,
                 showline=False,
                 zeroline=False
             ),
                   yaxis = dict(
                 title = "Y title",
                 showgrid=False,
                 showline=False,
                 zeroline=False
             )
                  )


    data3 = [trace3_1, trace3_2]
    f3 = dict(data=data3,layout=layout3)
    return f3

#line1
def make_sl1(color):
    random_x4 = np.linspace(0,1,1000)
    random_y4 = np.random.randn(1000)

    trace4 = go.Scatter(
        x = random_x4,
        y = random_y4,
        mode = 'lines',
        name = 'lines',
        marker = dict(
            size = 10,
            color=color
        )
    )

    data4 = [trace4]
    f4 = dict(data=data4)
    return f4

#line2
def make_sl2(color):
    random_x5_scatter = np.random.randn(1000)
    random_x5_line = np.linspace(0,1,1000)
    random_y5 = np.random.randn(1000)

    trace5_1 = go.Scatter(
        x = random_x5_line,
        y = random_y5,
        mode = 'markers+lines',
        name = 'markers and lines',
        marker = dict(
            size = 10,
            color=color
        )
    )

    trace5_2 = go.Scatter(
        x = random_x5_scatter,
        y = random_y5-5,
        mode = 'markers',
        name = 'markers only',
        marker = dict(
            color="rgba(255,165,0,0.5)"
        )
    )

    layout5 = dict(title = "Line and Scatter",
                   xaxis = dict(
                 title = "X title",
                 showgrid=False,
                 showline=False,
                 zeroline=False
             ),
                   yaxis = dict(
                 title = "Y title",
                 showgrid=False,
                 showline=False,
                 zeroline=False
             )
                  )


    data5 = [trace5_1, trace5_2]
    f5 = dict(data=data5,layout=layout5)
    return f5

#line3
def make_sl3(color):
    random_x6_scatter = np.random.randn(1000)
    random_x6_line = np.linspace(0,1,1000)
    random_y6 = np.random.randn(1000)

    trace6_1 = go.Scatter(
        x = random_x6_line,
        y = random_y6,
        mode = 'lines',
        name = 'dashed line',
        line = dict(
            width = 4,
            color=color,
            dash="dash"
        )
    )

    trace6_2 = go.Scatter(
        x = random_x6_scatter,
        y = random_y6-5,
        mode = 'lines',
        name = 'dotted line',
        line = dict(
            width = 8,
            color="rgba(255,165,0,0.5)",
            dash="dot"
        )
    )

    layout6 = dict(title = "Line and Scatter",
                   xaxis = dict(
                 title = "X title",
                 showgrid=False,
                 showline=False,
                 zeroline=False
             ),
                   yaxis = dict(
                 title = "Y title",
                 showgrid=False,
                 showline=False,
                 zeroline=False
             )
                  )


    data6 = [trace6_1, trace6_2]
    f6 = dict(data=data6, layout=layout6)
    return f6

#pie1
def make_pie1(color):
    labels1 = ['HTML/CSS','Python','SQL','Other']
    values1 = [15,50,15,20]

    trace7 = go.Pie(labels=labels1, values=values1)

    data7 = [trace7]
    f7 = dict(data=data7)
    return f7

#pie2
def make_pie2(color):
    labels2 = ['HTML/CSS','Python','SQL','Other']
    values2 = [15,50,15,20]
    colors2 = ['#FEBFB3', color, '#96D38C', '#D0F9B1']

    trace8 = go.Pie(labels=labels2, values=values2,
                   hoverinfo='label+percent', textinfo='percent', 
                   textfont=dict(size=20),
                   marker=dict(colors=colors2)
                  )

    data8 = [trace8]
    f8 = dict(data=data8)
    return f8

#pie3
def make_pie3(color):
    labels3 = ['HTML/CSS','Python','SQL','Other']
    values3 = [15,50,15,20]
    colors3 = ['#FEBFB3', color, '#96D38C', '#D0F9B1']

    trace9 = go.Pie(labels=labels3, values=values3,
                   hoverinfo='label+percent', textinfo='value', 
                   textfont=dict(size=20),
                   marker=dict(colors=colors3),
                   hole = 0.4,
                  )

    data9 = [trace9]
    f9 = dict(data=data9)
    return f9

#bar1
def make_bar1(color):
    x_values10 = ['HTML/CSS','Python','SQL','Other']
    y_values10 = [15,50,15,20]

    trace10 = go.Bar(x=x_values10, y=y_values10, marker=dict(color=color))

    data10 = [trace10]
    f10 = dict(data=data10)
    return f10

#bar2
def make_bar2(color):
    x_values11 = ['HTML/CSS','Python','SQL','Other']
    y_values11_1 = [15,50,15,20]
    y_values11_2 = [15,50,5,35]

    trace11_1 = go.Bar(x=x_values11, y=y_values11_1, name="Coverage", marker=dict(color=color))
    trace11_2 = go.Bar(x=x_values11, y=y_values11_2, name="Difficulty")

    layout11 = dict(barmode = 'group')
    #layout11 = dict(barmode = 'stack')

    data11 = [trace11_1,trace11_2]
    f11 = dict(data=data11,layout=layout11)
    return f11

#hist1
def make_hist1(color):
    x_values12 = np.random.randn(500)
    trace12 = go.Histogram(x=x_values12, marker=dict(color=color))

    data12 = [trace12]
    f12 = dict(data=data12)
    return f12

#hist2
def make_hist2(color):
    y_values13 = np.random.randn(500)
    trace13 = go.Histogram(y=y_values13, marker=dict(color=color))

    data13 = [trace13]
    f13 = dict(data=data13)
    return f13

#hist3
def make_hist3(color):
    x_values14 = np.random.randn(500)

    trace14_1 = go.Histogram(x=x_values14, marker=dict(color=color))
    trace14_2 = go.Histogram(x=x_values14+2)

    layout14 = dict(barmode='overlay')

    data14 = [trace14_1,trace14_2]
    f14 = dict(data=data14, layout=layout14)
    return f14

#box1
def make_box1(color):
    y_values15 = np.random.randn(500)

    trace15_1 = go.Box(y=y_values15, marker=dict(color=color))
    trace15_2 = go.Box(y=y_values15+2)

    data15 = [trace15_1,trace15_2]
    f15 = dict(data=data15)
    return f15

#box2
def make_box2(color):
    x_values16 = np.random.randn(500)

    trace16_1 = go.Box(x=x_values16, marker=dict(color=color))
    trace16_2 = go.Box(x=x_values16+2)

    data16 = [trace16_1,trace16_2]
    f16 = dict(data=data16)
    return f16

#table1
def make_t1(color):
    header17 = dict(values=['Percentage', 'Letter grade'], fill = dict(color=color))
    cells17 = dict(values=[ [90-100, 80-90, 70-80, 60-70], ["A", "B", "C", "D"] ])
    trace17 = go.Table(header=header17, cells=cells17)

    data17 = [trace17]
    f17 = dict(data=data17)
    return f17

#table2
def make_t2(color):
    header18 = dict(values=['Percentage','Letter grade'],
                  align = ['left','center'],
                  font = dict(color = 'white', size = 12),
                  fill = dict(color=color)
                 )
    cells18 = dict(values=[["90-100", "80-90", "70-80", "60-70"],
                         ["A", "B", "C", "D"]],
                 align = ['left','center'],
                 fill = dict(color=["yellow","white"])
                )
    trace18 = go.Table(header=header18, cells=cells18)

    data18 = [trace18]
    layout18 = dict(width=500, height=300)
    f18 = dict(data=data18, layout=layout18)
    return f18

#pandas scatter
def make_ps1(color):
    x_values19 = pd.to_datetime(qdata_2017.index.values)
    y_values19 = qdata_2017.Volume
    trace19 = go.Scatter(x=x_values19, y=y_values19, mode="markers", marker=dict(color=color))

    data19 = [trace19]
    f19 = dict(data=data19)
    return f19

#pandas hist1
def make_ph1(color):
    trace20 = go.Histogram(x=qdata.Open, marker=dict(color=color))

    data20 = [trace20]
    f20 = dict(data=data20)
    return f20

#pandas hist2
def make_ph2(color):
    trace21 = go.Histogram(x=qdata.Open.pct_change(), marker=dict(color=color))

    data21 = [trace21]
    f21 = dict(data=data21)
    return f21

#pandas box
def make_pb1(color):
    trace22 = go.Box(x=qdata.Open.pct_change(), marker=dict(color=color))

    data22 = [trace22]
    f22 = dict(data=data22)
    return f22

#corr
def make_pc1(color):
    data_scoped = qdata[["Open","Volume"]]
    corr_matrix_list = data_scoped.corr().values.tolist()
    x_axis23 = data_scoped.corr().columns
    y_axis23 = data_scoped.corr().index.values

    trace23 = go.Heatmap(x=x_axis23, y=y_axis23, z=corr_matrix_list, colorscale='Viridis')

    data23 = [trace23]
    f23 = dict(data=data23)
    return f23