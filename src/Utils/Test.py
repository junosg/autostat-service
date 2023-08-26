from abc import abstractmethod
from src.Utils.DataSource import DataSource

class Test():
    name = "defaultTest"
    assumptionsPassed = True
    assumptionsResults = {}
    
    dataSource: DataSource
    
    def __init__(self, dataSource: DataSource) -> None:
        self.dataSource = dataSource

    @abstractmethod
    def checkAssumptions(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass