import os
import pathlib
import py_dss_tools

dss_file = r"C:\GitHub\py-dss-tools\examples\feeders\123Bus\IEEE123Master.dss"

st = study = py_dss_tools.CreateStudy.power_flow(name:"Teste", dss_file)

st.dss.text("New EnergyMeter.Feeder Line.L115 1")
st.dss.text("solve")

print(os.path.dirname(os.path.abspath(__file__)))

st.view.voltage_profile()