from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import math

# 1. Create a single-qubit biased superposition circuit
qc = QuantumCircuit(1, 1)

# Rotate qubit by 60 degrees
qc.ry(math.pi / 3, 0)

# Measure the qubit
qc.measure(0, 0)

# Create simulator
simulator = AerSimulator()

# Different shot counts
shots_list = [100, 1000, 10000]

print("=== QUANTUM MEASUREMENT PROBABILITY CONVERGENCE ===")
print("Circuit Layout:")
print(qc.draw(output="text"))

print("\nShot Count | Counts (0, 1) | P(0) Measured | P(1) Measured")
print("-" * 65)

for shots in shots_list:
    result = simulator.run(qc, shots=shots).result()
    counts = result.get_counts()

    count_0 = counts.get("0", 0)
    count_1 = counts.get("1", 0)

    p_0 = count_0 / shots
    p_1 = count_1 / shots

    print(
        f"{shots:<10} | "
        f"{'0:' + str(count_0) + ', 1:' + str(count_1):<15} | "
        f"{p_0:<14.4f} | "
        f"{p_1:<14.4f}"
    )

# Theoretical probabilities
theoretical_p0 = math.cos(math.pi / 6) ** 2
theoretical_p1 = math.sin(math.pi / 6) ** 2

print("\n=== THEORETICAL PROBABILITIES ===")
print(f"P(0) theoretical = {theoretical_p0:.4f}")
print(f"P(1) theoretical = {theoretical_p1:.4f}")