def loadTemps():

    july_temps_file = open('D:/Documents/6.00.2x/julyTemps.txt', 'r')
    july_temps_data = july_temps_file.readlines()

    low_temps = []
    high_temps = []

    for i in july_temps_data:
        fields = i.split(' ')
        if not (len(fields) < 3 or not fields[0].isdigit()):
            high_temps.append(fields[1])
            low_temps.append(fields[2][:2])

    return high_temps, low_temps

def diffTemps():
    diff_temps = []
    for i in range(len(loadTemps()[1])):
        diff_temps.append(int(loadTemps()[0][i]) - int(loadTemps()[1][i]))

    return diff_temps

def plotTemps():
    import pylab
    pylab.plot(range(1, len(diffTemps())))
    pylab.show()


print plotTemps()




