from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def get_statevector(gate_name):
    """Create a one-qubit circuit and return its final statevector."""
    
    circuit = QuantumCircuit(1)
    gate = gate_name.upper()

    if gate == "X":
        circuit.x(0)
    elif gate == "Y":
        circuit.y(0)
    elif gate == "Z":
        circuit.z(0)
    else:
        raise ValueError("Gate must be X, Y, or Z.")

    return Statevector.from_instruction(circuit)


pauli_gates = ["X", "Y", "Z"]

for gate in pauli_gates:
    result = get_statevector(gate)

    print(f"\n--- Pauli-{gate} Gate Result ---")
    print("Initial state: |0⟩")
    print(f"Final statevector: {result.data}")
    print(f"Measurement probabilities: {result.probabilities_dict()}")