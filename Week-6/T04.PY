import matplotlib.pyplot as plt
import numpy as np

# String lengths from 3 to 30 bits
bit_lengths = np.arange(3, 31, 3)

# Quantum queries: Simon's algorithm requires approximately O(n) queries
quantum_queries = bit_lengths + 2

# Classical queries: Birthday Paradox requires approximately O(2^(n/2))
classical_queries = 2 ** (bit_lengths / 2)

print("=== REAL-WORLD: QUERY COMPLEXITY COMPARISON ===")
print("Bit Length (n) | Quantum Queries (n+2) | Classical Queries (2^(n/2))")
print("-" * 70)

# Display first 8 results
for n, q, c in zip(
    bit_lengths[:8],
    quantum_queries[:8],
    classical_queries[:8]
):
    print(f"{n:<14} | {q:<22} | {int(c):<25}")

# Create graph
plt.figure(figsize=(9, 5))

plt.plot(
    bit_lengths,
    classical_queries,
    "r-o",
    label="Classical (2^(n/2))"
)

plt.plot(
    bit_lengths,
    quantum_queries,
    "b-s",
    label="Quantum (n+2)"
)

# Logarithmic Y-axis
plt.yscale("log")

plt.xlabel(
    "Secret Bitstring Length (n)",
    fontsize=11
)

plt.ylabel(
    "Number of Oracle Queries (Log Scale)",
    fontsize=11
)

plt.title(
    "Query Complexity: Classical vs Simon's Algorithm",
    fontsize=12
)

plt.legend()

plt.grid(
    True,
    which="both",
    ls="--"
)

plt.tight_layout()

# Save graph
plt.savefig("simon_query_comparison.png")

print("\nPlot saved successfully as 'simon_query_comparison.png'.")