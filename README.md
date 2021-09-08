# circuit_simulator
Its a simulator of DC circuit, which contains 2 variable and one fixed resisters with 10V of source. There is and ammeter after fixed resister and voltmeter to check the potential change before and after fixed resister. Variable resistors are inversly proportional to each other, i.e. at 0 seconds R1=0 and R2=100, but when time reached to 10 seconds R1=100 and R2=0. For more details, please refer to the following cicuit figure:

![image](https://user-images.githubusercontent.com/56832126/132469493-8dc2ec49-6b53-4611-b847-0f87d96e55bf.png)






## Contens
there are 4 classes as following:

- CircuitSimulator: this class starts (restarts) the simulation and provides actual values of voltmeter and ammeter.
- Ohmmeter: calculates resistance of Rl (fixed resistance) by registering itself to Voltmeter and Ammeter classes. Also this class calculates last 2 seconds rolling average of RL;
- Voltmeter: reads and prints voltage at Voltmeter at defined intervals;
- Ammeter: reads and prints current at Ammeter at defined intervals;


## Limitations:

- Asynchronous execution features needs to be implemented;
- Rolling average calculation algorithm needs to be improved to make it simpler;
- Graph that shows the resultant signals needs to be implemented;
- Try except lines should be added by checking different scenarios.

