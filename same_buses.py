# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : same_buses.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import numpy as np


def check_same_buses(dss: py_dss_interface.DSS):
    dss.text("solve")

    elements = dss.circuit.elements_names
    for elem in elements:
        dss.circuit.set_active_element(elem)
        elem_name = dss.cktelement.name
        buses = dss.cktelement.bus_names

        if len(buses) > 1:
            bus1 = buses[0].split(".")[0]
            bus2 = buses[1].split(".")[0]

            if elem_name.split(".")[0] not in ["Vsource", "Capacitor", "Reactor"]:
                if bus1 == bus2:
                    print(f"\nElement: {elem_name} with the same bus1 {bus1} and bus2 {bus2}")


if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))

    dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

    dss = py_dss_interface.DSS()

    dss.text(f"compile [{dss_file}]")
    dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
    dss.text("Buscoords Buscoords.dat ")

    dss.text("edit Line.L67 bus2=67")

    check_same_buses(dss)