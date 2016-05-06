# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': True}
    mutProb = 0.005

    myViruses = []
    # creating viruses
    for i in range(numViruses):
        myViruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    drugAt = {0: [], 75: [], 150: [], 300: []}

    for j in range(numTrials):
        for k in drugAt.keys():
            patient = TreatedPatient(myViruses, maxPop)
            for l in range(k+150):
                patient.update()
                if l == k:
                    patient.addPrescription('guttagonol')
                if l == k+150-1:
                    drugAt[k].append(patient.update())

    for i in range(len(drugAt.keys())):
        pylab.subplot(2, 2, i+1)
        pylab.hist(drugAt[drugAt.keys()[i]], bins=20, label=str(drugAt.keys()[i]))
        pylab.legend()
        pylab.grid()
    pylab.show()

#print simulationDelayedTreatment(1000)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    myViruses = []
    # creating viruses
    for i in range(numViruses):
        myViruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    drugAt = {0: [], 75: [], 150: [], 300: []}

    for j in range(numTrials):
        for k in drugAt.keys():
            patient = TreatedPatient(myViruses, maxPop)
            for l in range(150+k+150):
                patient.update()
                if l == 150:
                    patient.addPrescription('guttagonol')
                if l == 150+k:
                    patient.addPrescription('grimpex')
                if l == 150+k+150-1:
                    drugAt[k].append(patient.update())

    for i in range(len(drugAt.keys())):
        pylab.subplot(2, 2, i+1)
        pylab.hist(drugAt[drugAt.keys()[i]], bins=20, label=str(drugAt.keys()[i]))
        pylab.legend()
        pylab.grid()
    pylab.show()

#simulationTwoDrugsDelayedTreatment(100)