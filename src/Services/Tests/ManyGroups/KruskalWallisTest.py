from src.Services.Tests.PostHocs.DunnsTest import DunnsTest
from src.Utils.Test import Test
from scipy import stats

class KruskalWallisTest(Test):
    name = "Kruskal-Wallis H Test"
    
    def checkAssumptions(self):
        pass
    
    def execute(self):
        result = stats.kruskal(*self.dataSource.valueArray)
        
        returnValue = {
            "test": self.name,
            "statistic": result.statistic,
            "pvalue": result.pvalue,
            "assumptionsResults": self.assumptionsResults
        }
        
        if (result.pvalue < 0.05):
            returnValue["postHoc"] = DunnsTest(self.dataSource).execute()

        return returnValue