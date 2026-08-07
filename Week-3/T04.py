from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# Create a one-qubit quantum circuit
coin_qc = QuantumCircuit(1)

# Hadamard gate creates an equal superposition
coin_qc.h(0)

# Measure the qubit
coin_qc.measure_all()

# Run the simulation
simulator = AerSimulator()
result = simulator.run(coin_qc, shots=1000).result()
coin_counts = result.get_counts()

# Get heads and tails counts
heads = coin_counts.get("0", 0)
tails = coin_counts.get("1", 0)

total_trials = heads + tails
heads_percentage = (heads / total_trials) * 100
tails_percentage = (tails / total_trials) * 100

print("--- Quantum Coin Flip Results ---")
print(f"Heads (0): {heads} times ({heads_percentage:.2f}%)")
print(f"Tails (1): {tails} times ({tails_percentage:.2f}%)")

print("\nCircuit:")
print(coin_qc.draw(output="text"))

# Display the histogram
plot_histogram(
    coin_counts,
    title="Quantum Coin Flip Results"
)

plt.show()