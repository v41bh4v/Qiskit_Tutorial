
from qiskit import *

qc = QuantumCircuit()
#Quantum registers
qr = QuantumRegister(2,'qreg')
#Giving it a name like 'qreg' is optional.
#Now we can add it to the circuit using the add_register method, and see that it has been added by checking the qregs variable of the circuit object.
qc.add_register( qr )
qc.qregs
#Adding Hadamard gate on Quantum register 0 
qc.h( qr[0] )
#We can also add a controlled-NOT using cx. This requires two arguments: control qubit, and then target qubit.
qc.cx( qr[0], qr[1] )
#We can see our circuit by draw()
qc.draw(output='mpl')


