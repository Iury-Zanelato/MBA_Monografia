# -*- coding: utf-8 -*-
# @Author  : Iury Zanelato
# @Email   : iury.ribeirozanelato@gmail.com
# @File    : varredura_opendss.py
# @Software: PyCharm

from py_dss_interface import DSS
import pandas as pd
from dataclasses import dataclass, field
from typing import Tuple

class Transformer:

    def __init__(self, dss: DSS):
        self._dss = dss
        self.summary_dict = pd.DataFrame()

    def summary_dict(self, v_array > 0.1, v_array.max, v_array.min, total_p, total_q, total_p_losses) -> pd.DataFrame:
        self._v_array = v_array
        self._v_array.max = v_array.max
        self._v_array.min = v_array.min
        self._total_p = total_p
        self._total_q = total_q
        self._total_p_losses = total_p_losses

        self._dss.text("solve")


summary_with_issue_dict = create_summary(dss)
print(summary_with_issue_dict)
return summary_dict

