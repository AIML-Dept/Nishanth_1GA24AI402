import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

ideal_circuit = QuantumCircuit(1)
ideal_circuit.h(0)

ideal_state = Statevector.from_instruction(ideal_circuit)

error_circuit = QuantumCircuit(1)
error_circuit.h(0)

phase_error = np.pi / 4
error_circuit.rz(phase_error, 0)

error_state = Statevector.from_instruction(error_circuit)

print("Ideal state:", ideal_state.data)
print("State with phase error:", error_state.data)
print("Phase error:", phase_error, "radians")

plot_bloch_multivector(
    ideal_state,
    title="Ideal State Bloch Sphere"
)
plt.show()

plot_bloch_multivector(
    error_state,
    title="State with Phase Error"
)
plt.show()