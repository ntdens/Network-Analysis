import pandas as pd
from bat.log_to_dataframe import LogToDataFrame
import plotly.offline as py
import plotly.graph_objs as go

web = LogToDataFrame('http.log')
print(web.host.unique())
