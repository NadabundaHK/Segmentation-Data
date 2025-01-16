# -*- coding: utf-8 -*-
"""CP 2-clustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BIJsASxHGc55jUEsheIHZ83fcVZKQlgb
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn import model_selection
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score, precision_score, recall_score, fbeta_score
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.datasets import load_breast_cancer

customer_info = pd.read_csv('/content/segmentation data.csv')
customer_info.head()

customer_info.info()

customer_info.describe()

customer_info = customer_info.drop(['ID'], axis = 1)
customer_info

num_col = ['Age', 'Income']
cat_col = ['Sex', 'Marital status', 'Education', 'Occupation', 'Settlement size']

df = customer_info.copy()

df[cat_col] = df[cat_col].astype('str')

df.info()

"""## Distribusi Variabel Numerik"""

for num in num_col:
  plt.figure(figsize=(6,3))
  sns.histplot(data = customer_info, x = num)

"""## Distrbusi Variabel Kategorikal"""

for cat in cat_col:
  plt.figure(figsize=(4,2))
  sns.countplot(data = customer_info, x = cat)

"""## Analisis Bivariat (antar 2 variabel)

# 1. Antar variabel numerik
"""

sns.scatterplot(x = 'Age', y = 'Income', data = customer_info)

import scipy.stats as stats

stats.pearsonr(customer_info['Age'], customer_info['Income']) # menghitung korelasi antar2 variabel numerik

sns.lmplot(x = 'Age', y = 'Income', data = customer_info)

"""# 2. Antar kolom kategorikal dan nominal"""

for cat in cat_col:
  for num in num_col:
    plt.figure(figsize = (4,2))
    sns.kdeplot(data = customer_info, x = num, hue=cat)

"""# 3. antar kolom kategorikal"""

cat_aux = cat_col.copy()  # Salin daftar kolom kategori
for category1 in cat_col:
    cat_aux.pop(0)  # Hapus elemen pertama dari daftar salinan
    for category2 in cat_aux:
        if category1 != category2:  # Pastikan pasangan kategori tidak sama
            plt.figure(figsize=(4, 2))  # Atur ukuran figure
            sns.countplot(data=customer_info, x=category1, hue=category2)

"""## Analisis Multivariat"""

def bivariate_scatter(x, y, hue, df):
    plt.figure(figsize=(6, 6))
    sns.scatterplot(x=x, y=y, data=df, hue=hue, alpha=0.85)

for cat in cat_col:
  bivariate_scatter('Age', 'Income', cat, customer_info)

"""## Scalling"""

df

df = customer_info.copy()
df.info()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X = scaler.fit_transform(df)

X

X.describe()

"""## Clustering

#1. menentukan jumlah cluster yang optimal dengan metode elbow
"""

# elbow method, untuk mencari berapa banyak cluster yang akan digunakan untuk membagi datase
from sklearn.cluster import KMeans

cluster_range = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
inertia = []

for c in cluster_range:
    kmeans = KMeans(n_clusters=c, random_state=42).fit(X)  # training clustering with KMeans
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(7, 7))
plt.plot(cluster_range, inertia, marker='o')

"""Dari metode elbow diatas, kita akan membagi customer ke dalam cluster 5 atau 6 kelompok

#2. menentukan banyaknya cluster dengan metode Shillouette score
"""

from sklearn.metrics import silhouette_samples, silhouette_score

clusters_range = range(2, 11)
random_range = range(0, 19)
results = []

for c in clusters_range:
    for r in random_range:
        clusterer = KMeans(n_clusters = c, random_state = r)
        cluster_labels = clusterer.fit_predict(X)
        silhouette_avg = silhouette_score(X, cluster_labels)
        results.append([c, r, silhouette_avg])

result = pd.DataFrame(results, columns=["n_clusters", "seed", "silhouette_score"])
pivot_km = pd.pivot_table(result, index="n_clusters", columns="seed", values="silhouette_score")

plt.figure(figsize=(15, 6))
sns.heatmap(pivot_km, annot=True, linewidths=.5, fmt=".3f", cmap=sns.cm.rocket_r)
plt.tight_layout()

"""Dari hasil elnow method dan silhoutte score, kita putuskan akan membagi dataset customers ke dalam 6 kelompok/cluster

## Jalankan algoritma clustering untuk membagi dataset ke dalam 6 kelompok
"""

pd.DataFrame(X, columns=df.columns)

#pengurangan dimensi dataset training kita, dari 7 dimensi menjadi 3 dimensi menggunakan algoritma PCA (Principal Component Analysis)

from sklearn.decomposition import PCA

pca = PCA (n_components=3, random_state=42)
X_pca = pca.fit_transform(X)
X_pca_df = pd.DataFrame(data=X_pca, columns = ['X1', 'X2', 'X3'])
X_pca_df

# Jalankan algoritma clustering KMeans untuk dataset kita yg sudah dijadikan 3 dimensi

kmeans = KMeans(n_clusters=6, random_state=0).fit(X)
labels = kmeans.labels_
X_pca_df['Labels'] = labels
X_pca_df['Labels'] = X_pca_df['Labels'].astype(str)

X_pca_df

X_pca_df['Labels'].value_counts()

"""## 8. Visualisasi hasil Clustering"""

import plotly.express as px

fig = px.scatter_3d(X_pca_df, x = 'X1', y ='X2', z = 'X3',
                    color=X_pca_df['Labels'])
fig.show()

results_df=customer_info.copy()
results_df['Labels'] = kmeans.labels_
results_df

summary = {}  # Inisialisasi list kosong

for index in range(6):
    # Gunakan append untuk menambahkan hasil ke dalam list
    summary[index] = results_df[results_df['Labels'] == index].describe().T

summary[5]

summary[1]

results_df

"""## 9. Manfaatkan dataset hasil clustering untuk membangun model prediksi"""

from sklearn import tree
import graphviz

clf = DecisionTreeClassifier(max_depth = 4, min_samples_leaf = 5)
X_clusters = results_df.drop('Labels', axis =1)
y_clusters = results_df['Labels']

clf.fit(X_clusters, y_clusters) # Training untuk DecisionTres Classifier

predictions = clf.predict(X_clusters)
print(classification_report(y_clusters, predictions))

dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=results_df.columns[:7],
                                class_names=['Cluster 0', 'Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5'],
                                filled=True)

# Draw graph
graph = graphviz.Source(dot_data, format="png")
graph

!jupyter nbconvert --to html /content/CP_2_clustering.ipynb