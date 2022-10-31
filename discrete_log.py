from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from math import pi
from qiskit.visualization import plot_histogram

#Defining a function 'inverse_qft' for n qubits, for performing inverse quantum forier transformation
def inverse_qft(n):
	qc = QuantumCircuit(n)  
	for qubit in range(n//2):   #initially swap gate is applied
		qc.swap(qubit, n-qubit-1)
	for i in range(n):           
		for j in range(i-1,-1,-1):
			qc.cp((-pi/2**(i-j)),j,i)    #controlled rotatio al gates and hadamard gate is applied
		qc.h(i)
	qc_gate = qc.to_gate()  #function is converted to gate qc_gate
	qc_gate.name = "  Inverse QFT"  #Newly desigend gate is named as Inverse QFT
	return qc_gate


#defining a function 'mod13' which performs 13^r(mod17) as the oracle
def mod13(iteration):
	qc = QuantumCircuit(5)
	for i in range(iteration):
		
		qc.cx(1,0)
		qc.cx(1,4)        #the circuit that performs a unitary  tarnsformation 13^r(mod17) inside the oracle
		qc.cx(0,1)
		qc.cx(1,0)
		qc.x(2)
		qc.cx(2,1)
		qc.x(0)
		qc.x(1)
		qc.x(2)
		qc.mct([0,1,2],4)
		qc.x(0)
		qc.x(1)
		qc.x(2)
#naming  the oracle to logical gates according to the power in modular exponentiation 		
		if(i==0):
			qc.name = " 13^1(mod17)"
		if(i==1):
			qc.name = " 13^2(mod17)"
		if(i==3):
			qc.name = " 13^4(mod17)"
		if(i==7):
			qc.name = " 13^8(mod17)"
		if(i==15):
			qc.name = " 13^16(mod17)"
			
	qc_gate = qc.to_gate() #converting the oracle to gate
	qc_controlled = qc_gate.control()
	return qc_controlled

#defining a function 'mod4'' that performs 4^r(mod17) inside the oracle
def mod4(iteration):
	qc = QuantumCircuit(5)
	for i in range (iteration):
	
		qc.swap(0,1) #circuit that performs the unitary transformation 4^r(mod17) inside the oracle
		qc.cx(2,0)
		qc.x(2)
		qc.cx(2,4)
#naming the oracle to logical gates according to the power in modular exponentiation 		
		if(i==0):
			qc.name = "4^1(mod17)"
		if(i==1):
			qc.name = "4^2(mod17)"
		if(i==3):
			qc.name = "4^4(mod17)"
		if(i==7):
			qc.name = "4^8(mod17)"
		if(i==15):
			qc.name = "4^16(mod17)"
	qc_gate = qc.to_gate()  #converting the oracle to logical gates
	qc_controlled = qc_gate.control()
	return qc_controlled

#Defining a quabtum register of 15 logical qubits and classical register of 10 memory cell to store the value of first 10  qubits after each measurement
my_circuit = QuantumCircuit(15,10)
my_circuit.h(range(10))
my_circuit.x(14)
#Appending the function mod4 and mod13 as oracle to last 5 qubits.
for qubit in range(5):
	my_circuit.append(mod4(2**qubit), [qubit] + [10,11,12,13,14])
for qubit in range(5,10,+1):
	my_circuit.append(mod13(2**(qubit-5)), [qubit] + [10,11,12,13,14])
#appending the gate for inverse quantum fourier transformation
my_circuit.append(inverse_qft(5), range(5))
my_circuit.append(inverse_qft(5), [5,6,7,8,9])
my_circuit.barrier()
my_circuit.measure(range(5),range(5)) #The first 5 qubits are measured initially
my_circuit.draw()     #The circuit is drawn

#Measurements are done by qasm simulator and the counts are converted to histogram for first 5 qubits.
simulator = Aer.get_backend('qasm_simulator')
result = ececute(my_circuit, backend = simulator, shots = 1024).result()
counts = result.get_counts()
print("Result: ", counts)
plot _histogram(counts)
	

#Measurements are done by qasm simulator and the counts are converted to histogram for the next 5 qubits.
simulator = Aer.get_backend('qasm_simulator')
result = ececute(my_circuit, backend = simulator, shots = 1024).result()
counts = result.get_counts()
print("Result: ", counts)
plot _histogram(counts)