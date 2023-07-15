# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : summary.py
# @Software: PyCharm

import py_dss_interface
import pandas as pd
import os
import pathlib
import numpy as np

x = 2

def round_x(y):
    return round(y, x)

def create_summary(dss: py_dss_interface.DSS):
    summary_dict = dict()
    dss.text("set mode=snapshot")
    dss.text("solve")

    summary_dict["Status"] = "Solved" if dss.solution.converged else "Not Solved"
    v_array = np.array(dss.circuit.buses_vmag_pu)
    v_array = v_array[v_array > 0.1]
    v_max = round_x(v_array.max())
    v_min = round_x(v_array.min())
    summary_dict["Max pu. Voltage"] = v_max
    summary_dict["Min pu. Voltage"] = v_min
    summary_dict["Good Voltage?"] = "Yes" if (v_min > 0.7 and v_max < 1.2) else "No"
    total_p = round_x(-dss.circuit.total_power[0])
    total_q = round_x(-dss.circuit.total_power[1])
    total_p_losses = round_x(dss.circuit.losses[0] / 1000.0)
    summary_dict["Total P kW"] = round_x(total_p)
    summary_dict["Total Q kvar"] = round_x(total_q)
    summary_dict["P Losses %"] = round_x(100.0 * total_p_losses / total_p)
    x = dss.topology.all_isolated_branches
    if "NONE" in x:
        x.remove("NONE")
    if x:
        summary_dict["Num. Isolated Branches"] = len(x)
    else:
        summary_dict["Num. Isolated Branches"] = 0
    # summary_dict["Loop?"] = "Yes" if dss.topology_looped_branch() > 0 else "No"

    dss.circuit.set_active_element("vsource.source")
    p = -1 * np.array(dss.cktelement.powers[0:6:2])

    summary_dict["PA Circuit %"] = round_x(p[0] / total_p) * 100.0
    summary_dict["PB Circuit %"] = round_x(p[1] / total_p) * 100.0
    summary_dict["PC Circuit %"] = round_x(p[2] / total_p) * 100.0

    km_mv_lines = 0
    km_lv_lines = 0
    dss.lines.first()
    for _ in range(dss.lines.count):

        bus = dss.lines.bus1

        dss.circuit.set_active_bus(bus)

        if 4 not in dss.bus.nodes:
            km_mv_lines = km_mv_lines + dss.lines.length

        else:
            km_lv_lines = km_lv_lines + dss.lines.length

        dss.lines.next()

    summary_dict["Lines MV (km)"] = round_x(km_mv_lines)
    summary_dict["Lines LV (km)"] = round_x(km_lv_lines)

    summary_dict["Num. Tran"] = dss.transformers.count

    summary_dict["Num. Loads"] = dss.loads.count / 2

    max_load_kw = 0
    max_load_name = None
    dss.loads.first()
    for _ in range(dss.loads.count):
        if dss.loads.kw > max_load_kw:
            max_load_kw = dss.loads.kw
            max_load_name = dss.loads.name

        dss.loads.next()

    summary_dict["Max name of One Load"] = max_load_name
    summary_dict["Max kW of One Load"] = max_load_kw

    tr_c = list()
    dss.transformers.first()
    for _ in range(dss.transformers.count):
        dss.circuit.set_active_element(f"transformer.{dss.transformers.name}")

        p = sum(dss.cktelement.powers[:int(len(dss.cktelement.powers) / 2): 2])
        p_n = dss.transformers.kva

        tr_c.append(p / p_n * 100)

        dss.transformers.next()

    summary_dict["Loading max % transformers"] = np.max(tr_c)

    return summary_dict


if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))

    dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

    dss = py_dss_interface.DSS()

    dss.text(f"compile [{dss_file}]")

    summary_without_issue_dict = create_summary(dss)
    print(summary_without_issue_dict)

    dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

    dss.text(f"compile [{dss_file}]")
    dss.text("New line.loop phases=3 bus1=79.1.2.3 bus2=450.1.2.3")
    dss.text("Edit LINE.L114 enabled=no")
    dss.text("calcvoltage")

    summary_with_issue_dict = create_summary(dss)
    print(summary_with_issue_dict)

