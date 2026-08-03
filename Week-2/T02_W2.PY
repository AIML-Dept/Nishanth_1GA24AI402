from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)

qc.h(0)
qc.s(0)

state = Statevector.from_instruction(qc)

plot_bloch_multivector(
    state,
    title="Bloch Sphere after H and S Gates"
)

plt.show()