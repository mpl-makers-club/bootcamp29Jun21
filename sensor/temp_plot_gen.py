# temp_plot_gen.py
import plotly
import plotly.graph_objects as go
import pandas
df = pandas.read_csv('/home/pi/botanica-park-lake/data.txt')

fig = go.Figure(data = go.Scatter(mode='markers',
                                  x=df.Date,
                                  y=df.Temp,
                                  marker=dict(
                                      color="LightSkyBlue",
                                      size=20)
                                  )
                )
fig.update_layout(title='Temperature data',
                  xaxis_title = 'Time',
                  yaxis_title = 'Temperature',
                  font=dict(
                      size=26,
                      color="RebeccaPurple"
                      )
                  )
plotly.offline.plot(fig,
                    filename="/home/pi/botanica-park-lake/atm_temp.html",
                    auto_open=False)
print("Atmospheric temperature plotted")


