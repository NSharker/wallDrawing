import matplotlib.pyplot as plt





wallCoordinateFile = open('wallCoordinate.txt', 'r')

xCoordinates = []
yCoordinates = []


for coordinatesString in wallCoordinateFile.readlines():
    coordinateSplit = coordinatesString[1:-2].split(', ')
    #print ("coord[0] = ")
    #print (coordinateSplit[0])
    #print ("coord[1] = ")
    #print (coordinateSplit[1])
    xCoordinates.append(float(coordinateSplit[0]))
    yCoordinates.append(float(coordinateSplit[1]))


xCoordinateRobot = [9.6347360611]
yCoordinateRobot = [20.1799144745]


plt.plot(xCoordinates, yCoordinates, 'ro', xCoordinateRobot, yCoordinateRobot, 'g^')

plt.show()
