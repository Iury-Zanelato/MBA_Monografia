# -*- coding: utf-8 -*-
# @Time    : 7/14/2023 3:32 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : transformer_data.py
# @Software: PyCharm


import os
import pathlib
import py_dss_interface

def tr_3_wdg(dss: py_dss_interface.DSS):
    dss.text("solve")

    dss.transformers.first()
    for _ in range(dss.transformers.count):
        num_wdg = dss.transformers.num_windings

        if num_wdg == 3:
            dss.transformers.wdg = 3
            if dss.transformers.kv == 12.47:
                print(f"transformer {dss.transformers.name} with kv missing")

            wdg_3_bus = dss.cktelement.bus_names[-1].lower()

            if wdg_3_bus == f"{dss.transformers.name.lower()}_3":
                print(f"transformer {dss.transformers.name} with bus missing")


        dss.transformers.next()


if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))

    dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

    dss = py_dss_interface.DSS()

    dss.text(f"compile [{dss_file}]")
    dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
    dss.text("Buscoords Buscoords.dat ")

    dss.text("New Transformer.t phases=1  windings=3 buses=[sourcebus A.4.2] conns=[  Wye] kvs=[ 0.22 0.22] kvas=[15 15 15] %loadloss=2.033333 %noloadloss=0.6")

    tr_3_wdg(dss)
