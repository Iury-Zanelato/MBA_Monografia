# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : missing_nodes.py
# @Software: PyCharm



import py_dss_interface
import os
import pathlib
import numpy as np

def check_missing_phases(dss):
    dss.text("solve")
    dss.meters_first()
    elements = dss.circuit_all_element_names()
    elements_checked = list()
    for elem in elements:

        if elem.split(".")[0].lower() in ["line", "transformer"]:
            dss.circuit_set_active_element(elem)
            elem_name = dss.cktelement_name()
            elements_checked.append(elem_name)

            elem_bus1 = dss.cktelement_read_bus_names()[0].split(".")[0]
            elem_bus2 = dss.cktelement_read_bus_names()[1].split(".")[0]
            elem_nodes1 = dss.cktelement_read_bus_names()[0].split(".")[1:]
            elem_nodes2 = dss.cktelement_read_bus_names()[1].split(".")[1:]

            if not elem_nodes1:
                print(f"{elem_name} with Bus1 without nodes {elem_bus1}")

            if not elem_nodes2:
                print(f"{elem_name} with Bus2 without nodes {elem_bus2}")


if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))

    dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

    dss = py_dss_interface.DSSDLL()

    dss.text(f"compile [{dss_file}]")
    dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
    dss.text("Buscoords Buscoords.dat ")

    dss.text("solve")
    check_missing_phases(dss)

    dss_file = r"C:\Users\ppra005\Box\Documents_PC\PR\OpenDSS_Perdas\2-RoraimaFiles\Alimentadores CE-01_07_09\ArquivosOpenDSS_FT_AL2-10-FT_AL2-10_2023.02.28\Master_370_FT_AL2-10_Mes01_DO.dss"
    dss = py_dss_interface.DSSDLL()

    dss.text(f"compile [{dss_file}]")
    dss.text("solve")
    check_missing_phases(dss)