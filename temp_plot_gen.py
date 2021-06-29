import plotly.graph_objects as go
import pandas

df = pandas.read_csv('/home/pi/botanica-park-lake/data.txt')
print(df)

mx = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my = [2, 4, 6, 8, 2, 34, 33, 23, 12]

fig = go.Figure(data = go.Scatter(x=mx, y=my))

fig.update_layout(title='Test data',
                  xaxis_title = 'Time',
                  yaxis_title = 'Temperature')


fig.show()
print("Graph completed")
