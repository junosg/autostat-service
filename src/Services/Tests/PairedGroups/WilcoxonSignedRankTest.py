from src.Utils.Test import Test

from scipy import stats

class WilcoxonSignedRankTest(Test):
    name = "Wilcoxon Signed-Rank Test"
    
    def checkAssumptions(self):
        pass
    
    def execute(self):
        result = stats.wilcoxon(*self.dataSource.valueArray)
        
        returnValue = {
            "test": self.name,
            "statistic": result.statistic,
            "pvalue": result.pvalue
        }
        
        return returnValue