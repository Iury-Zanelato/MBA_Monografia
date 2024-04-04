# -*- coding: utf-8 -*-
# @Author  : Iury Zanelato
# @Email   : iury.ribeirozanelato@gmail.com
# @File    : Phases_Conections.py
# @Software: PyCharm

from py_dss_interface import DSS
import pandas as pd
#from dataclasses import dataclass, field
#from typing import Tuple

class Phases_Conections:

    def __init__(self, dss: DSS):
        self._dss = dss
        self.add_default_nodes = pd.DataFrame()
        self.phase_connection = pd.DataFrame()
        self.phases_connections = pd.DataFrame()

    def add_default_nodes(self, elem_nodes):
        if not elem_nodes:
            return ['1', '2', '3']
        else:
            return elem_nodes


    def check_phase_connection(self, parent_elem_nodes, elem_nodes):
        issue_flag = False
        for node in elem_nodes:
            if node not in parent_elem_nodes:
                issue_flag = True
        return issue_flag

    def check_phases_connections(self):
        self._dss.meters.first()
        end_elements = self._dss.meters.all_end_elements
        elements_checked = list()
        for end_elem in end_elements:

            self._dss.circuit.set_active_element(end_elem)
            elem_name = self._dss.cktelement.name
            elements_checked.append(elem_name)

            elem_bus1 = self._dss.cktelement.bus_names[0].split(".")[0]
            elem_bus2 = self._dss.cktelement.bus_names[1].split(".")[0]
            elem_nodes1 = self._dss.cktelement.bus_names[0].split(".")[1:]
            elem_nodes2 = self._dss.cktelement.bus_names[1].split(".")[1:]

            while self._dss.circuit.parent_pd_element:

                parent_elem_name = self._dss.cktelement.name

                if parent_elem_name not in elements_checked:

                    parent_elem_bus1 = self._dss.cktelement.bus_names[0].split(".")[0]
                    parent_elem_bus2 = self._dss.cktelement.bus_names[1].split(".")[0]
                    parent_elem_nodes1 = self._dss.cktelement.bus_names[0].split(".")[1:]
                    parent_elem_nodes2 = self._dss.cktelement.bus_names[1].split(".")[1:]

                    elem_nodes1 = self.add_default_nodes[0].split(".")[0]
                    elem_nodes2 = self.add_default_nodes[1].split(".")[0]
                    parent_elem_nodes1 = self.add_default_nodes[0].split(".")[1:]
                    parent_elem_nodes2 = self.add_default_nodes[1].split(".")[1:]


                    if elem_bus1 == parent_elem_bus2:
                        if self.check_phase_connection(parent_elem_nodes2, elem_nodes1):
                            print(
                                f"\nPhase issue between (Case 1):\nParent: {parent_elem_name} with bus {parent_elem_bus2} and nodes {parent_elem_nodes2}"
                                f"\nElement: {elem_name} with bus {elem_bus1} and nodes {elem_nodes1}")

                    elif elem_bus1 == parent_elem_bus1:
                        if self.check_phase_connection(parent_elem_nodes1, elem_nodes1):
                            print(
                                f"\nPhase issue between (Case 2):\nParent: {parent_elem_name} with bus {parent_elem_bus1} and nodes {parent_elem_nodes1}"
                                f"\nElement: {elem_name} with bus {elem_bus1} and nodes {elem_nodes1}")

                    elif elem_bus2 == parent_elem_bus2:
                        if self.check_phase_connection(parent_elem_nodes2, elem_nodes2):
                            print(
                                f"\nPhase issue between (Case 3):\nParent: {parent_elem_name} with bus {parent_elem_bus2} and nodes {parent_elem_nodes2}"
                                f"\nElement: {elem_name} with bus {elem_bus2} and nodes {elem_nodes2}")

                    elif elem_bus2 == parent_elem_bus1:
                        if self.check_phase_connection(parent_elem_nodes1, elem_nodes2):
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

        self._dss.text("solve")
        end_elements
        elements_checked
