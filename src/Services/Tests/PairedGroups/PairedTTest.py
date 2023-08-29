from src.Services.Tests.Assumptions.EqualVariance.LevenesTest import LevenesTest
from src.Services.Tests.Assumptions.Normality.ShapiroWilkTest import ShapiroWilkTest
from src.Utils.Test import Test

from scipy import stats

class PairedTTest(Test):
    name = "Paired T-test"
    
    def checkAssumptions(self):
        normalityTestResult = ShapiroWilkTest(self.dataSource).execute()
        equalVarianceTestResult = LevenesTest(self.dataSource).execute()

        self.assumptionsPassed = bool(normalityTestResult["passed"] and equalVarianceTestResult["passed"])
        self.assumptionsResults["normality"] = normalityTestResult
        self.assumptionsResults["equalVariance"] = equalVarianceTestResult

    def execute(self):
        result = stats.ttest_rel(*self.dataSource.valueArray)

        returnValue = {
            "test": self.name,
            "statistic": result.statistic,
            "pvalue": result.pvalue,
        }
        
        return returnValue