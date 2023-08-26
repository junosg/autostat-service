from src.Services.Tests.TwoGroups.IndependentTTest import IndependentTTest
from src.Services.Tests.TwoGroups.WilcoxonRankSumTest import WilcoxonRankSumTest
from src.Utils.DataSource import DataSource
from src.Utils.Test import Test


class TwoGroupsService():
    parametricTest: IndependentTTest
    alternativeTest: WilcoxonRankSumTest
    
    def __init__(self, dataSource: DataSource) -> None:
        self.parametricTest = IndependentTTest(dataSource)
        self.alternativeTest = WilcoxonRankSumTest(dataSource)
        
        self.parametricTest.checkAssumptions()

    def analyze(self):
        if (self.parametricTest.assumptionsPassed):
            return self.parametricTest.execute()
        else:
            return self.alternativeTest.execute()
        