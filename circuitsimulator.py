#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
from threading import Timer



class CircuitSimulator:
    """a class to simulate the circuit"""
 
    def __init__ (self, RL = 30000, Vs = 10):
        self.RL = RL
        self.Vs = Vs
        self.start_timestamp = 0
 
    def timestamp(self):
        """ tracks the time"""
        elapsed_time = time.time() - self.start_timestamp
        if (elapsed_time > 10):
            return 10
        else: 
            return round(elapsed_time, 1)
 
    def start_simulation(self):
        """methods to start the simulation"""
        self.start_timestamp = time.time()
 
 
    def restart_simulation(self):
        """restarts the simulation"""
        self.start_timestamp = time.time()
 
    def voltmeter_value(self):
        """calculates and returns value of the voltmeter"""
        return round(self.Vs * self.__r2L()/self.__r_total(), 2)
 
    def ammeter_value(self):
        """calculates and returns value of the voltmeter"""
        return (self.voltmeter_value()/self.RL)
 
 
    def __r1(self):
        """value of resistor 1 increases proportionally with time"""
        return 10000 * self.timestamp()
 
 
    def __r2(self):
        """value of resistor 2 inversly proportional to the time"""
        return 10000 * (10 - self.timestamp())
 
    def __r2L(self):
        """combined effect of resistor 2 and resistor L (parallely connected)"""
        r2 = self.__r2()
        return (r2 * self.RL)/(r2 + self.RL)
 
    def __r_total(self):
        """total resistance of the circuit"""
        return (self.__r1() + self.__r2L())
    
    def is_simulation_running(self):
        """to stop simulation after 10 seconds"""
        elapsed_time = time.time() - self.start_timestamp
        if (elapsed_time > 10):
            return False
        else: 
            return True

        
        
class Ohmmeter:
    """implements resistance change of RL"""
    def __init__(self, simulator:CircuitSimulator):
        self.simulator = simulator
        self.rl_values = {}
        self.last_voltage = -1
        self.last_current = -1
        self.__output_rl()
        
    def __output_rl(self):
        """outputs RL value and its rolling average for the last 2 seconds"""
        if self.simulator.is_simulation_running():
            if self.last_voltage != -1:
                print(f'RL: {round(self.last_voltage / self.last_current, 2)} Ohm\n')
                print(f'Rolling average: {round(self.rolling_avg(), 2)} Ohm\n')

            timer = Timer(1, self.__output_rl)
            timer.start()    
        
    def set_voltage(self, voltage):
        """registers RL whenever voltage changes"""
        self.last_voltage = voltage
        self.__collect_values()
        
    def set_current(self, current):
        """registers RL whenever current changes"""
        self.last_current = current
        self.__collect_values()
        
    def __collect_values(self):
        """collect RL values to calcualte rolling average"""
        if self.last_current > 0:
            rl = self.last_voltage / self.last_current
            self.rl_values[time.time()] = rl
        
    def rolling_avg(self):
        """calculate last 2 seconds rolling average from above collected values"""
        total_value = 0
        total_count = 0
        current_time = time.time()
        for timestamp, value in self.rl_values.items():
            if current_time - timestamp <= 2:
                total_value += value
                total_count += 1
        if total_count < 1:                #to prevent division by zero
            return -1
        return total_value / total_count

    
    
    
class Voltmeter:
    """Voltmeter values are calculated and printed in this class"""
    def __init__(self, simulator:CircuitSimulator, ohmmeter:Ohmmeter):
        self.simulator = simulator
        self.ohmmeter = ohmmeter
        self.last_value = -1
        self.last_timestamp = -1
        self.__read_voltmeter()
        
    def __read_voltmeter(self):
        """read the values of voltmeter"""
        self.last_value = self.simulator.voltmeter_value()
        self.ohmmeter.set_voltage(self.last_value)
        self.last_timestamp = time.time()
        print(f'Voltage: {self.last_value} V\n')
        if self.simulator.is_simulation_running():
            timer = Timer(0.1, self.__read_voltmeter)
            timer.start()
        
    def last_value(self):
        """ saves the last_values of voltmeter with respective timestamp"""
        return (self.last_value, self.last_timestamp)
        
        
        

class Ammeter:
    """Ammeter values are calculated and printed in this class"""
    
    def __init__(self, simulator:CircuitSimulator, ohmmeter:Ohmmeter):
        self.simulator = simulator
        self.ohmmeter = ohmmeter
        self.last_value = -1
        self.last_timestamp = -1
        self.__read_ammeter()
        
    def __read_ammeter(self):
        """read the values of ammeter"""
        self.last_value = self.simulator.ammeter_value()
        self.ohmmeter.set_current(self.last_value)
        self.last_timestamp = time.time()
        print(f'Current: {round(self.last_value*1000, 2)} mA\n')
        if self.simulator.is_simulation_running():
            timer = Timer(0.3, self.__read_ammeter)
            timer.start()
        
    def last_value(self):
        """ saves the last_values of voltmeter with respective timestamp"""
        return (self.last_value, self.last_timestamp)

