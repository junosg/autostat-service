import numpy as np
import scipy.stats as stats

class DataSource():
    valueObject = {}
    valueArray = []
    columns = []
    descriptives = {}
    predictor: str
    outcome: str

    def __init__(self, data, predictor, outcome):
        valueObject = {}
        valueArray = []
        columns = []

        dataNpArray = np.array(data)

        for item in dataNpArray:
            if item[predictor] in valueObject:
                valueObject[item[predictor]].append(item[outcome])
            else:
                valueObject[item[predictor]] = [item[outcome]]
                columns.append(item[predictor])

        for column in columns:
            valueArray.append(valueObject[column])

        self.valueObject = valueObject
        self.valueArray = valueArray
        self.columns = columns
        self.predictor = predictor
        self.outcome = outcome

        self.__setDescriptives()

    def __setDescriptives(self):
        descriptives = {}
        
        for column in self.columns:
            descriptive = stats.describe(self.valueObject[column])

            descriptives[column] = {
                "predictor": self.predictor,
                "outcome": self.outcome,
                "observationCount": len(self.valueObject[column]),
                "min": min(self.valueObject[column]),
                "max": max(self.valueObject[column]),
                "mean": descriptive.mean,
                "variance": descriptive.variance,
                "skewness": descriptive.skewness,
                "kurtosis": descriptive.kurtosis
            }
            
        self.descriptives = descriptives
        