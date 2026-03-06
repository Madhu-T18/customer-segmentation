
--
# Customer Segmentation using Machine Learning

## 1 Introduction

Customer segmentation is a process of dividing customers into groups based on similar characteristics. Businesses use segmentation to target specific groups of customers for marketing and product recommendations.

This project applies machine learning techniques to identify customer segments using income and spending behavior.

---

## 2 Problem Statement

Businesses often struggle to understand different types of customers. Without segmentation, marketing campaigns may be inefficient.

The objective of this project is to use machine learning to group customers into meaningful clusters.

---

## 3 Dataset

The dataset used is the Mall Customers dataset.

Features available:

- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

For clustering analysis, the following features were selected:

- Annual Income
- Spending Score

---

## 4 Methodology

Steps followed in this project:

1. Data collection
2. Data preprocessing
3. Feature selection
4. Model training using K-Means
5. Model evaluation using silhouette score
6. Visualization of clusters
7. Deployment using Flask

---

## 5 Machine Learning Model

Algorithm used: **K-Means Clustering**

K-Means works by:

1. Selecting number of clusters
2. Assigning data points to nearest cluster center
3. Updating cluster centroids
4. Repeating until convergence

The model identified **5 clusters** in the dataset.

---

## 6 Model Evaluation

The model was evaluated using **Silhouette Score**.

Result:

Silhouette Score = **0.55**

This indicates that the clusters are reasonably well separated.

---

## 7 Visualization

Clusters were visualized using scatter plots showing:

- X-axis: Annual Income
- Y-axis: Spending Score
- Different colors represent different customer groups
- Cluster centers highlighted

---

## 8 Deployment

The trained model was deployed using Flask web framework.

Users can input:

- Annual Income
- Spending Score

The system predicts the customer segment.

---

## 9 Applications

Customer segmentation can be used for:

- Targeted marketing
- Personalized recommendations
- Customer relationship management
- Business strategy planning

---

## 10 Conclusion

This project successfully applied machine learning techniques to segment customers based on income and spending patterns. The model achieved a silhouette score of 0.55 and was deployed using a web interface for real-time predictions.