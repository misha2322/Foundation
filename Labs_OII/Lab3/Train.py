from lab1.CsvDoc import CsvDoc
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score


class Train(CsvDoc):
    train = 4 / 5
    results = []
    names = []
    models = []

    def __init__(self, path, sep, names):
        super().__init__(path, sep, names)
        self.train_data = self.data.head(int(self.len() * self.train)) #типа первые 120
        self.test_data = self.data.tail(int(self.len() * 1 - self.train)) #типа все остольное до 150
        X = self.data.values[:, 0:4]
        y = self.data.values[:, 4]
        self.X_train, self.X_validation, self.Y_train, self.Y_validation \
            = train_test_split(X, y, test_size=1 - self.train, random_state=1)
        print("\ntrain:\n", self.train_data, "\ntest:\n", self.test_data)

    models.append(('Логистическая регрессия', LogisticRegression(solver='liblinear', multi_class='ovr')))
    models.append(('Линейный дискриминантный анализ', LinearDiscriminantAnalysis()))
    models.append(('Метод k-ближайших соседей', KNeighborsClassifier()))
    models.append(('Классификация и регрессия с помощью деревьев', DecisionTreeClassifier()))
    models.append(('Наивный байесовский классификатор', GaussianNB()))
    models.append(('Метод опорных векторов', SVC(gamma='auto')))

    def testtrain(self):
        for name, model in self.models:
            Kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
            cv_results = cross_val_score(model, self.X_train, self.Y_train, cv=Kfold, scoring='accuracy')
            self.results.append(cv_results)
            self.names.append(name)
            print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
