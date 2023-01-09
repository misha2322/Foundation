import pandas as pd
from matplotlib import pyplot


class CsvDoc:
    def __init__(self, path, sep, names):
        if len(names) > 0:
            self.data = pd.read_csv(path, names=names, sep=sep)
        else:
            self.data = pd.read_csv(path, sep=sep)

    def print(self):
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(self.data)
            print('\n')

    def sort(self, col, asc):
        self.data = self.data.sort_values(by=col, ascending=asc)
        self.print()

    def get_row(self, index):
        print(self.data.take(index))
        print('\n')

    def len(self):
        return len(self.data)

    def save(self, name):
        self.data.to_csv(name, index=False)

    #from lab2
    def get_dim(self):
        print(self.data.shape)

    def first_row(self, count):
        print(self.data.head(count))

    def describe(self):
        print(self.data.describe())

    def group_data(self, group):
        print(self.data.groupby(by=group, axis=0, level=None, sort=True, group_keys=True, dropna=True).size())

    def draw1(self, type, layout_x, layout_y):
        self.data.plot(kind=type, subplots=True, layout=(layout_x, layout_y), sharex=False, sharey=False)
        pyplot.show()

    def draw2(self, type):
        pd.plotting.scatter_matrix(self.data, alpha=0.5, figsize=None, grid=False, diagonal=type, marker='.')
        pyplot.show()


