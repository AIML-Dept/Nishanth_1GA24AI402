import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

N = 100
SEED = 2024

rng = np.random.default_rng(SEED)
payload = "".join(rng.choice(["0", "1"], size=2 * N))

messages = [
    payload[i:i + 2]
    for i in range(0, len(payload), 2)
]

circuits = []

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

    # Bob decodes
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])

    circuits.append(qc)

simulator = AerSimulator()
compiled = transpile(circuits, simulator)

result = simulator.run(
    compiled, shots=1, seed_simulator=SEED
).result()

received = ""

for i in range(N):
    counts = result.get_counts(i)
    received += max(counts, key=counts.get)[::-1]

print("First 20 bits sent:     ", payload[:20])
print("First 20 bits received: ", received[:20])

correct = sum(a == b for a, b in zip(payload, received))
print(f"Correct bits: {correct}/{2 * N}")

print("\nRESOURCE COMPARISON")
print("Classical bits sent:", 2 * N)
print("Superdense qubits sent at message time:", N)
print("Bell pairs consumed:", N)
print("Qubits sent earlier to share Bell pairs:", N)
print("Total carriers including pair distribution:", 2 * N)