from src.Services.Tests.ManyGroups.ManyGroupsService import ManyGroupsService
from src.Services.Tests.PairedGroups.PairedGroupsService import PairedGroupsService
from src.Services.Tests.TwoGroups.TwoGroupsService import TwoGroupsService
from src.Utils.DataSource import DataSource


class TestService():
    twoGroupsService: TwoGroupsService
    pairedGroupsService: PairedGroupsService
    manyGroupsService: ManyGroupsService
    dataSource: DataSource
    
    def __init__(self, dataSource: DataSource) -> None:
        self.dataSource = dataSource

        self.twoGroupsService = TwoGroupsService(dataSource)
        self.pairedGroupsService = PairedGroupsService(dataSource)
        self.manyGroupsService = ManyGroupsService(dataSource)
        
    def autoAnalyze(self):
        result = {}

        if (self.twoGroupsService.prereqPassed):
            result = self.twoGroupsService.analyze()
        elif (self.pairedGroupsService.prereqPassed):
            result = self.pairedGroupsService.analyze()
        elif (self.manyGroupsService.prereqPassed):
            result = self.manyGroupsService.analyze()

        result["descriptives"] = self.dataSource.descriptives
        
        return result

