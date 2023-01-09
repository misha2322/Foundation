from lab1.CsvDoc import CsvDoc

test = CsvDoc('../1.csv', ',', names=['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'])
test.get_dim()
test.first_row(20)
test.describe()
test.group_data('class')
test.group_data('sepal-length')
test.draw1('box', 2, 2)
test.draw1('hist', 2, 2)
test.draw2('hist')
test.draw2('hist, kde')
