import random

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator


# Select four random gates
gate_options = ["x", "h", "s", "t"]
random_sequence = random.choices(gate_options, k=4)

print("Selected gate sequence:", " → ".join(gate.upper() for gate in random_sequence))

# Create a one-qubit circuit
circuit = QuantumCircuit(1)

# Apply each selected gate
for gate in random_sequence:
    if gate == "x":
        circuit.x(0)
    elif gate == "h":
        circuit.h(0)
    elif gate == "s":
        circuit.s(0)
    elif gate == "t":
        circuit.t(0)

# Calculate the final statevector
final_state = Statevector.from_instruction(circuit)

print("\nFinal statevector:")
print(final_state.data)

print("\nMeasurement probabilities:")
print(final_state.probabilities_dict())

print("\nCircuit diagram:")
print(circuit.draw(output="text"))

# Create a separate circuit for measurement
measured_circuit = circuit.copy()
measured_circuit.measure_all()

simulator = AerSimulator()
result = simulator.run(measured_circuit, shots=500).result()
counts = result.get_counts()

print("\nSimulation results for 500 shots:")
print(counts)