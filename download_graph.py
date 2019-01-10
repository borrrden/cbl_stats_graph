import plotly
import plotly.graph_objs as go
import argparse

parser = argparse.ArgumentParser(description='Creates a bar graph given a set of download count inputs (must be ordered correctly)')
parser.add_argument('--version', type=str, help='The version to show as the title')

args = parser.parse_args()
version = args.version

with open('downloads.txt') as f:
    content = f.readlines()

content = [int(x.strip()) for x in content]

data = [go.Bar(
            x=['CE Base','EE Base','CE Android','CE iOS','CE Desktop','CE UWP','EE Desktop','EE UWP','EE Android','EE iOS'],
            y=content
    )]

layout = go.Layout(title = "Couchbase Lite {}".format(version))

plotly.offline.plot({"data":data, "layout":layout}, filename='downloads.html', show_link=False, auto_open=False)
