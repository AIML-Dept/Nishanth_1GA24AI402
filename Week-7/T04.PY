from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def conceptual_classification_circuit():
    # Demonstration of phase kickback for binary classification
    # q0 = Feature register
    # q1 = Label / oracle ancilla

    qc = QuantumCircuit(2, 1)

    # -------------------------------------------------
    # Step 1: Encode feature state
    # -------------------------------------------------
    qc.h(0)

    # Prepare ancilla in |-> state
    qc.x(1)
    qc.h(1)

    qc.barrier()

    # -------------------------------------------------
    # Step 2: Classification Oracle
    # -------------------------------------------------
    # Modified boundary condition:
    # Apply X to q0 before and after the CNOT.
    # This reverses the feature condition being tagged.
    qc.x(0)
    qc.cx(0, 1)
    qc.x(0)

    qc.barrier()

    # -------------------------------------------------
    # Step 3: Interference
    # -------------------------------------------------
    qc.h(0)

    qc.barrier()

    # -------------------------------------------------
    # Step 4: Readout
    # -------------------------------------------------
    qc.measure(0, 0)

    return qc


# Build classifier circuit
qc_classifier = conceptual_classification_circuit()

# Display results
print("=== REAL-WORLD: MODIFIED PHASE KICKBACK BINARY CLASSIFICATION ===")
print("Conceptual Decision Circuit Diagram:")
print(qc_classifier.draw(output="text"))
print()

# Run simulation
simulator = AerSimulator()

result = simulator.run(
    qc_classifier,
    shots=1024
).result()

counts = result.get_counts()

print("Measurement Counts:", counts)

# Determine classification
measured_bit = max(counts, key=counts.get)

if measured_bit == "0":
    classification = "Class A"
else:
    classification = "Class B"

print(f"Measured Output: {measured_bit}")
print(f"Predicted Classification: {classification}")

print(
    "\nConceptual Mapping:\n"
    "1. Feature Encoding: Qubit q0 represents the feature state.\n"
    "2. Boundary Oracle: The modified oracle evaluates the opposite\n"
    "   feature condition relative to the original circuit.\n"
    "3. Phase Kickback: The |-> ancilla converts the oracle response\n"
    "   into a phase change on the feature state.\n"
    "4. Interference Readout: The final Hadamard converts the phase\n"
    "   difference into a computational-basis result.\n"
    "5. Classification: Output 0 corresponds to Class A, while\n"
    "   output 1 corresponds to Class B."
)