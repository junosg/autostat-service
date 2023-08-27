from src.Services.Tests.TwoGroups.IndependentTTest import IndependentTTest
from src.Services.Tests.TwoGroups.WilcoxonRankSumTest import WilcoxonRankSumTest
from src.Utils.DataSource import DataSource
from src.Utils.Test import Test


class TwoGroupsService():
    parametricTest: IndependentTTest
    alternativeTest: WilcoxonRankSumTest
    prereqPassed: True
    
    def __init__(self, dataSource: DataSource) -> None:
        self.parametricTest = IndependentTTest(dataSource)
        self.alternativeTest = WilcoxonRankSumTest(dataSource)
        
        self.__checkPrerequisites(dataSource)
        self.parametricTest.checkAssumptions()

    def __checkPrerequisites(self, dataSource: DataSource):
        self.prereqPassed = bool(len(dataSource.columns) == 2)

    def analyze(self):
        returnValue = {}
        
        if (self.parametricTest.assumptionsPassed):
            returnValue = self.parametricTest.execute()
        else:
            returnValue = self.alternativeTest.execute()

        returnValue["assumptionsResults"] = self.parametricTest.assumptionsResults
        
        return returnValue
        