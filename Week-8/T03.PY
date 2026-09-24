from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a quantum circuit with 2 qubits and 2 classical bits
circuit = QuantumCircuit(2, 2)

# Prepare Bell state
circuit.h(0)
circuit.cx(0, 1)

# Separate state preparation and measurement
circuit.barrier()

# Convert to Hadamard/X basis
for qubit in range(2):
    circuit.h(qubit)

# Measure the qubits
circuit.measure(0, 0)
circuit.measure(1, 1)

print("=== HARD: BELL PAIR - HADAMARD BASIS ===")
print("\nQuantum Circuit:")
print(circuit.draw(output="text"))

# Run simulation
backend = AerSimulator()
job = backend.run(circuit, shots=1024)
result = job.result()

# Get measurement distribution
results = result.get_counts()

print("\nX-Basis Measurement Results:")
print(results)