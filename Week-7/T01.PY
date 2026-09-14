from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Initialize circuit:
# 2 qubits:
# q0 = input qubit
# q1 = ancilla qubit
# 1 classical bit
qc = QuantumCircuit(2, 1)

# Step 1: State preparation
qc.x(1)          # Set ancilla to |1>
qc.h(0)          # Input qubit into superposition
qc.h(1)          # Ancilla into |->

qc.barrier()

# Step 2: Oracle for BALANCED function f(x) = x
# If input q0 is |1>, flip ancilla q1
qc.cx(0, 1)

qc.barrier()

# Step 3: Interference on input qubit
qc.h(0)

qc.barrier()

# Step 4: Measure input qubit
qc.measure(0, 0)

# Display information
print("=== DEUTSCH'S ALGORITHM (BALANCED f(x)=x) ===")
print("Circuit Diagram:")
print(qc.draw(output="text"))
print()

# Run simulation
simulator = AerSimulator()

result = simulator.run(
    qc,
    shots=1024
).result()

counts = result.get_counts()

print(f"Measurement Counts (1024 shots): {counts}")

# Determine function type
if '0' in counts and len(counts) == 1:
    print("Function Type: Constant")
else:
    print("Function Type: Balanced")