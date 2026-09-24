import numpy as np
import matplotlib.pyplot as plt

# Range of input sizes
bits = list(range(2, 11))

# Calculate query requirements
classical = []
quantum = []

for n in bits:
    classical.append((2 ** (n - 1)) + 1)
    quantum.append(1)

print("=" * 70)
print("       DEUTSCH-JOZSA QUERY COMPLEXITY COMPARISON")
print("=" * 70)

print(f"{'Input Bits':<15}{'Classical Queries':<25}{'Quantum Queries':<20}")
print("-" * 70)

for n, c, q in zip(bits, classical, quantum):
    print(f"{n:<15}{c:<25}{q:<20}")

# Create the graph
fig, ax = plt.subplots(figsize=(10, 6))

ax.semilogy(
    bits,
    classical,
    marker="o",
    linewidth=2,
    label="Classical: 2^(n-1) + 1"
)

ax.semilogy(
    bits,
    quantum,
    marker="s",
    linestyle="--",
    linewidth=2,
    label="Quantum: 1 Query"
)

ax.set_title("Classical vs Quantum Query Complexity")
ax.set_xlabel("Number of Input Bits (n)")
ax.set_ylabel("Oracle Queries (Logarithmic Scale)")

ax.set_xticks(bits)
ax.grid(True, which="both", linestyle=":", alpha=0.7)
ax.legend()

plt.tight_layout()

# Save the graph
filename = "query_complexity_comparison.png"
plt.savefig(filename, dpi=300)

print("\nGraph generated successfully.")
print("Saved as:", filename)

plt.show()