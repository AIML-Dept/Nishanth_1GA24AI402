from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Create the Bell state |Psi+>
qc.h(0)
qc.cx(0, 1)
qc.x(1)

print("=== HARD: PARTIAL MEASUREMENT ON ENTANGLED STATE ===")

print("\nCircuit Diagram:")
print(qc.draw(output="text"))

# Get the initial statevector
state_initial = Statevector.from_instruction(qc)

print("\nInitial Joint Statevector:")
print(state_initial.data)

# Measure qubit 1
outcome, post_meas_state = state_initial.measure([1])

print("\nMeasured Qubit 1 Outcome:", outcome)

print("\nCollapsed Post-Measurement Statevector:")
print(post_meas_state.data)

# Display probabilities
print("\nProbabilities Before Measurement:")
print(state_initial.probabilities())

print("\nProbabilities After Measurement:")
print(post_meas_state.probabilities())