# Minimum Cost Network

## Search and Problem Solving
Finding optimal graph structures is a significant optimization problem with applications in various fields, including machine learning, such as Bayesian Network Learning. This repo focuses on the vertex ordering problem, a simplified version of Bayes-Net Learning.

Given a set of vertices, the goal is to determine a vertex ordering with the minimum cost. For instance, an ordering (B, C, A) might represent a network with vertices B, C, and A.

### Problem Description
We are provided with vertices \(V1, \ldots, Vn\) and possible parent sets for each vertex, each with an associated cost. An ordering \(O\) of the vertices is considered consistent if all parents come before the vertex in the ordering. The task is to find an ordering \(O\) that minimizes the total cost of the network.

The objective is to implement and experiment with the search algorithms discussed in class (BFS, DFS, UCS) to find a good ordering of the variables. Three datasets are provided for experimentation in addition to two simple examples.

### Example
Consider vertices A, B, and C with possible parent sets and their associated costs. For instance:
- The cost of ordering (B, C, A) might be \( \text{cost}(C \rightarrow \{B\}) + \text{cost}(A \rightarrow \{B, C\}) = 2.4 + 6.3 + 1.3 = 10 \).
- The cost of ordering (A, B, C) might be \( \text{cost}(C \rightarrow \{B\}) + \text{cost}(B \rightarrow \{\}) = 7.5 + 6.3 + 2.4 = 16.2 \).

We are going to implement search algorithms to determine the minimum cost ordering and its cost.

## Implementation Tasks
This repository contains the following implementation tasks:

- Implementation of search algorithms (BFS, DFS, UCS) in Python to find the minimum cost ordering and its associated cost.
- Experimentation with various datasets to analyze the results.