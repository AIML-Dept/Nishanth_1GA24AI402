from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(3, 3)

qc.h([0, 1, 2])

qc.measure([0, 1, 2], [0, 1, 2])

print("Quantum Circuit:")
print(qc.draw())

simulator = AerSimulator()
shots = 1024

job = simulator.run(qc, shots=shots)
result = job.result()


counts = result.get_counts()

print("\nMeasurement Counts:")
print(counts)

plot_histogram(counts)
plt.show()

print("\nExperimental Probabilities:")
for state in sorted(counts):
    probability = counts[state] / shots
    print(f"{state}: {probability:.3f}")

print("\nTheoretical Probability:")
print("Each of the 8 states has probability = 1/8 = 0.125")