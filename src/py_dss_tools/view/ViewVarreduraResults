# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : ViewTemporalResults.py
# @Software: PyCharm

from py_dss_interface import DSS
from py_dss_tools.results import TemporalResults
from py_dss_tools.view.Monitor import Monitor


class ViewVarreduraResults(Monitor):

    def __init__(self, dss: DSS, results: VarreduraResults):
        self._dss = dss
        self._results = results
        Monitor.__init__(self, self._dss, self._results)
