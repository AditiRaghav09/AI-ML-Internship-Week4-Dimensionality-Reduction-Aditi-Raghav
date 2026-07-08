# Dimensionality Reduction Techniques using PCA and t-SNE

## Overview

This project was completed as part of the AI/ML Internship Week 4 Task 3.

The objective of this project is to explore dimensionality reduction techniques using the Iris dataset. Principal Component Analysis (PCA) and t-Distributed Stochastic Neighbor Embedding (t-SNE) were implemented to reduce the dataset dimensions and compare their performance.

---

## Dataset

- **Dataset:** Iris Dataset
- **Samples:** 150
- **Features:** 4
- **Classes:** 3

---

## Project Workflow

The following steps were completed:

- Load the Iris dataset
- Perform Exploratory Data Analysis (EDA)
- Standardize the data
- Apply Principal Component Analysis (PCA)
- Apply t-SNE
- Visualize the reduced data
- Compare PCA and t-SNE
- Train a Logistic Regression classifier
- Compare classification performance
- Summarize the results

---

## Techniques Used

- Principal Component Analysis (PCA)
- t-Distributed Stochastic Neighbor Embedding (t-SNE)
- Logistic Regression

---

## Project Structure

```
AI-ML-Internship-Week4-Dimensionality-Reduction-Aditi-Raghav
│
├── notebooks/
│   └── dimensionality_reduction.ipynb
│
├── assets/
│   └── plots/
│       ├── pca_plot.png
│       └── tsne_plot.png
│
├── docs/
│   └── comparative_report.md
│
├── src/
│   ├── pca_reduction.py
│   └── tsne_visualization.py
│
├── requirements.txt
│
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Key Findings

- PCA successfully reduced the dataset while preserving most of the important information.
- t-SNE produced clear visualization of the different Iris species.
- Logistic Regression achieved high accuracy on the original and PCA-reduced datasets.
- PCA is useful for feature reduction, while t-SNE is mainly used for data visualization.

---

## Conclusion

This project demonstrates the implementation and comparison of PCA and t-SNE for dimensionality reduction. Both techniques help simplify high-dimensional data, but they are used for different purposes. PCA is suitable for feature reduction before machine learning, whereas t-SNE is mainly used for visualization.
