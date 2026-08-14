from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc_bell = QuantumCircuit(2, 2)

qc_bell.x(1)
qc_bell.h(0)
qc_bell.cx(0, 1)

qc_bell.measure([0, 1], [0, 1])

print("=== MEDIUM: PSI+ BELL STATE ===")
print("Circuit Diagram:")
print(qc_bell.draw(output="text"))

simulator = AerSimulator()
counts_bell = simulator.run(qc_bell, shots=1024).result().get_counts()

print("\nMeasurement Results (1024 shots):", counts_bell)