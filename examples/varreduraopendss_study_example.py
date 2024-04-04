# -*- coding: utf-8 -*-
# @Author  : Iury Zanelato
# @Email   : iury.ribeirozanelato@gmail.com
# @File    : varreduraopendss_example.py
# @Software: PyCharm

import os
import pathlib
import py_dss_tools

script_path = os.path.dirname(os.path.abspath(__file__))
feeders = pd.read_csv("feeder.csv")

feeder_summary = dict()
for index, row in feeders.iterrows():
    feeder = row["feeder name"]
    model_path = dss_file = pathlib.Path(script_path).joinpath("feeders", str(feeder), "000_master.dss")

    print(f"\n{feeder}")
    dss = py_dss_interface.DSS()

    dss.text(f"compile [{model_path}]")


script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

study = py_dss_tools.CreateStudy.varreduraopendss_study(name="Varredura OpenDSS", dss_file=str(dss_file))
study.dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
study.dss.text("Buscoords Buscoords.dat")

study.dss.text("solve")

study.dss.text("edit Line.L67 bus2=open") #Isolated
print(f"{name} bus1: {bus1}")
print(f"{name} bus1: {bus1}")
study.results.isolated

study.dss.text("edit Line.L67 bus2=67") #Same_Bus
print(f"\nElement: {elem_name} with the same bus1 {bus1} and bus2 {bus2}")
study.results.same_bus

study.dss.text("edit LINE.L74 Bus1=73.1") #Phases_Connections
print(f"\nPhase issue between (Case 1):\nParent: {parent_elem_name} with bus {parent_elem_bus2} and nodes {parent_elem_nodes2}"
      f"\nElement: {elem_name} with bus {elem_bus1} and nodes {elem_nodes1}")
print(f"\nPhase issue between (Case 3):\nParent: {parent_elem_name} with bus {parent_elem_bus2} and nodes {parent_elem_nodes2}"
      f"\nElement: {elem_name} with bus {elem_bus2} and nodes {elem_nodes2}")
print(f"\nPhase issue between (Case 4):\nParent: {parent_elem_name} with bus {parent_elem_bus1} and nodes {parent_elem_nodes1}"
      f"\nElement: {elem_name} with bus {elem_bus2} and nodes {elem_nodes2}")
study.results.phases_connections
study.results.phase_connection


self._dss.meters.next()
self._dss.loads.name = "S37a"
self._dss.loads.kv = 4.16
print(f"\nLoad: {self._dss.loads.name} with kV {self._dss.loads.kv} but should be {energymeter_voltage[self._dss.meters.name][0]}")
print(f"\nLoad: {self._dss.loads.name} with kV {self._dss.loads.kv} but should be {energymeter_voltage[self._dss.meters.name][0]}")
print(f"\nLoad: {self._dss.loads.name} with kV {self._dss.loads.kv} but should be {energymeter_voltage[self._dss.meters.name][1]}")
study.results.load_transformer

#Resultados e Execução
summary_df = study.model.summary_df #Ajustar de acordo com o Summary.py
feeders = pd.read_csv("feeder.csv") #Rodar pelo csv??
study.run() #Apenas executar por aqui??

print("here")

'''''
study.dss.text("edit Line.L67 bus2=open") #Isolated
study.dss.text("edit Line.L67 bus2=67") #Same_Bus
study.dss.text("edit LINE.L74 Bus1=73.1") #Phases_Connections
study.dss.text("New Transformer.t phases=1  windings=3 buses=[sourcebus A.4.2] conns=[Wye] kvs=[0.22 0.22] "  ????
                "kvas=[15 15 15] %loadloss=2.033333 %noloadloss=0.6") #Transformer_Data                       ????
study.dss.text("New line.loop phases=3 bus1=79.1.2.3 bus2=450.1.2.3") #Summary
study.dss.text("Edit LINE.L114 enabled=no") #Summary

study.dss.text("MakebusList") #Isolated
study.dss.text("plot circuit") #Isolated
study.dss.text("All elements checked")
'''''

#study.results.summary
study.results.isolated
study.results.same_bus
study.results.transformer_data
study.results.phases_connections
study.results.phase_connection
study.results.load_transformer
#df = study.results.analise_alimentador



