from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def create_bell_state(state):
    circuit = QuantumCircuit(2, 2)

    # Create the Bell state
    circuit.h(0)
    circuit.cx(0, 1)

    if state == "Phi-":
        circuit.z(0)

    elif state == "Psi+":
        circuit.x(1)

    elif state == "Psi-":
        circuit.x(1)
        circuit.z(0)

    # Measure both qubits
    circuit.measure(0, 0)
    circuit.measure(1, 1)

    return circuit


# Initialize simulator
sim = AerSimulator()

states = ["Phi+", "Phi-", "Psi+", "Psi-"]

print("======================================")
print("       ALL FOUR BELL STATES")
print("======================================")

for state in states:

    qc = create_bell_state(state)

    result = sim.run(qc, shots=1024).result()
    distribution = result.get_counts()

    print("\nBell State:", state)
    print("Measurement Distribution:", distribution)
    print("--------------------------------------")