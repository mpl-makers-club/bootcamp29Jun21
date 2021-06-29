import plotly.graph_objects as go

mx = [1, 2, 3, 4]
my = [2, 4, 6, 8]

fig = go.Figure(data = go.Scatter(x=mx, y=my))

fig.update_layout(title='Test data',
                  xaxis_title = 'Time',
                  yaxis_title = 'Temperature')

fig.show()


