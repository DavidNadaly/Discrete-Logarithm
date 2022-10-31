#Code for post processing the measured state. By writing the measured state as fraction the value of 's' (s is the index or discrete log of mod17) can be found.
#Initially first 5 qubits data are processed. 
#Measured state is a list of states with highest probablity that appear in the histogram plot.
#In the histogram plot the states are represented in binary form which is later converted to decimal form and divided by 1024 (1024 = 2^10, since we have 10 qubits for implementing modular exponentiation) then converted to fraction using fraction module


#Measured state of first 5 qubit in decimal form = 8,16,24
#Measured state of next 5 qubit in decimal form = 280,776,528


from fractions import Fraction
measured_state1 = [8, 16, 24, 280, 528, 776]
for x in range(len(measured_state1)):
	a = measured_state1[x]
	decimal = a/32
	z = Fraction(decimal)
	print("Measured_state: ",a, "   Decimal Value: ",decimal, "  Fraction", z)
	