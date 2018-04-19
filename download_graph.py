import plotly
import plotly.graph_objs as go

with open('downloads.txt') as f:
    content = f.readlines()

content = [int(x.strip()) for x in content]

data = [go.Bar(
            x=['CE Base','EE Base','CE Android','CE iOS','CE Desktop','CE UWP','EE Desktop','EE UWP'],
            y=content
    )]

layout = go.Layout(title = "Couchbase Lite 2.0.0.1")

plotly.offline.plot({"data":data, "layout":layout}, filename='downloads.html', show_link=False)
