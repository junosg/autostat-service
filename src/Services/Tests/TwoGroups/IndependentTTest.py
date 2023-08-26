from src.Services.Tests.Assumptions.EqualVariance.LevenesTest import LevenesTest
from src.Services.Tests.Assumptions.Normality.ShapiroWilkTest import ShapiroWilkTest
from src.Utils.Test import Test

import scipy.stats as stats

class IndependentTTest(Test):
    name = "Independent T-test"
    
    def checkAssumptions(self):
        normalityTestResult = ShapiroWilkTest(self.dataSource).execute()
        levenesTestResult = LevenesTest(self.dataSource).execute()

        self.assumptionsPassed = bool(normalityTestResult["passed"] and levenesTestResult["passed"])
        self.assumptionsResults["normality"] = normalityTestResult
        self.assumptionsResults["equalVariance"] = levenesTestResult
    
    def execute(self):
        result = stats.ttest_ind(*self.dataSource.valueArray)
        
        returnValue = {
            "test": self.name,
            "statistic": result.statistic,
            "pvalue": result.pvalue,
            "assumptionsResults": self.assumptionsResults
        }
        
        return returnValue