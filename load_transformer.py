# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : load_transformer.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import numpy as np


def check_load_transformer(dss: py_dss_interface.DSSDLL):
    dss.text("solve")

    dss.loads_first()

    load_transformer_dict = dict()

    for _ in range(dss.loads_count()):

        load_name = dss.loads_read_name()
        print(load_name)
        bus = dss.cktelement_read_bus_names()[0].split(".")[0]

        elements = dss.circuit_all_element_names()
        for elem in elements:

            if elem.split(".")[0].lower() in ["line", "transformer"]:
                dss.circuit_set_active_element(elem)

                elem_name = dss.cktelement_name()

                elem_bus1 = dss.cktelement_read_bus_names()[0].split(".")[0]
                elem_bus2 = dss.cktelement_read_bus_names()[1].split(".")[0]

                if (elem_bus1 == bus) or (elem_bus2 == bus):
                    break

        while dss.circuit_parent_pd_element():

            elem_name = dss.cktelement_name()
            if elem_name.split(".")[0].lower() == "transformer":
                print(elem_name)
                load_transformer_dict[load_name] = elem_name
                
                break

        dss.loads_next()


if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))

    dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

    dss = py_dss_interface.DSSDLL()
    dss.text(f"compile [{dss_file}]")

    check_load_transformer(dss)