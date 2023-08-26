from src.Utils.Test import Test

from scipy import stats

class WilcoxonRankSumTest(Test):
    name = "Wilcoxon Rank-Sum Test"
    
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