#!/usr/bin/env python
# coding: utf-8

# In[10]:

# import classes for simulation
import circuitsimulator as cs

# construct the simulator object
simulator = cs.CircuitSimulator()

# start the simulator object
simulator.start_simulation()

# construct ohmmeter object
ohmmeter = cs.Ohmmeter(simulator)

# construct voltmeter object
voltmeter = cs.Voltmeter(simulator, ohmmeter)

# construct ammeter object
ammeter = cs.Ammeter(simulator, ohmmeter)



