from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from math import pi
from qiskit.visualization import plot_histogram


def inverse_qft(n):
	qc = QuantumCircuit(n)
	for qubit in range(n//2):
		qc.swap(qubit, n-qubit-1)
	for i in range(n):
		for j in range(i-1,-1,-1):
			qc.cp((-pi/2**(i-j)),j,i)
		qc.h(i)
	qc_gate = qc.to_gate()
	qc_gate.name = "  Inverse QFT"
	return qc_gate


def mod13(iteration):
	qc = QuantumCircuit(5)
	for i in range(iteration):
		
		qc.cx(1,0)
		qc.cx(1,4)
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
			
	qc_gate = qc.to_gate()
	qc_controlled = qc_gate.control()
	return qc_controlled


def mod4(iteration):
	qc = QuantumCircuit(5)
	for i in range (iteration):
	
		qc.swap(0,1)
		qc.cx(2,0)
		qc.x(2)
		qc.cx(2,4)
		
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
	qc_gate = qc.to_gate()
	qc_controlled = qc_gate.control()
	return qc_controlled
	
my_circuit = QuantumCircuit(15,10)
my_circuit.h(range(10))
my_circuit.x(14)

for qubit in range(5):
	my_circuit.append(mod(2**qubit), [qubit] + [10,11,12,13,14])
for qubit in range(5,10,+1):
	my_circuit.append(mod14(2**(qubit-5)), [qubit] + [10,11,12,13,14])

my_circuit.append(inverse_qft(10), range(10))
my_circuit.barrier()
my_circuit.measure(range(5),range(5)) #The first 5 qubits are measured initially
my_circuit.draw()     #The circuit is drawn

simulator = Aer.get_backend('qasm_simulator')
result = ececute(my_circuit, backend = simulator, shots = 1024).result()
counts = result.get_counts()
print("Result: ", counts)
plot _histogram(counts)
	
