from src.Services.Tests.ManyGroups.AnovaTest import AnovaTest
from src.Services.Tests.ManyGroups.KruskalWallisTest import KruskalWallisTest
from src.Utils.DataSource import DataSource
from src.Utils.Test import Test


class ManyGroupsService():
    parametricTest: AnovaTest
    alternativeTest: KruskalWallisTest
    prereqPassed: True
    
    def __init__(self, dataSource: DataSource) -> None:
        self.parametricTest = AnovaTest(dataSource)
        self.alternativeTest = KruskalWallisTest(dataSource)
        
        self.__checkPrerequisites(dataSource)
        self.parametricTest.checkAssumptions()


    def __checkPrerequisites(self, dataSource: DataSource):
        self.prereqPassed = bool(len(dataSource.columns) > 2)
    
    def analyze(self):
        returnValue = {}
        
        if (self.parametricTest.assumptionsPassed):
            returnValue = self.parametricTest.execute()
        else:
            returnValue = self.alternativeTest.execute()

        returnValue["assumptionsResults"] = self.parametricTest.assumptionsResults
        
        return returnValue
        