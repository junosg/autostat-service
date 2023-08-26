from src.Utils.Test import Test

import scipy.stats as stats

class WilcoxonRankSumTest(Test):
    name = "Independent T-test"
    
    def checkAssumptions(self):
        pass
    
    def execute(self):
        result = stats.ranksums(*self.dataSource.valueArray)
        
        returnValue = {
            "test": self.name,
            "statistic": result.statistic,
            "pvalue": result.pvalue
        }
        
        return returnValue