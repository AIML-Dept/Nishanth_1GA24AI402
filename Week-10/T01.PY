from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)

# Prepare shared Bell pair
qc.h(0)
qc.cx(0, 1)

# Alice encodes message 00 (no gate needed)

# Bob decodes
qc.cx(0, 1)
qc.h(0)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Simulate
simulator = AerSimulator()
result = simulator.run(qc, shots=2048, seed_simulator=2024).result()
counts = result.get_counts()

print("Message sent: 00")
print("Measurement counts:", counts)
print("Decoded message:", max(counts, key=counts.get))
print(qc.draw())