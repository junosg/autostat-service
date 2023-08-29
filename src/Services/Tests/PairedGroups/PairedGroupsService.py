from src.Services.Tests.PairedGroups.PairedTTest import PairedTTest
from src.Services.Tests.PairedGroups.WilcoxonSignedRankTest import WilcoxonSignedRankTest
from src.Utils.DataSource import DataSource
from src.Utils.Test import Test


class PairedGroupsService():
    parametricTest: PairedTTest
    alternativeTest: WilcoxonSignedRankTest
    prereqPassed: True
    
    def __init__(self, dataSource: DataSource) -> None:
        self.parametricTest = PairedTTest(dataSource)
        self.alternativeTest = WilcoxonSignedRankTest(dataSource)
        
        self.__checkPrerequisites(dataSource)
        self.parametricTest.checkAssumptions()

    def __checkPrerequisites(self, dataSource: DataSource):
        self.prereqPassed = bool(len(dataSource.columns) == 2) and dataSource.predictorPaired

    def analyze(self):
        returnValue = {}
        
        if (self.parametricTest.assumptionsPassed):
            returnValue = self.parametricTest.execute()
        else:
            returnValue = self.alternativeTest.execute()

        returnValue["assumptionsResults"] = self.parametricTest.assumptionsResults
        
        return returnValue
        