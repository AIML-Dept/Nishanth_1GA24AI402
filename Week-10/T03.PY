from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, pauli_error

simulator = AerSimulator()
messages = ["00", "01", "10", "11"]

print("CERTAIN BIT-FLIP ERROR")

for message in messages:
    qc = QuantumCircuit(2, 2)

    # Prepare Bell pair
    qc.h(0)
    qc.cx(0, 1)

    # Alice encodes
    if message[0] == "1":
        qc.z(0)
    if message[1] == "1":
        qc.x(0)

    # Bit-flip error on transmitted qubit
    qc.x(0)

    # Bob decodes
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])

    result = simulator.run(qc, shots=2048).result()
    counts = result.get_counts()
    decoded = max(counts, key=counts.get)[::-1]

    print("Sent:", message, "| Received:", decoded)

print("\nRANDOM BIT-FLIP ERROR, p = 0.20")

p = 0.20
noise_model = NoiseModel()
noise_model.add_quantum_error(
    pauli_error([("X", p), ("I", 1 - p)]),
    ["id"],
    [0]
)

noisy_simulator = AerSimulator(noise_model=noise_model)

for message in messages:
    qc = QuantumCircuit(2, 2)

    # Prepare Bell pair
    qc.h(0)
    qc.cx(0, 1)

    # Alice encodes
    if message[0] == "1":
        qc.z(0)
    if message[1] == "1":
        qc.x(0)

    # Noisy transmission channel
    qc.id(0)

    # Bob decodes
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])

    result = noisy_simulator.run(
        qc, shots=2048
    ).result()

    counts = result.get_counts()
    correct = counts.get(message[::-1], 0)
    success = correct / 2048 * 100

    print("Sent:", message)
    print("Counts:", {k[::-1]: v for k, v in counts.items()})
    print(f"Success rate: {success:.2f}%")
    print("-" * 30)