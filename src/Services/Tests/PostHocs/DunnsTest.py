import json
import logging
from src.Utils.Test import Test

from scipy import stats
import numpy as np
import scikit_posthocs as sp

class DunnsTest(Test):
    name = "Dunn's Test"
     
    def checkAssumptions(self):
        return super().checkAssumptions()
    
    def execute(self):
        result = sp.posthoc_dunn(self.dataSource.valueArray, p_adjust = 'bonferroni')
        
        dunn = {}

        for leftIndex, leftColumn in enumerate(self.dataSource.columns):
            for rightIndex, rightColumn in enumerate(self.dataSource.columns):
                if (leftIndex != rightIndex):
                    dunn[leftColumn + "-" + rightColumn] = {
                        "pvalue": result.values[leftIndex][rightIndex],
                    }

        returnValue = {
            "test": self.name,
            "result": dunn
        }

        return returnValue