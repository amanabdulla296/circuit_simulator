# CircuitSimulator
It's a simulator of a DC circuit with 10V of the source, which contains 2 variable resistors and one fixed resistor. There is an ammeter after the fixed resistor and a voltmeter to check the potential change before and after the fixed resistor. Variable resistors are inversely proportional to each other, i.e. at 0 seconds R1=0 and R2=100, but when the time reached 10 seconds R1=100 and R2=0. For more details, please refer to the following circuit figure:

![image](https://user-images.githubusercontent.com/56832126/132469493-8dc2ec49-6b53-4611-b847-0f87d96e55bf.png)






## Contens
The whole module contains 4 classes as following:

- CircuitSimulator: this class starts (restarts) the simulation and provides actual values of voltmeter and ammeter.
- Ohmmeter: calculates the resistance of RL (fixed resistance) by registering itself to Voltmeter and Ammeter classes. Also, this class contains a method that calculates the last 2 seconds' rolling average of RL;
- Voltmeter: reads and prints voltage at Voltmeter at defined intervals;
- Ammeter: reads and prints current at Ammeter at defined intervals;


## Limitations:

- Asynchronous execution features need to be implemented;
- Rolling average calculation algorithm needs to be improved to make it simpler;
- Graph that shows the resultant signals needs to be implemented;
- Try/except lines should be added by checking different scenarios.

