from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def create_e91_pair():
    circuit = QuantumCircuit(2, 2)

    # Generate entangled pair
    circuit.h(0)
    circuit.cx(0, 1)

    # Measurement
    circuit.measure(0, 0)
    circuit.measure(1, 1)

    return circuit


# Create simulator
simulator = AerSimulator()

# Create E91 circuit
e91_circuit = create_e91_pair()

print("=== E91 QKD CONCEPT ===")
print("Circuit Diagram:")
print(e91_circuit.draw(output="text"))
print()

# Run 16 trials
result = simulator.run(
    e91_circuit,
    shots=16,
    memory=True
).result()

measurements = result.get_memory()

# Extract Alice and Bob results
alice = []
bob = []

for result_bit in measurements:
    alice.append(result_bit[1])
    bob.append(result_bit[0])

# Calculate matching results
matches = sum(a == b for a, b in zip(alice, bob))
total = len(alice)
match_rate = (matches / total) * 100

print("Alice's Results :", alice)
print("Bob's Results   :", bob)
print()

print("Matching Results:", matches, "/", total)
print(f"Key Match Rate: {match_rate:.2f}%")