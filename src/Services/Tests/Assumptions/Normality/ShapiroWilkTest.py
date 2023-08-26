from src.Utils.Test import Test

import scipy.stats as stats

class ShapiroWilkTest(Test):
    def execute(self):
        result = {}
        result["passed"] = True
        result["testResults"] = {}

        for column in self.dataSource.columns:
            shapiro = stats.shapiro(self.dataSource.valueObject[column])
            
            if (shapiro.pvalue < 0.05):
                result["passed"] = False

            result["testResults"][column] = {
                "isNormal": bool(shapiro.pvalue > 0.05),
                "statistic": shapiro.statistic,
                "pvalue": shapiro.pvalue
            }
            
        return result