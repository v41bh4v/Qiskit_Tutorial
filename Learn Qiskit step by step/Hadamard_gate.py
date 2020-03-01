
from qiskit import *

qc =QuantumCiruit()
#Quantum registers
qr = QuantumRegister(2,'qreg')
#Giving it a name like 'qreg' is optional.
#Now we can add it to the circuit using the add_register method, and see that it has been added by checking the qregs variable of the circuit object.
qc.add_register( qr )

qc.qregs
#We can see our circuit by draw()
qc.draw(output='mpl')

qc.h( qr[0] )