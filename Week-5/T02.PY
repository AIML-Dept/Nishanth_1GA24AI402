from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def measure_in_x_basis(state_type: str):
    qc = QuantumCircuit(1, 1)

    # Step 1: Prepare computational basis state
    if state_type == "0":
        qc.id(0)          # Prepare |0>
    elif state_type == "1":
        qc.x(0)           # Prepare |1>

    # Step 2: Convert X-basis measurement to Z-basis
    qc.h(0)

    # Step 3: Measure
    qc.measure(0, 0)

    # Step 4: Run simulator
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1024).result()
    counts = result.get_counts()

    return qc, counts


print("=== MEDIUM: X-BASIS MEASUREMENT ===")

# Test |0> state
qc_zero, counts_zero = measure_in_x_basis("0")

print("\n1. Circuit for |0> measured in X-Basis:")
print(qc_zero.draw(output="text"))
print("Counts for |0> state:", counts_zero)


# Test |1> state
qc_one, counts_one = measure_in_x_basis("1")

print("\n2. Circuit for |1> measured in X-Basis:")
print(qc_one.draw(output="text"))
print("Counts for |1> state:", counts_one)


# Calculate probabilities
zero_0 = counts_zero.get("0", 0)
zero_1 = counts_zero.get("1", 0)

one_0 = counts_one.get("0", 0)
one_1 = counts_one.get("1", 0)

print("\n=== MEASUREMENT PROBABILITIES ===")

print("\nFor |0> state:")
print(f"P(0) = {zero_0 / 1024:.4f}")
print(f"P(1) = {zero_1 / 1024:.4f}")

print("\nFor |1> state:")
print(f"P(0) = {one_0 / 1024:.4f}")
print(f"P(1) = {one_1 / 1024:.4f}")