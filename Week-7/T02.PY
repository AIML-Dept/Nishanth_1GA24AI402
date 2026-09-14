from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Initialize circuit:
# q0 = input qubit
# q1 = ancilla qubit
# 1 classical bit
qc_medium = QuantumCircuit(2, 1)

# Step 1: State preparation
qc_medium.x(1)          # Set ancilla to |1>
qc_medium.h(0)          # Input qubit into superposition
qc_medium.h(1)          # Ancilla into |->

qc_medium.barrier()

# Step 2: Oracle for balanced function f(x) = 1 XOR x
# First apply CNOT for f(x) = x
qc_medium.cx(0, 1)

# Add X to implement the constant 1 part
qc_medium.x(1)

qc_medium.barrier()

# Step 3: Interference on input qubit
qc_medium.h(0)

qc_medium.barrier()

# Step 4: Measure input qubit
qc_medium.measure(0, 0)

# Display circuit
print("=== MEDIUM: DEUTSCH'S ALGORITHM (BALANCED f(x)=1 XOR x) ===")
print("Circuit Diagram:")
print(qc_medium.draw(output="text"))
print()

# Run simulation
simulator = AerSimulator()

result = simulator.run(
    qc_medium,
    shots=1024
).result()

counts = result.get_counts()

print(f"Measurement Counts (1024 shots): {counts}")

# Determine function type
if '0' in counts and len(counts) == 1:
    print("Function Type: Constant")
else:
    print("Function Type: Balanced")