# -*- coding: utf-8 -*-
# @Author  : Iury Zanelato
# @Email   : iury.ribeirozanelato@gmail.com
# @File    : varreduraopendss_example.py
# @Software: PyCharm

#########Tentativa 1
import os
import pandas as pd
import pathlib
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
    #print("Summary")
    #summary_result = dss.Summary
    #print(summary_result)

    # Verificando Same Bus
    print("Same Bus")
    same_bus_result = dss.Same_Bus()
    print(same_bus_result)

    # Verificando Isolated
    print("Isolated")
    isolated_result = dss.Isolated()
    print(isolated_result)

    # Verificando load_transformer
    print("load_transformer")
    load_transformer_result = dss.Load_transformer()
    print(load_transformer_result)

    # Verificando Phases Connections
    print("Phases Connections")
    phases_connections_result = dss.Phases_connections()
    print(phases_connections_result)

#Erro
#(242) OpenDSS
#Redirect File: "C:\GitHub\py-dss-tools\examples\feeders\1_ALPE_1\  feeder name
#0    1_ALPE_1.dss" Not Found.

'''
########Tentativa 2
script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

study = py_dss_tools.CreateStudy.varreduraopendss_study(name="Varredura OpenDSS", dss_file=str(dss_file))
study.dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
study.dss.text("Buscoords Buscoords.dat")

study.dss.text("solve")

study.dss.text("edit Line.L67 bus2=open") #Isolated
study.dss.text("MakebusList") #Isolated
study.dss.text("plot circuit") #Isolated
study.dss.text("All elements checked")
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

self._dss.meters.next() #load_transformer
self._dss.loads.name = "S37a" #load_transformer
self._dss.loads.kv = 4.16 #load_transformer
print(f"\nLoad: {self._dss.loads.name} with kV {self._dss.loads.kv} but should be {energymeter_voltage[self._dss.meters.name][0]}")
print(f"\nLoad: {self._dss.loads.name} with kV {self._dss.loads.kv} but should be {energymeter_voltage[self._dss.meters.name][0]}")
print(f"\nLoad: {self._dss.loads.name} with kV {self._dss.loads.kv} but should be {energymeter_voltage[self._dss.meters.name][1]}")
study.results.load_transformer


study.dss.text("New line.loop phases=3 bus1=79.1.2.3 bus2=450.1.2.3") #Summary
study.dss.text("Edit LINE.L114 enabled=no") #Summary
study.results.create_summary_dict
#Jogar Print(AnáliseAlimentador aqui ???)

#Resultados e Execução
summary_df = study.model.summary_df #Ajustar de acordo com o Summary.py
feeders = pd.read_csv("feeder.csv") #Rodar pelo csv??
study.run() #Apenas executar por aqui??

print("here")
'''''



