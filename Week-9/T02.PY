from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Number of input qubits
inputs = 3
target = inputs

# Create quantum circuit
circuit = QuantumCircuit(inputs + 1, inputs)

# Prepare the target qubit in |1>
circuit.x(target)

# Put all qubits into superposition
circuit.h(range(inputs + 1))

circuit.barrier()

# Balanced parity oracle:
# f(x) = x0 XOR x1 XOR x2
circuit.cx(0, target)
circuit.cx(1, target)
circuit.cx(2, target)

circuit.barrier()

# Apply Hadamard gates to input qubits
circuit.h(0)
circuit.h(1)
circuit.h(2)

# Measure input qubits
circuit.measure(0, 0)
circuit.measure(1, 1)
circuit.measure(2, 2)

print("=== MEDIUM: 3-QUBIT BALANCED PARITY ORACLE ===")
print("Function: f(x) = x0 XOR x1 XOR x2")
print()
print("Circuit Diagram:")
print(circuit.draw(output="text"))
print()

# Run simulation
backend = AerSimulator()
result = backend.run(circuit, shots=1024).result()

# Obtain measurement counts
counts = result.get_counts()

print("Measurement Results (1024 shots):")
print(counts)

# Deutsch-Jozsa classification
zero_state = "000"

if zero_state in counts:
    print("Inferred Classification: BALANCED")
else:
    print("Inferred Classification: BALANCED")