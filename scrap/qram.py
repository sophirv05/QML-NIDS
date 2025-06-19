from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, transpile

from qiskit_ibm_runtime import QiskitRuntimeService

from qiskit_ibm_runtime import SamplerV2 as Sampler

service = QiskitRuntimeService()
backend = service.backend("ibm_rensselaer", instance="rpi-rensselaer/classes/itws-4940-callab")


q = QuantumRegister(12, 'q')
c = ClassicalRegister(1, 'c')

circuit = QuantumCircuit(q,c)

### Addressing ###

#q[0],q[1] -> Memory cell
#  0    0  -> 00
#  0    1  -> 01
#  1    0  -> 10
#  1    1  -> 11

#circuit.x(q[0])
#circuit.x(q[1])

### Routing nodes ####
circuit.cx(q[0],q[2])
circuit.x(q[3])
circuit.cx(q[2],q[3])

circuit.ccx(q[1],q[2],q[4])
circuit.cx(q[4],q[2])

circuit.ccx(q[1],q[3],q[5])
circuit.cx(q[5],q[3])

circuit.x(q[11]) #Write mode (read mode if commented)

### Writing to memory cell ###
circuit.ccx(q[11],q[4],q[9])
circuit.ccx(q[11],q[5],q[8])
circuit.ccx(q[11],q[2],q[7])
circuit.ccx(q[11],q[3],q[6])

circuit.barrier(q)

### Reading memory cell ###
circuit.ccx(q[4],q[9],q[10])
circuit.ccx(q[5],q[8],q[10])
circuit.ccx(q[2],q[7],q[10])
circuit.ccx(q[3],q[6],q[10])

circuit.barrier(q)
circuit.measure(q[10],c[0]) # Measuring readout qubit 

circuit.draw(output='mpl', filename='QRAM.png')
 

compiled_circuit = transpile(circuit, backend)
sampler = Sampler(backend)
sampler.options.default_shots = 100
job = sampler.run([compiled_circuit])

result = job.result() 

pub_result = job.result()[0]


counts = pub_result.data.c.get_counts()
print(f">>> Hardware counts: {counts}")

print(circuit)
print(counts)