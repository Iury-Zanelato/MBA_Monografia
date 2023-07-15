# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : feeders_analysis.py
# @Software: PyCharm


import pandas as pd
import summary
import phases_connections
import isolated
import same_buses
import summary
import py_dss_interface
import os
import pathlib
import load_transformer

script_path = os.path.dirname(os.path.abspath(__file__))


feeders = pd.read_csv("feeder.csv")


feeder_summary = dict()
for index, row in feeders.iterrows():
    feeder = row["feeder name"]
    model_path = dss_file = pathlib.Path(script_path).joinpath("feeders", str(feeder), "000_master.dss")

    print(f"\n{feeder}")
    dss = py_dss_interface.DSS()

    dss.text(f"compile [{model_path}]")

    print("Summary")
    print(summary.create_summary(dss))

    print("Same Bus")
    same_buses.check_same_buses(dss)

    print("Isolated")
    isolated.check_isolated(dss)

    print("load_transformer")
    load_transformer.check_load_transformer(dss)

    print("Phases Connections")
    phases_connections.check_phases_connections(dss)

