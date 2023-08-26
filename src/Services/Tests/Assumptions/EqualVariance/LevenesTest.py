from src.Utils.Test import Test

from scipy import stats

class LevenesTest(Test):
    def execute(self):
        result = {}
        result["passed"] = True
        result["testResults"] = {}
        
        levenes = stats.levene(*self.dataSource.valueArray, center = "mean")
        
        result["passed"] = bool(levenes.pvalue > 0.05)
        result["testResults"] = {
            "areVariancesEqual": bool(levenes.pvalue > 0.05),
            "statistic": levenes.statistic,
            "pvalue": levenes.pvalue
        }
        
        return result