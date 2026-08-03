from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)
qc.x(0)

state = Statevector.from_instruction(qc)

print("Statevector:", state.data)
print("\nCircuit Diagram:")
print(qc.draw(output="text"))

bloch_vector = [0, 0, -1]

plot_bloch_vector(
    bloch_vector,
    title="X Gate Applied on |0>"
)

plt.show()