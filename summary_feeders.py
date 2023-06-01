# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : summary_feeders.py
# @Software: PyCharm


import pandas as pd
import summary
import phases_connections
import py_dss_interface
import os
import pathlib

script_path = os.path.dirname(os.path.abspath(__file__))


feeders = pd.read_csv("feeder.csv")


feeder_summary = dict()
for index, row in feeders.iterrows():
    feeder = row["feeder name"]
    model_path = dss_file = pathlib.Path(script_path).joinpath("feeders", str(feeder), "000_master.dss")

    dss = py_dss_interface.DSS()

    dss.text(f"compile [{model_path}]")

    feeder_summary[feeder] = summary.create_summary(dss)

summary = pd.DataFrame.from_dict(feeder_summary).T
file = pathlib.Path(script_path).joinpath("summary_results.csv")
summary.to_csv(file)

