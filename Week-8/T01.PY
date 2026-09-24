from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)

qc.h(0)
qc.h(1)

qc.measure([0, 1], [0, 1])

print("=== TWO QUBIT SUPERPOSITION ===")
print("Circuit Diagram:")
print(qc.draw(output="text"))

simulator = AerSimulator()

result = simulator.run(qc, shots=1024).result()

counts = result.get_counts()

print("Measurement Results (1024 shots):", counts)