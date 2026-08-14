from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def build_full_adder(a_bit: int, b_bit: int, cin_bit: int):

    qc = QuantumCircuit(4, 2)

    if a_bit:
        qc.x(0)
    if b_bit:
        qc.x(1)
    if cin_bit:
        qc.x(2)

    qc.ccx(0, 1, 3)
    qc.cx(0, 1)
    qc.ccx(1, 2, 3)
    qc.cx(2, 1)

    qc.cx(0, 1)

    qc.measure([1, 3], [0, 1])

    return qc

print("=== REAL-WORLD: MODIFIED FULL-ADDER ===")

test_a, test_b, test_cin = 1, 0, 1

qc_adder = build_full_adder(test_a, test_b, test_cin)

print(f"Testing Inputs: A={test_a}, B={test_b}, Cin={test_cin}")
print("Circuit Diagram:")
print(qc_adder.draw(output="text"))

simulator = AerSimulator()

counts_adder = simulator.run(
    qc_adder,
    shots=100
).result().get_counts()

print("\nSimulation Result (Outcome string 'Cout Sum'):", counts_adder)