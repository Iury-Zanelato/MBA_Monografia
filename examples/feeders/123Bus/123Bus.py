import os
import py_dss_tools

dss_file = r"C:\IuryZanelato\GitHub\py-dss-tools\examples\feeders\123Bus\IEEE123Master.dss"

st = py_dss_tools.CreateStudy.power_flow("Test 1", dss_file)

st.dss.text("New EnergyMeter.Feeder Line.L115 1")
st.dss.text("solve")

print(os.path.dirname(os.path.abspath(__file__)))

st.view.voltage_profile()