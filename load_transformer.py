# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : load_transformer.py
# @Software: PyCharm

import py_dss_interface
import os
import pathlib
import numpy as np


def check_load_transformer(dss: py_dss_interface.DSS):
    dss.text("solve")

    dss.text("batchedit energymeter..* enabled=no")

    energymeter_voltage = dict()
    dss.transformers.first()
    for _ in range(dss.transformers.count):
        # 1 - Get buses
        # 2 - for in transformers
        # 3 - Bank? Vll 3ph

        dss.text(f"new energymeter.{dss.transformers.name} "
                 f"element=transformer.{dss.transformers.name} terminal=1")

        dss.circuit.set_active_element(f"transformer.{dss.transformers.name}")

        tr_ph = dss.cktelement.num_phases

        if tr_ph == 3:
            dss.transformers.wdg = 2
            vll = dss.transformers.kv
            vln = dss.transformers.kv / np.sqrt(3)

        elif tr_ph == 1:
            num_wdg = dss.transformers.num_windings

            if num_wdg == 2:
                dss.transformers.wdg = 2
                vln = dss.transformers.kv
                vll = vln
            elif num_wdg == 3:
                dss.transformers.wdg = 2
                vln = dss.transformers.kv
                vll = 2 * vln

        energymeter_voltage[dss.transformers.name] = (round(vll, 2), round(vln, 2))

        dss.transformers.next()
    dss.text("solve")

    dss.meters.first()
    for _ in range(dss.meters.count):
        loads = dss.meters.all_pce_in_zone

        for load in loads:
            if load.split(".")[0].lower() == "load":
                dss.circuit.set_active_element(load)
                load_ph = dss.cktelement.num_phases

                vll = energymeter_voltage[dss.meters.name][0]
                vln = energymeter_voltage[dss.meters.name][1]

                if load_ph == 3:
                    if round(dss.loads.kv, 2) != vll:
                        print(f"\nLoad: {dss.loads.name} with kV {dss.loads.kv} but should be {energymeter_voltage[dss.meters.name][0]}")
                elif load_ph == 1:
                    nodes = dss.cktelement.bus_names[0].split(".")[1:]

                    if ("1" in nodes and "2" in nodes) or ("1" in nodes and "3" in nodes) or ("3" in nodes and "2" in nodes):
                        if round(dss.loads.kv, 2) != vll:
                            print(f"\nLoad: {dss.loads.name} with kV {dss.loads.kv} but should be {energymeter_voltage[dss.meters.name][0]}")
                    elif "1" in nodes or "2" in nodes or "3" in nodes:
                        if round(dss.loads.kv, 2) != vln:
                            print(f"\nLoad: {dss.loads.name} with kV {dss.loads.kv} but should be {energymeter_voltage[dss.meters.name][1]}")

        dss.meters.next()
if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))

    dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

    dss = py_dss_interface.DSS()

    dss.text(f"compile [{dss_file}]")
    dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
    dss.text("Buscoords Buscoords.dat ")

    dss.loads.name = "S37a"
    dss.loads.kv = 4.16

    check_load_transformer(dss)