# -*- coding: utf-8 -*-
# @Author  : Iury Ribeiro Zanelato
# @Email   : iury.ribeirozanelato@gmail.com
# @File    : Análise_alimentador.py
# @Software: PyCharm

from py_dss_interface import DSS
import pandas as pd
from dataclasses import dataclass, field
from typing import Tuple


class AnaliseAlimentador:
    def __init__(self, dss: DSS):
        self._dss = dss

    @property
    def analise_alimentador(self) -> pd.DataFrame:
        return self.__analise_alimentador()

    def __analise_alimentador(self) -> pd.DataFrame:
        buses = self._dss.solution.converged
        buses = self._dss.circuit.buses_vmag_pu
        buses = self._dss.topology.all_isolated_branches
        buses = self._dss.circuit.set_active_bus
        buses = self._dss.transformers.count
        buses = self._dss.loads.count
        buses = self._dss.circuit.set_active_element

        v_max = list()
        v_min = list()
        total_p = list()
        total_q = list()
        total_p_losses = list()
        x = list()
        PA = list()
        PB = list()
        PC = list()
        km_mv_lines = list()
        km_lv_lines = list()
        max_load_name = list()
        max_load_kw = list()

        summary_dict["Status"] = "Solved" if dss.solution.converged else "Not Solved"  #### como inserir?
        summary_dict["Good Voltage?"] = "Yes" if (v_min > 0.7 and v_max < 1.2) else "No"  #### como inserir?

        for bus in buses:
            self._dss.solution.converged(bus)
            PA = round_x(p[0] / total_p) * 100.0
            PB = round_x(p[0] / total_p) * 100.0
            PC = round_x(p[0] / total_p) * 100.0

            distance.append(self._dss.bus.distance)
            r1_list.append(zsc1[0])
            x1_list.append(zsc1[1])
            r0_list.append(zsc0[0])
            x0_list.append(zsc0[1])

        summary_dict_to_df = dict()
        summary_dict_to_df["Max pu. Voltage"] = v_max
        summary_dict_to_df["Min pu. Voltage"] = v_min
        summary_dict_to_df["Total P kW"] = total_p
        summary_dict_to_df["Total Q kVAr"] = total_q
        summary_dict_to_df["P Losses %"] = total_p_losses
        summary_dict_to_df["Num. Isolated Branches"] = len(x)
        summary_dict_to_df["PA Circuit %"] = PA
        summary_dict_to_df["PB Circuit %"] = PB
        summary_dict_to_df["PC Circuit %"] = PC
        summary_dict_to_df["Lines MV (km)"] = km_mv_lines
        summary_dict_to_df["Lines LV (km)"] = km_lv_lines
        summary_dict_to_df["Num. Tran"] = len(transformers.count)
        summary_dict_to_df["Num. Loads"] = len(loads.count)
        summary_dict_to_df["Max name of One Load"] = max_load_name
        summary_dict_to_df["Max kW of One Load"] = max_load_kw
        summary_dict_to_df["Loading max % transformers"] = transformers.name

        df = pd.DataFrame.from_summary_dict(summary_dict_to_df)

        return df
