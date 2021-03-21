import chart_studio.plotly as py
from plotly.graph_objs import *  # pylint: disable=unused-wildcard-import
import igraph as ig


def create_plotly_plot(layt, N, E, labels, colors, sizes):
    Xn=[layt[k][0] for k in range(N)]
    Yn=[layt[k][1] for k in range(N)]
    Xe=[]
    Ye=[]
    for e in E:
        Xe+=[layt[e[0]][0],layt[e[1]][0], None]
        Ye+=[layt[e[0]][1],layt[e[1]][1], None]

    trace1=Scatter(x=Xe,
                y=Ye,
                mode='lines',
                line= dict(color='rgb(210,210,210)', width=1),
                hoverinfo='none'
                )
    trace2=Scatter(x=Xn,
                y=Yn,
                mode='markers',
                name='ntw',
                marker=dict(symbol='circle-dot',
                                            color=colors,
                                            size=sizes,
                                            line=dict(color='rgb(50,50,50)', width=0.5)
                                            ),
                text=labels,
                hoverinfo='text'
                )

    axis=dict(showline=False,  # hide axis line, grid, ticklabels and  title
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title=''
            )

    width=1400
    height=800
    _layout=Layout(title= f"layout of {labels[0]}",
        font= dict(size=12),
        showlegend=False,
        autosize=False,
        width=width,
        height=height,
        xaxis=layout.XAxis(axis),
        yaxis=layout.YAxis(axis),
        margin=layout.Margin(
            l=40,
            r=40,
            b=85,
            t=100,
        ),
        hovermode='closest'#,
        # annotations=[
        #     dict(
        #         x=30,  # arrows' head
        #         y=30,  # arrows' head
        #         ax=40,  # arrows' tail
        #         ay=40,  # arrows' tail
        #         xref='x',
        #         yref='y',
        #         axref='x',
        #         ayref='y',
        #         text='',  # if you want only the arrow
        #         showarrow=True,
        #         arrowhead=3,
        #         arrowsize=1,
        #         arrowwidth=1,
        #         arrowcolor='black'
        #         )
        #     ]
        )

    data=[trace1, trace2]
    fig=Figure(data=data, layout=_layout)
    fig.write_html('plot.html')
