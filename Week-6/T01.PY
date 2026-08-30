from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def simon_oracle_101():
    # 3 input qubits (0,1,2) and 3 output qubits (3,4,5)
    oracle = QuantumCircuit(6, name="Oracle_101")

    # Step 1: Copy input qubits to output qubits
    for i in range(3):
        oracle.cx(i, i + 3)

    # Step 2: Implement XOR logic for secret string s = '101'
    # s = 101 means flip q3 and q5 when MSB q2 = 1
    oracle.cx(2, 3)
    oracle.cx(2, 5)

    return oracle


# Create oracle
oracle_circuit = simon_oracle_101()

print("=== SIMON'S ORACLE ('101') ===")
print("Oracle Circuit Diagram:")
print(oracle_circuit.draw(output="text"))
print()

# Simulator
simulator = AerSimulator()

print("Input x  | Output f(x) | Matching Collision x XOR s")
print("-" * 60)

# Verify all 8 possible inputs
for x_int in range(8):

    x_str = format(x_int, "03b")

    qc = QuantumCircuit(6, 3)

    # Initialize input qubits according to x_str
    for i in range(3):
        if x_str[2 - i] == "1":
            qc.x(i)

    # Apply Simon oracle
    qc.compose(oracle_circuit, inplace=True)

    # Measure output qubits
    qc.measure([3, 4, 5], [0, 1, 2])

    # Run simulation
    result = simulator.run(qc, shots=1).result().get_counts()

    fx_str = list(result.keys())[0]

    # Calculate x XOR s
    x_xor_s = format(x_int ^ 0b101, "03b")

    print(f"{x_str:<8} | {fx_str:<11} | x XOR 101 = {x_xor_s}")