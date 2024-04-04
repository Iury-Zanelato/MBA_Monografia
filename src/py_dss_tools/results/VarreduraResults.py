# -*- coding: utf-8 -*-
# @Author  : Iury Zanelato
# @Email   : iury.ribeirozanelato@gmail.com
# @File    : VarreduraResults.py
# @Software: PyCharm

import pandas as pd
from py_dss_interface import DSS
#from py_dss_tools.results.Summary.py import Summary
from py_dss_tools.results.Same_Bus import Same_Bus
from py_dss_tools.results.Isolated import Isolated
from py_dss_tools.results.Load_transformer import Load_Transformer
from py_dss_tools.results.Phases_Conections import Phases_Conections
from py_dss_tools.results.Transformer_data import Transformer_data


class VarreduraResults:
    def __init__(self, dss: DSS):
        self._dss = dss
        #Summary.__init__(self, self._dss)
        Same_Bus.__init__(self, self._dss)
        Isolated.__init__(self, self._dss)
        Load_Transformer.__init__(self, self._dss)
        Phases_Conections.__init__(self, self._dss)
        Transformer_data.__init__(self, self._dss)