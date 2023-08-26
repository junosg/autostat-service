import numpy as np
import scipy.stats as stats

class DataSource():
    valueObject = {}
    valueArray = []
    columns = []
    descriptives = {}

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

        self.__setDescriptives()

    def __setDescriptives(self):
        for column in self.columns:
            descriptives = stats.describe(self.valueObject[column])

            self.descriptives[column] = {
                "observationCount": len(self.valueObject[column]),
                "min": min(self.valueObject[column]),
                "max": max(self.valueObject[column]),
                "mean": descriptives.mean,
                "variance": descriptives.variance,
                "skewness": descriptives.skewness,
                "kurtosis": descriptives.kurtosis
            }
        