from TrafficData import TrafficData

test = TrafficData()
test.read('../traffic_data.txt')
test.split()
test.train()
test.regres()
test.test()
test.predict()