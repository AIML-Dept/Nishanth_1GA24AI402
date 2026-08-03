import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram

circuit = QuantumCircuit(3)

circuit.h([0, 1, 2])

result_state = Statevector.from_instruction(circuit)
state_values = result_state.to_dict()

print("Generated Quantum State:")
for basis, amplitude in state_values.items():
    print(f"|{basis}> : {amplitude}")

probabilities = np.abs(result_state.data) ** 2

print("\nMeasurement Probabilities:")
for index, probability in enumerate(probabilities):
    print(f"State |{index:03b}> probability = {probability:.4f}")

total = probabilities.sum()

print("\nTotal Probability:", total)

if np.isclose(total, 1.0):
    print("Verification Passed: Probabilities are normalized.")
else:
    print("Verification Failed: Probabilities are not normalized.")

print("\nCircuit Diagram:")
print(circuit.draw(output="text"))

plot_histogram(
    result_state.probabilities_dict(),
    title="Three-Qubit Measurement Probabilities"
)
plt.show()