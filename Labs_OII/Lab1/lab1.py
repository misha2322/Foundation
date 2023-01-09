from CsvDoc import CsvDoc

test = CsvDoc('../1.csv', ',', names=['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'])
test.print()
test.get_row([1, 3, 7])
test.sort(['sepal-length'], True)
test.get_row([1, 3, 7])
test.sort(['sepal-length'], False)
print(test.len())
test.save('2.csv')
