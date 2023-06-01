# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : voltage_load.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import numpy as np


def check_voltage_load(dss: py_dss_interface.DSSDLL):
    dss.text("solve")

    dss.loads_first()


    for _ in range(dss.loads_count()):

        load_name = dss.loads_read_name()
        print(load_name)
        load_kv = dss.loads_read_kv()
        bus = dss.cktelement_read_bus_names()[0].split(".")[0]
        nodes = dss.cktelement_read_bus_names()[0].split(".")[1:]

        dss.circuit_set_active_bus(bus)
        vf_bus = dss.bus_kv_base()

        if (['1', '4'] == nodes) or (['2', '4'] == nodes) or (['3', '4'] == nodes) or (['1'] == nodes) or (['2'] == nodes) or (['3'] == nodes):
            load_v_type = "vf"

        else:
            load_v_type = "vl"
        #
        # if v_type == "vf":
        #     if v != vf_bus:
        #         print(f"Bus {bus} with voltage: {round(v,3)} different than vbase {round(vf_bus)}")
        #

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
                dss.transformers_write_wdg(2)
                trafo_kv = dss.transformers_read_kv()
                bus = dss.cktelement_read_bus_names()[0].split(".")[0]
                nodes = dss.cktelement_read_bus_names()[0].split(".")[1:]

                if (['1', '4'] == nodes) or (['2', '4'] == nodes) or (['3', '4'] == nodes) or (['1'] == nodes) or (
                        ['2'] == nodes) or (['3'] == nodes):
                    tr_v_type = "vf"
                    trafo_kv_f = trafo_kv / np.sqrt(3)
                else:
                    tr_v_type = "vl"
                    num_win = dss.transformers_read_num_windings()
                    if num_win == 3:
                        trafo_kv_f = trafo_kv / 2
                    else:
                        trafo_kv_f = trafo_kv / np.sqrt(3)

                if tr_v_type == load_v_type:
                    if round(trafo_kv, 3) != round(load_kv, 3):
                        print(f"Load {load_name} with different voltage then transformer {elem_name} - case vl")
                if load_v_type == "vf":
                    if round(trafo_kv_f, 3) != round(load_kv, 3):
                        print(f"Load {load_name} with different voltage then transformer {elem_name} - Case vf")

                break

        dss.loads_next()


if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))

    dss_file = pathlib.Path(script_path).joinpath("../feeders", "123Bus", "IEEE123Master.dss")

    dss = py_dss_interface.DSSDLL()
    dss_file = r"C:\Users\ppra005\Box\Documents_PC\PR\OpenDSS_Perdas\2-RoraimaFiles\Alimentadores CE-01_07_09\ArquivosOpenDSS_CE_AL2-01-CE_AL2-01_2023.02.16\Master_370_CE_AL2-01_Mes01_DO.dss"
    dss.text(f"compile [{dss_file}]")

    check_voltage_load(dss)