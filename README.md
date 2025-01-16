# Customer Clustering & Prediction  

This repository provides an end-to-end solution for **customer clustering** and predictive modeling, leveraging a segmentation dataset. The workflow covers preprocessing, exploratory data analysis, clustering, and model training for better customer insights.  

---  

## Project Overview  

Businesses often need to understand their customers better to optimize strategies and improve customer satisfaction. This project uses customer demographic and transactional data to:  
1. **Segment customers into clusters** for personalized strategies.  
2. **Build predictive models** to classify customers into these clusters.  

---  

## Dataset Overview  

The dataset contains customer information, including demographics and income-related features.  

### **Key Features:**  
- **Age**: Customer's age.  
- **Income**: Customer's annual income.  
- **Sex**: Customer's gender (Male/Female).  
- **Marital Status**: Marital status (Single/Married).  
- **Education**: Education level.  
- **Occupation**: Type of occupation.  
- **Settlement Size**: Size of the area where the customer resides.  

---  

## Project Workflow  

### **1. Exploratory Data Analysis (EDA)**  
- Visualize distributions of numerical and categorical features.  
- Analyze relationships between features (e.g., correlation, scatterplots).  

### **2. Data Preprocessing**  
- Handle missing or redundant values.  
- Scale numerical features using Min-Max Scaling.  
- Encode categorical variables for model compatibility.  

### **3. Clustering**  
- **Elbow Method**: Determine the optimal number of clusters based on inertia.  
- **Silhouette Score**: Validate clustering quality.  
- Use **K-Means Clustering** to segment customers into 6 distinct clusters.  

### **4. Dimensionality Reduction**  
- Apply **PCA** to reduce feature dimensions from 7 to 3 for visualization.  

### **5. Visualization**  
- Create 3D scatter plots to visualize cluster distributions.  

### **6. Predictive Modeling**  
- Build a **Decision Tree Classifier** to predict cluster membership based on input features.  
- Evaluate model performance using metrics like accuracy and classification reports.  

---  

