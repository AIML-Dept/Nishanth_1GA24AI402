from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0, 1)

state = Statevector.from_instruction(qc)

print("CNOT WITH SUPERPOSITION CONTROL")
print(qc.draw(output="text"))
print("\nResulting Statevector:")
print(state.data)
print("\nState Label:")
print(state.draw(output="repr"))