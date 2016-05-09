import pylab, random, math


class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        current_location = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = current_location.move(xDist, yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'This drunk is named ' + self.name


def walkVector(field, drunk, num_steps):
    start = field.getLoc(drunk)
    for i in range(num_steps):
        field.moveDrunk(drunk)
    return(field.getLoc(drunk).getX() - start.getX(),
           field.getLoc(drunk).getY() - start.getY())


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)]
        return random.choice(stepChoices)


def simWalks(num_steps, num_trials, drunk_class):
    homer = drunk_class
    origin = Location(0.0, 0.0)
    distances = []
    for i in range(num_trials):
        field = Field()
        field.addDrunk(homer, origin)
        distances.append(walkVector(field, homer, num_steps))
    return distances


def getFinalLocations(num_steps, num_trials, drunk_class):
    locations = []
    drunk = drunk_class
    origin = Location(0.0, 0.0)
    for i in range(num_trials):
        my_field = Field()
        my_field.addDrunk(drunk, origin)
        for j in range(num_steps):
            my_field.moveDrunk(drunk)
        locations.append(my_field.getLoc(drunk))
    return locations


def plotLocations(drunks, num_steps, num_trials):
    for i in range(len(drunks)):
        locations = getFinalLocations(num_steps, num_trials, drunks[i])
        xVals, yVals = [], []
        for j in locations:
            xVals.append(j.getX())
            yVals.append(j.getY())
        pylab.subplot(2, 3, i+1)
        pylab.xlim(-100, 100)
        pylab.ylim(-100, 100)
        pylab.plot(xVals, yVals, 'ro', label=drunks[i].name)
        pylab.legend()
        pylab.grid()
    pylab.show()

myDrunks = [UsualDrunk('UsualDrunk'), ColdDrunk('ColdDrunk'), EDrunk('EDrunk'), PhotoDrunk('PhotoDrunk'), DDrunk('DDrunk')]

plotLocations(myDrunks, 1500, 500)


