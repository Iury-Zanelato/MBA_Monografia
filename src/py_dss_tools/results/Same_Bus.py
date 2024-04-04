# -*- coding: utf-8 -*-
# @Author  : Iury Zanelato
# @Email   : iury.ribeirozanelato@gmail.com
# @File    : Same_Bus.py
# @Software: PyCharm

from py_dss_interface import DSS
import pandas as pd
from dataclasses import dataclass, field
from typing import Tuple

class Same_Bus:

    def __init__(self, dss: DSS):
        self._dss = dss
        self.same_bus = pd.DataFrame()

    def check_same_buses(self):
        elements = self._dss.circuit.elements_names

        for elem in elements:
            self._dss.circuit.set_active_element(elem)
            elem_name = self._dss.cktelement.name
            buses = self._dss.cktelement.bus_names
            if len(buses) > 1:
                bus1 = self._dss.cktelement.bus_names[0].split(".")[0]
                bus2 = self._dss.cktelement.bus_names[1].split(".")[0]

                if elem_name.split(".")[0] not in ["Vsource", "Capacitor", "Reactor"]:
                    if self._dss.cktelement.bus_names[0] == self._dss.cktelement.bus_names[1]:
                        print(f"\nElement: {elem_name} with the same bus1 {bus1} and bus2 {bus2}")

        self._dss.text("solve")
        elements