# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : isolated.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import numpy as np


def check_isolated(dss: py_dss_interface.DSS):
    dss.text("solve")

    branches_isolated = dss.topology.all_isolated_branches
    loads_isolated = dss.topology.all_isolated_loads

    for branch in branches_isolated:
        dss.circuit.set_active_element(branch)
        name = dss.cktelement.name
        if len(dss.cktelement.bus_names) == 2:
            bus1 = dss.cktelement.bus_names[0].split(".")[0]
            bus2 = dss.cktelement.bus_names[1].split(".")[0]

            print(f"{name} bus1: {bus1} bus2: {bus2}")
        else:
            bus1 = dss.cktelement.bus_names[0].split(".")[0]
            print(f"{name} bus1: {bus1}")

    for load in loads_isolated:
        dss.circuit.set_active_element(load)
        name = dss.cktelement.name
        bus1 = dss.cktelement.bus_names[0].split(".")[0]

        print(f"{name} bus1: {bus1}")


if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))

    dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

    dss = py_dss_interface.DSS()

    dss.text(f"compile [{dss_file}]")
    dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
    dss.text("Buscoords Buscoords.dat ")

    dss.text("edit Line.L67 bus2=open")

    dss.text("MakebusList")
    dss.text("plot circuit")
    check_isolated(dss)
