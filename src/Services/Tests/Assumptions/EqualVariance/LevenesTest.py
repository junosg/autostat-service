from src.Utils.Test import Test

from scipy import stats

class LevenesTest(Test):
    name = "Levene's Test"
    def execute(self):
        result = {}
        result["passed"] = True
        result["testResults"] = {}
        
        levenes = stats.levene(*self.dataSource.valueArray, center = "mean")
        
        result["passed"] = bool(levenes.pvalue > 0.05)
        result["testResults"] = {
            "test": self.name,
            "areVariancesEqual": result["passed"],
            "statistic": levenes.statistic,
            "pvalue": levenes.pvalue
        }
        
        return result