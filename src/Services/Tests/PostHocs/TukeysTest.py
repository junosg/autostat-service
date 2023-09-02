import json
import logging
from src.Utils.Test import Test

from scipy import stats
import numpy as np

class TukeysTest(Test):
    name = "Tukey's Test"
     
    def checkAssumptions(self):
        return super().checkAssumptions()
    
    def execute(self):
        result = stats.tukey_hsd(*self.dataSource.valueArray)
        
        tukey = {}

        for leftIndex, leftColumn in enumerate(self.dataSource.columns):
            for rightIndex, rightColumn in enumerate(self.dataSource.columns):
                if (leftIndex != rightIndex):
                    tukey[leftColumn +"-" + rightColumn] = {
                        "statistic": result.statistic[leftIndex][rightIndex],
                        "pvalue": result.pvalue[leftIndex][rightIndex]
                    }

        returnValue = {
            "test": self.name,
            "result": tukey
        }

        return returnValue