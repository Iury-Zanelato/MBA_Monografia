# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : phases_connections.py
# @Software: PyCharm



import py_dss_interface
import os
import pathlib
import numpy as np


def add_default_nodes(elem_nodes):
    if not elem_nodes:
        return ['1', '2', '3']
    else:
        return elem_nodes


def check_phase_connection(parent_elem_nodes, elem_nodes):
    issue_flag = False
    for node in elem_nodes:
        if node not in parent_elem_nodes:
            issue_flag = True

    return issue_flag


def check_phases_connections(dss: py_dss_interface.DSS):
    dss.text("solve")
    dss.meters.first()
    end_elements = dss.meters.all_end_elements
    elements_checked = list()
    for end_elem in end_elements:

        dss.circuit.set_active_element(end_elem)
        elem_name = dss.cktelement.name
        elements_checked.append(elem_name)

        elem_bus1 = dss.cktelement.bus_names[0].split(".")[0]
        elem_bus2 = dss.cktelement.bus_names[1].split(".")[0]
        elem_nodes1 = dss.cktelement.bus_names[0].split(".")[1:]
        elem_nodes2 = dss.cktelement.bus_names[1].split(".")[1:]

        while dss.circuit.parent_pd_element:

            parent_elem_name = dss.cktelement.name

            if parent_elem_name not in elements_checked:

                parent_elem_bus1 = dss.cktelement.bus_names[0].split(".")[0]
                parent_elem_bus2 = dss.cktelement.bus_names[1].split(".")[0]
                parent_elem_nodes1 = dss.cktelement.bus_names[0].split(".")[1:]
                parent_elem_nodes2 = dss.cktelement.bus_names[1].split(".")[1:]

                elem_nodes1 = add_default_nodes(elem_nodes1)
                elem_nodes2 = add_default_nodes(elem_nodes2)
                parent_elem_nodes1 = add_default_nodes(parent_elem_nodes1)
                parent_elem_nodes2 = add_default_nodes(parent_elem_nodes2)

                if elem_bus1 == parent_elem_bus2:
                    if check_phase_connection(parent_elem_nodes2, elem_nodes1):
                        print(
                            f"\nPhase issue between (Case 1):\nParent: {parent_elem_name} with bus {parent_elem_bus2} and nodes {parent_elem_nodes2}"
                            f"\nElement: {elem_name} with bus {elem_bus1} and nodes {elem_nodes1}")

                elif elem_bus1 == parent_elem_bus1:
                    if check_phase_connection(parent_elem_nodes1, elem_nodes1):
                        print(
                            f"\nPhase issue between (Case 2):\nParent: {parent_elem_name} with bus {parent_elem_bus1} and nodes {parent_elem_nodes1}"
                            f"\nElement: {elem_name} with bus {elem_bus1} and nodes {elem_nodes1}")

                elif elem_bus2 == parent_elem_bus2:
                    if check_phase_connection(parent_elem_nodes2, elem_nodes2):
                        print(
                            f"\nPhase issue between (Case 3):\nParent: {parent_elem_name} with bus {parent_elem_bus2} and nodes {parent_elem_nodes2}"
                            f"\nElement: {elem_name} with bus {elem_bus2} and nodes {elem_nodes2}")

                elif elem_bus2 == parent_elem_bus1:
                    if check_phase_connection(parent_elem_nodes1, elem_nodes2):
                        print(
                            f"\nPhase issue between (Case 4):\nParent: {parent_elem_name} with bus {parent_elem_bus1} and nodes {parent_elem_nodes1}"
                            f"\nElement: {elem_name} with bus {elem_bus2} and nodes {elem_nodes2}")

                elem_name = parent_elem_name
                elem_bus1 = parent_elem_bus1
                elem_bus2 = parent_elem_bus2
                elem_nodes1 = parent_elem_nodes1
                elem_nodes2 = parent_elem_nodes2

                elements_checked.append(elem_name)

                if elem_name.lower() == "vsourve.source":
                    print("All elements checked")


if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))

    dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

    dss = py_dss_interface.DSS()

    dss.text(f"compile [{dss_file}]")
    dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
    dss.text("Buscoords Buscoords.dat ")

    dss.text("solve")
    check_phases_connections(dss)
