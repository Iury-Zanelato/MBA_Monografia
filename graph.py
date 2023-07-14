# -*- coding: utf-8 -*-
# @Time    : 6/30/2023 4:20 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : graph.py
# @Software: PyCharm

import networkx as nx
import py_dss_interface
import os
import pathlib
import matplotlib.pyplot as plt


def create_graph(dss: py_dss_interface.DSS):
    dss.text("solve")
    dss.text("interpolate")

    sections = dict()
    pos = dict()

    dss.vsources.name = "source"
    bus_feeder_head = dss.cktelement.bus_names[0].split(".")[0]
    dss.circuit.set_active_bus(bus_feeder_head)
    x_feeder_head = dss.bus.x
    y_feeder_head = dss.bus.y
    pos[str(bus_feeder_head)] = (x_feeder_head, y_feeder_head)

    if x_feeder_head == 0 and y_feeder_head == 0:
        print(f"Node {bus_feeder_head} with zero coords")

    elements = dss.circuit.elements_names
    for element in elements:
        if element.split(".")[0].lower() in ["transformer", "line"]:
            dss.circuit.set_active_element(element)
            # if dss.cktelement.is_enabled:
            elem_name = dss.cktelement.name.lower()
            bus1 = dss.cktelement.bus_names[0].split(".")[0]
            bus2 = dss.cktelement.bus_names[1].split(".")[0]

            params = {
                "element type": element.split(".")[0].lower(),
                "element name": elem_name,
                "bus1": bus1.split(".")[0],
                "bus2": bus2.split(".")[0]
            }

            sections[f"{bus1}-{bus2}"] = (bus1, bus2, params)

            dss.circuit.set_active_bus(bus1)
            x1 = dss.bus.x
            y1 = dss.bus.y
            if x1 == 0 and y1 == 0:
                print(f"Node {bus1} with zero coords")

            dss.circuit.set_active_bus(bus1)
            x2 = dss.bus.x
            y2 = dss.bus.y
            if x2 == 0 and y2 == 0:
                print(f"Node {bus2} with zero coords")

            pos[str(bus2)] = (x2, y2)

    G = nx.DiGraph()
    # G = nx.Graph()
    section_edges = {}
    for section in sections:
        from_node, to_node, params = sections[section]
        edges = [from_node, to_node]
        section_edges[section] = []
        for u, v in zip(edges[:-1], edges[1:]):
            G.add_edge(u, v, **params)
            section_edges[section].append((u, v))
            G.nodes[u]["pos"] = pos[u]
            G.nodes[v]["pos"] = pos[v]

    return G

def plot_graph(G, i):
    fig = plt.figure(num=i)
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, arrows=False, with_labels=True, font_size=8, node_color='blue', node_size=5)
    plt.show()

if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))

    dss = py_dss_interface.DSS()
    dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")
    dss.text(f"compile [{dss_file}]")
    dss.text("Buscoords Buscoords.dat ")
    dss.text("New line.loop phases=3 bus1=79.1.2.3 bus2=450.1.2.3")
    # dss.text("Edit LINE.L114 enabled=no")
    dss.text("Edit LINE.L117 bus1=67")
    dss.text("calcvoltagebases")

    graph = create_graph(dss)

    dss.text("show isolated")
    dss.text("show loops")

    # Find cycles
    cycles = list(nx.simple_cycles(graph))

    # Print cycles
    print(cycles)

    # Find isolated nodes
    isolated_nodes = list(nx.isolates(graph))

    # Print isolated nodes
    print(isolated_nodes)

    # Check if the graph is a directed acyclic graph (DAG)
    is_dag = nx.is_directed_acyclic_graph(graph)

    # Print result
    if is_dag:
        print("The graph is a directed acyclic graph.")
    else:
        print("The graph contains cycles.")

    # Check if the graph is a directed acyclic graph (DAG)
    is_dag = nx.is_directed_acyclic_graph(graph)

    # Print result
    if is_dag:
        print("The graph is a directed acyclic graph.")
    else:
        print("The graph contains cycles.")

    print(f"Number of Nodes: {graph.number_of_nodes()}")
    print(f"Number of Edges: {graph.number_of_edges()}")

    plot_graph(graph, 0)

    # subsG = nx.connected_components(graph)
    # for i, sub_nodes in enumerate(subsG):
    #     subG = graph.subgraph(sub_nodes)
    #     plot_graph(subG, i + 1)
    #     print(subG)

    plt.show()