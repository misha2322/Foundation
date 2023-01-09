from Meanshift import Mean_Shift

clf = Mean_Shift('../test.csv', ',', 1000)
clf.shuffle()
clf.fix(100)
clf.fit()
