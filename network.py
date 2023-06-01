# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : network.py
# @Software: PyCharm

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import py_dss_interface
import os
import pathlib
import numpy as np
import plotly.graph_objects as go


def check_isolated(dss: py_dss_interface.DSSDLL):
    dss.text("solve")
    dss.text("interpolate")

    G = nx.Graph()
    nodes_seen = list()
    elements = dss.circuit_all_element_names()
    for element in elements:
        if element.split(".")[0].lower() in ["transformer", "line"]:
            dss.circuit_set_active_element(element)
            elem_name = dss.cktelement_name()
            elem_bus1 = dss.cktelement_read_bus_names()[0].split(".")[0]
            elem_bus2 = dss.cktelement_read_bus_names()[1].split(".")[0]

            G.add_edge(elem_bus1, elem_bus2)
            G.edges[elem_bus1, elem_bus2]["name"] = elem_name

            for bus in [elem_bus1, elem_bus2]:
                if bus not in nodes_seen:
                    nodes_seen.append(bus)
                    dss.circuit_set_active_bus(bus)
                    bus_name = dss.bus_name()
                    x = dss.bus_read_x()
                    y = dss.bus_read_y()
                    if x == 0 and y == 0:
                        print(f"Node {bus_name} with zero coords")
                    G.nodes[bus_name]["pos"] = (x, y)

    print(f"Number of Nodes: {G.number_of_nodes()}")
    print(f"Number of Edges: {G.number_of_edges()}")

    plot_graph(G, 0)

    subsG = nx.connected_components(G)
    for i, sub_nodes in enumerate(subsG):
        subG = G.subgraph(sub_nodes)
        plot_graph(subG, i + 1)
        print(subG)

    plt.show()

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        # line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines',
        line=dict(colorbar=dict(
                      thickness=15,
                      title='Node Connections',
                      xanchor='left',
                      titleside='right'
                  ),
                  colorscale='YlGnBu')
    )

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            # colorscale options
            # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    node_text = []
    for node in G.nodes():
        node_text.append('Bus Name: ' + str(node))

    node_trace.text = node_text

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<br>Network graph made with Python',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        # annotations=[dict(
                        #     text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                        #     showarrow=False,
                        #     xref="paper", yref="paper",
                        #     x=0.005, y=-0.002)],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    fig.show()


def plot_graph(G, i):
    fig = plt.figure(num=i)
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, arrows=False, with_labels=True, font_size=8, node_color='blue', node_size=5)


if __name__ == '__main__':

    script_path = os.path.dirname(os.path.abspath(__file__))

    dss = py_dss_interface.DSSDLL()
    dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

    # dss_file = r"C:\Users\ppra005\Box\Documents_PC\PR\OpenDSS_Perdas\2-RoraimaFiles\Alimentadores CE-01_07_09\ArquivosOpenDSS_CE_AL2-01-CE_AL2-01_2023.02.16\Master_370_CE_AL2-01_Mes01_DO.dss"

    dss.text(f"compile [{dss_file}]")
    dss.text("Buscoords Buscoords.dat ")
    # dss.text("Buscoords pac.csv ")
    # dss.text("Edit LINE.1002565549 bus1=889927.2")
    dss.text("Edit LINE.L117 bus1=67")
    dss.text("calcvoltagebases")


    check_isolated(dss)
