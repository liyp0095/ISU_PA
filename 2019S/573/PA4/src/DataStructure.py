import numpy as np
import util


class Data:
    feature = np.array(0)
    label = np.array(0)

    def __init__(self):
        pass


class DataStructure:
    data_name = ""
    feature_name = []
    label_class = []
    shape = (0, 0)
    train_set = Data()
    test_set = Data()

    def __init__(self, train_file_name="", test_file_name="", first_line_name=True):
        self.load_data(train_file_name=train_file_name,
                       test_file_name=test_file_name,
                       first_line_name=first_line_name)
        pass

    def load_csv_file(self, filename, first_line_name):
        feature = []
        label = []
        for i in util.read_csv_file(filename):
            if first_line_name:
                first_line_name = False
                continue
            tra = i[0:-1]
            lab = i[-1]
            feature.append(tra)
            label.append(lab)
        return np.array(feature).astype(float), np.array(label).astype(float)

    def load_data(self, train_file_name="", test_file_name="", first_line_name=True):
        if train_file_name != "":
            self.train_set.feature, self.train_set.label = self.load_csv_file(train_file_name, first_line_name)
        if test_file_name != "":
            self.test_set.feature, self.test_set.label = self.load_csv_file(test_file_name, first_line_name)
