Sequential Clustering

This project implements a custom clustering algorithm that groups multidimensional data points using sequential proximity links and distance-based cutting to form `K` clusters.

Overview

Given a CSV file containing `N` data points in a multidimensional space, the algorithm builds a single chain of connections between points based on nearest-neighbor distance, then removes the `K-1` longest connections to separate the data into `K` clusters.

This method is similar to a greedy variant of hierarchical clustering with linkage pruning.

Input Format

Each line in the CSV input file contains comma-separated floating point values representing one point. The index (line number) of the point is its unique identifier (starting from 1).

**Example:**
```csv
1.0,2.0
3.0,4.0
5.0,6.0
```

The output file is also a CSV file. Each line contains the identifiers of the points in a cluster, separated by commas.

Example (K = 2):
```csv
1, 2
3
```

Running the Program

   Place the .csv input file in the project directory.

   Run the program:
        python main.py

