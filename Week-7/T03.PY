from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_deutsch_circuit(oracle_type: str):
    qc = QuantumCircuit(2, 1)

    # Step 1: Prepare |01> -> |+->
    qc.x(1)
    qc.h(0)
    qc.h(1)

    qc.barrier()

    # Step 2: Select Oracle
    if oracle_type == "constant_0":
        # f(x) = 0
        pass

    elif oracle_type == "constant_1":
        # f(x) = 1
        qc.x(1)

    elif oracle_type == "balanced_identity":
        # f(x) = x
        qc.cx(0, 1)

    elif oracle_type == "balanced_not":
        # f(x) = NOT x
        qc.x(1)
        qc.cx(0, 1)

    else:
        raise ValueError("Unknown oracle type")

    qc.barrier()

    # Step 3: Interference
    qc.h(0)

    qc.barrier()

    # Step 4: Measurement
    qc.measure(0, 0)

    return qc


# -------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------

print("=== HARD: DEUTSCH'S ALGORITHM ===")
print("Testing Four Different Oracles")
print("=" * 60)

simulator = AerSimulator()

oracle_names = [
    "constant_0",
    "constant_1",
    "balanced_identity",
    "balanced_not"
]

results = {}

for name in oracle_names:

    circuit = build_deutsch_circuit(name)

    # Run 1000 shots
    result = simulator.run(
        circuit,
        shots=1000
    ).result()

    counts = result.get_counts()

    # Get measured result
    measured_bit = max(counts, key=counts.get)

    # Classify function
    if measured_bit == "0":
        classification = "CONSTANT"
    else:
        classification = "BALANCED"

    results[name] = measured_bit

    print(f"\nOracle: {name}")
    print(f"Measurement Counts: {counts}")
    print(f"Measured Output: {measured_bit}")
    print(f"Function Type: {classification}")

    print("-" * 60)


# -------------------------------------------------
# FINAL SUMMARY
# -------------------------------------------------

print("\n=== FINAL SUMMARY ===")

for oracle, output in results.items():

    if output == "0":
        function_type = "Constant"
    else:
        function_type = "Balanced"

    print(
        f"{oracle:<22} -> Output: {output} -> {function_type}"
    )