import pandas as pd
from bat.log_to_dataframe import LogToDataFrame
import plotly.offline as py
import plotly.graph_objs as go
import cufflinks as cf


def main():
    web = LogToDataFrame('http.log')
    # print(web.host.unique())

    conn = LogToDataFrame('conn.log')
    conn.index.names = ['Timestamp']
    conn.columns.names = ['Columns']
    conn = conn.rename(
        columns={'id.orig_h': 'source', 'id.orig_p': 'src port', 'id.resp_h': 'destination', 'id.resp_p': 'dst port'})
    print(conn[['source', 'src port', 'destination', 'dst port', 'proto', 'service']])

    service = conn.service.value_counts()
    plot = service.iplot(asFigure=True, kind='bar',yTitle='Number of Occurrences',title='Protocols')
    py.plot(plot, auto_open=True)



if __name__ == '__main__':
    main()