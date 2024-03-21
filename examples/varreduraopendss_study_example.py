# -*- coding: utf-8 -*-
# @Author  : Iury Zanelato
# @Email   : iury.ribeirozanelato@gmail.com
# @File    : varredura_opendss.py
# @Software: PyCharm

import os
import pathlib
import py_dss_tools

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

study = py_dss_tools.CreateStudy.varreduraopendss_study(name="Varredura OpenDSS", dss_file=str(dss_file))
study.dss.text("New EnergyMeter.M element=Transformer.Sub terminal=1")

#study.dss.text("New monitor.M1 element=Line.692675 terminal=1")
#study.dss.text("New monitor.M1_p element=Line.692675 terminal=1 mode=1 ppolar=no")
#study.dss.text("batchedit load..* daily=default")

study.dss.text("set mode=daily")
study.dss.text("solve")
df = study.results.short_circuit_impedances

study.run()

print(StudyVarredura)


