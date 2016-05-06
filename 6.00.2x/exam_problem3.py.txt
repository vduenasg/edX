import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    for i in range(CURRENTRABBITPOP):
        rabbitReproduction = 1.0 - (CURRENTRABBITPOP*1.0 / MAXRABBITPOP)

        if random.random() <= rabbitReproduction:
            CURRENTRABBITPOP += 1


def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for i in range(CURRENTFOXPOP):
        successfulHunt = CURRENTRABBITPOP*1.0 / MAXRABBITPOP

        if random.random() <= successfulHunt:
            if CURRENTRABBITPOP > 10:
                CURRENTRABBITPOP -= 1
                if random.random() >= 1.0/3:
                    CURRENTFOXPOP += 1
        else:
            if random.random() <= 0.1:
                if CURRENTFOXPOP > 10:
                    CURRENTFOXPOP -= 1


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    myRabbits = []
    myFoxes = []
    for i in range(numSteps):
        rabbitGrowth()
        myRabbits.append(CURRENTRABBITPOP)
        foxGrowth()
        myFoxes.append(CURRENTFOXPOP)
    return (myRabbits, myFoxes)

def plotSimulation():
    rabbits, foxes = runSimulation(200)
    pylab.plot(rabbits, label='Rabbits')
    pylab.plot(foxes, label='Foxes')
    a, b, c = pylab.polyfit(range(len(rabbits)), rabbits, 2)
    pylab.plot(pylab.polyval([a, b, c], range(len(rabbits))), label='Rabbits')
    d, e, f = pylab.polyfit(range(len(foxes)), foxes, 2)
    pylab.plot(pylab.polyval([d, e, f], range(len(foxes))), label='Foxes')
    pylab.grid()
    pylab.legend()
    pylab.show()
plotSimulation()
