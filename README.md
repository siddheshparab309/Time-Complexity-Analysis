# Asymptotic Analysis

## Project Overview

This project provides a practical analysis of a custom algorithm's time complexity. The goal is to demonstrate how a theoretical model of an algorithm's efficiency holds up when compared to real-world performance measurements.

---

## The Algorithm

The program analyzed is a nested-loop structure with the following logic:

```java
int j = 2;
while (j < n) {
    int k = 2;
    while (k < n) {
        Sum += a[k] * b[k];
        k = k * sqrt(k);
    }
    j = j + j/2;
}
```

---

## How It Works

This project validates a theoretical time complexity of **O(log n · log log n)** by running the algorithm and measuring its execution time for various input sizes. The experimental data is then plotted against the theoretical curve.

The graph shows that while initial runtimes are affected by environmental overhead, the overall trend of the experimental results aligns with the theoretical prediction as the input size `n` increases.

---

## Repository Contents

- `TimeComplexityAnalysis.java`: The Java code for the algorithm.
- `Graph.py`: The Python script used to plot the results.

---

## Getting Started

To replicate the analysis:

1. Clone this repository.
2. Compile and run the `TimeComplexityAnalysis.java` file to generate experimental data.
3. Use the `Graph.py` script with your data from the Java program’s output table to create the comparison graph.

