import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import pickle

# 1️⃣ Load dataset
df = pd.read_csv("data/Mall_Customers.csv")

# 2️⃣ Select features
X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

# 3️⃣ Train KMeans model
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)

# 4️⃣ Evaluate clustering
score = silhouette_score(X, kmeans.labels_)
print("Silhouette Score:", score)

# 5️⃣ Save trained model
pickle.dump(kmeans, open("model/kmeans_model.pkl", "wb"))
print("Model saved successfully!")

# 6️⃣ Get centroids
centroids = kmeans.cluster_centers_

# 7️⃣ Visualization
plt.figure(figsize=(8,6))

plt.scatter(
    X["Annual Income (k$)"],
    X["Spending Score (1-100)"],
    c=kmeans.labels_,
    cmap="viridis",
    s=60
)

# plot cluster centers
plt.scatter(
    centroids[:,0],
    centroids[:,1],
    c="red",
    s=200,
    marker="X",
    label="Centroids"
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using KMeans")
plt.legend()

# 8️⃣ Save graph
plt.savefig("cluster_visualization.png")
print("Visualization saved as cluster_visualization.png")