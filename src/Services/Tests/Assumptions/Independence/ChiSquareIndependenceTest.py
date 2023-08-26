import logging
from src.Utils.Test import Test

from scipy import stats
import numpy as np


class ChiSquareIndependenceTest(Test):
    name = "Chi-Square Test of Independence"
    
    def execute(self):
        result = {}
        result["passed"] = True
        result["testResults"] = {}

        logging.error(self.dataSource.valueArray)

        table = np.array(self.dataSource.valueArray)
        
        logging.error(table)

        chiSquare = stats.chi2_contingency(table[0])
        
        result["passed"] = bool(chiSquare.pvalue > 0.05)
        result["testResults"] = {
            "test": self.name,
            "areIndependent": result["passed"],
            "statistic": chiSquare.statistic,
            "pvalue": chiSquare.pvalue
        }
        
        return result
