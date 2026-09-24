from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Number of input qubits
num_inputs = 3

# Create circuit: 3 input qubits + 1 auxiliary qubit
circuit = QuantumCircuit(num_inputs + 1, num_inputs)

# Prepare auxiliary qubit in |1>
circuit.x(num_inputs)

# Apply Hadamard gates to all qubits
circuit.h(range(num_inputs + 1))

circuit.barrier()

# Constant oracle: f(x) = 1
# Flip the auxiliary qubit
circuit.x(num_inputs)

circuit.barrier()

# Apply Hadamard gates to input qubits
circuit.h(range(num_inputs))

# Measure only the input qubits
circuit.measure(range(num_inputs), range(num_inputs))

print("=== EASY: CONSTANT ORACLE FOR 3 INPUT QUBITS ===")
print("Function: f(x) = 1")
print()
print("Circuit:")
print(circuit.draw(output="text"))
print()

# Run the circuit
simulator = AerSimulator()
result = simulator.run(circuit, shots=1024).result()

# Get measurement counts
counts = result.get_counts()

print("Measurement Results:", counts)

# Check whether all measured states are zero
if set(counts.keys()) == {"000"}:
    print("Inferred Classification: CONSTANT")
else:
    print("Inferred Classification: BALANCED")