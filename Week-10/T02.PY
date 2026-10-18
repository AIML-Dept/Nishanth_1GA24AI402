from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

simulator = AerSimulator()
messages = ["00", "01", "10", "11"]

for message in messages:
    qc = QuantumCircuit(2, 2)

    # Prepare Bell pair
    qc.h(0)
    qc.cx(0, 1)

    # Alice encodes the message
    if message[0] == "1":
        qc.z(0)
    if message[1] == "1":
        qc.x(0)

    # Bob decodes
    qc.cx(0, 1)
    qc.h(0)

    # Measure
    qc.measure([0, 1], [0, 1])

    result = simulator.run(
        qc, shots=2048, seed_simulator=2024
    ).result()

    counts = result.get_counts()
    decoded = max(counts, key=counts.get)[::-1]

    print("Sent:", message)
    print("Decoded:", decoded)
    print("Counts:", {k[::-1]: v for k, v in counts.items()})
    print("-" * 30)