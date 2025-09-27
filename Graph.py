import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

n_values = np.array([1000, 5000, 10000, 50000, 100000, 500000, 1000000])
experimental_ns = np.array([26375, 7875, 7708, 6042, 6167, 8209, 8000])
theory = np.array([13.351236, 18.244768, 20.450066, 25.765978, 28.131502, 33.781137, 36.276657])

# Adjust theory by scaling factor based on first point
scaling_factor = 0.7 * (experimental_ns[0] / theory[0])
adjusted_theory = theory * scaling_factor

plt.figure(figsize=(8, 6))
plt.plot(n_values, experimental_ns, 'o-', label='Experimental Results', color='brown', linewidth=2)
plt.plot(n_values, adjusted_theory, 'o-', label='Adjusted Theoretical Result', color='blue', linewidth=2)

plt.xscale('log')
plt.yscale('linear')


x_ticks = np.logspace(3, 6, num=7, base=10, dtype=int)
plt.xticks(x_ticks)

plt.gca().yaxis.set_major_formatter(ticker.ScalarFormatter())
plt.gca().yaxis.get_major_formatter().set_scientific(False)

plt.xlabel('n (log scale)')
plt.ylabel('Time (ns)')
plt.title('Experimental vs Adjusted Theoretical Results')

plt.legend(loc='center right', bbox_to_anchor=(1, 0.5), borderaxespad=0)
plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()
