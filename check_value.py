# -*- coding: utf-8 -*-
# @Time    : 7/14/2023 10:03 AM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : check_value.py
# @Software: PyCharm

import os
import pathlib
import py_dss_interface

def check_value(dss: py_dss_interface.DSS):
    dss.text("solve")

    # Check if line has x1 greater than a value (10 in this example)

    dss.lines.first()
    for _ in range(dss.lines.count):
        if dss.lines.x1 > 10:
            print(f"\nLine: {dss.lines.name} with the X1 {dss.lines.x1} greater than 10")
        dss.lines.next()


if __name__ == '__main__':
    script_path = os.path.dirname(os.path.abspath(__file__))

    dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

    dss = py_dss_interface.DSS()

    dss.text(f"compile [{dss_file}]")
    dss.text("New EnergyMeter.Feeder element=Line.L115 terminal=1")
    dss.text("Buscoords Buscoords.dat ")

    dss.text("edit Line.L67 x1=11")

    check_value(dss)