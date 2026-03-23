# Customer Segmentation using K-Means Clustering

## Project Overview
This project uses Machine Learning to segment customers based on their **Annual Income** and **Spending Score**.  
Customer segmentation helps businesses understand different types of customers and create targeted marketing strategies.

The project implements **K-Means Clustering** and deploys the model using **Flask** to allow users to input new customer data and get predictions.

---
## Project Structure
customer_segmentation
│
├── app.py
├── train_model.py
│
├── model
│ └── kmeans_model.pkl
│
├── templates
│ └── index.html
│
├── data
│ └── Mall_Customers.csv
│
└── cluster_visualization.png
---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Flask
- HTML & CSS

---

## Dataset

The dataset used is **Mall Customers Dataset** containing:

- Customer ID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1–100)

For clustering, the following features were used:

- Annual Income
- Spending Score

---

## Machine Learning Model

Algorithm used:

**K-Means Clustering**

Number of clusters:

**5 customer segments**

Model evaluation metric:

**Silhouette Score = 0.55**

---

## Customer Segments

| Cluster | Customer Type |
|-------|---------------|
| 0 | Budget Customers |
| 1 | Young High Spenders |
| 2 | Regular Customers |
| 3 | Careful High Income Customers |
| 4 | Luxury Shoppers |

---



# Installation & Usage

## 1 Clone the Repository

```bash
git clone https://github.com/yourusername/customer-segmentation-ml.git

### 2 Go to the Project Directory
cd customer-segmentation-ml

###3 Install Required Libraries
pip install pandas scikit-learn flask matplotlib

Or if using requirements.txt:

pip install -r requirements.txt
### 4 Train the Machine Learning Model

Run the training script:

python train_model.py

This will:

Train the K-Means clustering model

Calculate the Silhouette Score

Save the trained model

Generate the cluster visualization graph

###5 Run the Flask Web Application
Start the web server:
python app.py

###6 Open the Application
Open your browser and visit:
http://127.0.0.1:5000

###7 Use the Application
Enter Annual Income
Enter Spending Score
Click Predict
The application will display the customer segment.

Example Input
Annual Income	Spending Score
70	80

Example Output:
Customer Type: Luxury Shopper

Features
Customer segmentation using K-Means clustering
Visualization of clusters
Web interface for prediction
Model saved using Pickle
Interactive input system"# CUSTOMER-SEGEMENTATION-ML-PROJEC" 
