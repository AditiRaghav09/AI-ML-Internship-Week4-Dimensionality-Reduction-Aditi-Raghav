# Comparative Report: PCA vs t-SNE

## Project Overview

This project demonstrates two popular dimensionality reduction techniques, Principal Component Analysis (PCA) and t-Distributed Stochastic Neighbor Embedding (t-SNE), using the Iris dataset.

The objective was to reduce the dataset from four dimensions to two dimensions and compare the performance of both techniques.

---

## Dataset

- **Dataset:** Iris Dataset
- **Number of Samples:** 150
- **Number of Features:** 4
- **Number of Classes:** 3

---

## PCA (Principal Component Analysis)

- Reduced the dataset from 4 features to 2 principal components.
- Preserved most of the important information in the dataset.
- Helped reduce dimensionality while maintaining high classification accuracy.

---

## t-SNE (t-Distributed Stochastic Neighbor Embedding)

- Reduced the dataset to 2 dimensions for visualization.
- Produced well-separated clusters of the three Iris species.
- Mainly used for visualization rather than model training.

---

## Comparison

| Feature | PCA | t-SNE |
|---------|-----|--------|
| Technique | Linear | Non-linear |
| Purpose | Feature Reduction | Data Visualization |
| Speed | Faster | Slower |
| Classification | Suitable | Not Recommended |
| Visualization | Good | Excellent |

---

## Results

- PCA reduced the dimensions while preserving most of the dataset information.
- t-SNE produced clearer visual separation between the different Iris species.
- Logistic Regression achieved high accuracy on both the original and PCA-reduced datasets.

---

## Conclusion

Both PCA and t-SNE are useful dimensionality reduction techniques.

- PCA is suitable for reducing features before machine learning.
- t-SNE is better for visualizing high-dimensional data and understanding cluster patterns.
