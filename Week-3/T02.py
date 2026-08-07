from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def create_minus_state():
    circuit = QuantumCircuit(1)

    # Apply X gate to convert |0⟩ into |1⟩
    circuit.x(0)

    # Apply Hadamard gate:
    # H|1⟩ = (|0⟩ - |1⟩) / √2 = |-⟩
    circuit.h(0)

    return circuit


qc = create_minus_state()
minus_state = Statevector.from_instruction(qc)

print("Quantum state: |->")
print("Statevector:", minus_state.data)
print("Probabilities:", minus_state.probabilities_dict())

print("\nCircuit:")
print(qc.draw(output="text"))