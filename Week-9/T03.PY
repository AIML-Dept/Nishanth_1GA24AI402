from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def deutsch_jozsa(n, oracle):
    # n input qubits + 1 auxiliary qubit
    circuit = QuantumCircuit(n + 1, n)

    # Prepare auxiliary qubit
    circuit.x(n)

    # Create superposition
    circuit.h(range(n + 1))

    circuit.barrier()

    # Apply oracle
    if oracle == "constant":
        # f(x) = 1
        circuit.x(n)

    elif oracle == "balanced":
        # Balanced parity function
        for qubit in range(n):
            circuit.cx(qubit, n)

    else:
        raise ValueError("Oracle must be 'constant' or 'balanced'")

    circuit.barrier()

    # Interference on input qubits
    circuit.h(range(n))

    # Measurement
    circuit.measure(range(n), range(n))

    return circuit


# Simulator
backend = AerSimulator()

print("==============================================")
print(" GENERALIZED DEUTSCH-JOZSA ALGORITHM")
print(" Input Qubits: 2 to 5")
print("==============================================")

for number_of_qubits in range(2, 6):

    print(f"\n--- Number of Input Qubits: {number_of_qubits} ---")

    for oracle in ("constant", "balanced"):

        circuit = deutsch_jozsa(number_of_qubits, oracle)

        result = backend.run(
            circuit,
            shots=500
        ).result()

        measurements = result.get_counts()

        # Find the most frequently measured state
        dominant_state = max(
            measurements,
            key=measurements.get
        )

        # Deutsch-Jozsa classification
        zero_state = "0" * number_of_qubits

        if dominant_state == zero_state:
            answer = "Constant"
        else:
            answer = "Balanced"

        print(f"Oracle Type : {oracle}")
        print(f"Measurement : {measurements}")
        print(f"Classification : {answer}")

print("\n==============================================")
print("Execution Completed")
print("==============================================")