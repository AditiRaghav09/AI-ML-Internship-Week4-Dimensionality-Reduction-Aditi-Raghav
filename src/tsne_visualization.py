# t-SNE Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Apply t-SNE
tsne = TSNE(
    n_components=2,
    random_state=42,
    perplexity=30,
    learning_rate=200
)

X_tsne = tsne.fit_transform(X_scaled)

# Create DataFrame
tsne_df = pd.DataFrame(X_tsne, columns=["Dimension 1", "Dimension 2"])
tsne_df["Species"] = iris.target

# Plot
plt.figure(figsize=(8,6))

sns.scatterplot(
    data=tsne_df,
    x="Dimension 1",
    y="Dimension 2",
    hue="Species",
    palette="viridis",
    s=80
)

plt.title("t-SNE Visualization of Iris Dataset")

plt.show()
