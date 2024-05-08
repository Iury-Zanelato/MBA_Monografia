# -*- coding: utf-8 -*-
# @Author  : Iury Zanelato
# @Email   : iury.ribeirozanelato@gmail.com
# @File    : varreduraopendss_example.py
# @Software: PyCharm

import os
import pathlib
import pandas as pd
import py_dss_interface
import py_dss_tools

script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pd.read_csv(r"C:\GitHub\py-dss-tools\feeder.csv")
study = py_dss_tools.CreateStudy.varreduraopendss_study(name="Varredura OpenDSS", dss_file=str(dss_file))

feeder_Summary = dict()
for index, row in dss_file.iterrows():
    feeder = row["feeder name"]
    model_path = pathlib.Path(script_path).joinpath("feeders", str(feeder), "000_master.dss")

    print(f"\n{feeder}")
    dss = py_dss_interface.DSS()

    dss.text(f"compile [{model_path}]")

    # Verificando Summary
    print("Summary")
    summary_dict = study.results.summary
    print(summary_dict)

    # Verificando Same Bus
    print("Same Bus")
    same_bus_result = study.results.same_bus
    print(same_bus_result)

    # Verificando Isolated
    print("Isolated")
    isolated_result = study.results.isolated
    print(isolated_result)

    # Verificando load_transformer
    print("load_transformer")
    load_transformer_result = study.results.load_transformer
    print(load_transformer_result)

    # Verificando Phases Connections
    print("Phases Connections")
    phases_connections_result = study.results.phases_connections
    print(phases_connections_result)



