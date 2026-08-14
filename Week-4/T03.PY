from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

qc_ghz = QuantumCircuit(3, 3)

qc_ghz.h(0)
qc_ghz.cx(0, 1)
qc_ghz.cx(1, 2)
qc_ghz.x(2)

state_ghz = Statevector.from_instruction(qc_ghz)

qc_ghz.measure([0, 1, 2], [0, 1, 2])

print("=== HARD: MODIFIED 3-QUBIT GHZ STATE ===")
print("Circuit Diagram:")
print(qc_ghz.draw(output="text"))

print("\nAnalytical Statevector:")
print(state_ghz.data)

simulator = AerSimulator()
counts_ghz = simulator.run(qc_ghz, shots=1024).result().get_counts()

print("\nMeasurement Results (1024 shots):", counts_ghz)