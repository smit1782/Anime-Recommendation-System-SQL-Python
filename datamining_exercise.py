# -*- coding: utf-8 -*-
"""Datamining Exercise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18BsvmwMMOoLN8Qv_ZkjY96yqnSIzmk4V

Import the Datamining CSV file:
"""

from google.colab import files
uploaded = files.upload()

"""Datamining exercise for UserInfo:"""

# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("Datamining.csv")

# Examine first few rows:
df.head()

"""Data Pre-processing"""

# Drop any rows with missing values:
df = df.dropna()

# Convert the 'gender' column to a categorical variable:
df['gender'] = pd.Categorical(df['gender'])

"""Gender Frequency Analysis"""

# Calculate the frequency of each gender in the dataset:
gender_counts = df['gender'].value_counts()

# Plot the frequency of each gender using a bar chart:
sns.barplot(x = gender_counts.index, y = gender_counts.values)
plt.title('Gender Frequency Analysis')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.show()

"""Clustering data with K-Means"""

'''
This code performs k-means clustering on our dataset, based on the gender attribute. 
The scatter plot that we display shows the distribution of scores and shows for each gender, with Male 
data points represented in red, Female data points in blue, and Non-Binary data points in green. 
We also show the centroids for each cluster.
'''

# Prepare Data

'''
We need to extract the data for each gender separately and create a dictionary, so 
we can map the color for each gender. We also need to select the attributes we
want to use for clustering (animeID and score) and normalize the data using 
MinMaxScaler.
'''

# Create dictionary to map color for each gender
colors = {"Male":"red", "Female":"blue", "Non-Binary":"green"}

# Select attributes for clustering and data normalization
X = df.loc[:,["animeID", "score"]]
X = (X - X.min()) / (X.max() - X.min())

"""Perform Clustering"""

'''
We can now use K-Means algorithm for clustering. 
We will set the number of clusters to 3 (male, Female, and Non-Binary
as explanied before).
'''

# Perform clustering
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

"""Plot Results (Numerical and Categorical Data)"""

'''
Finally, we can plot the results using matplotlib. We will create a scatter plot for each gender 
and assign the corresponding color.'
'''

# Create scatter plot for each gender
for i in range(len(colors)):
    plt.scatter(X.iloc[labels == i, 0], X.iloc[labels == i, 1], color=colors[list(colors.keys())[i]])

# Plot centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", color="black", s=200)

# Add axis labels and title
plt.xlabel("Anime Show (by ID)")
plt.ylabel("Score")
plt.title("K-Means Clustering by Gender")

# Set background color
ax = plt.gca()
ax.set_facecolor("#424141")

# Show plot
plt.show()

"""Correlation Heatmap Analysis"""

'''
We want to see if there are any patterns to how the rating of a show and the users' gender when it comes to a shows score.
'''
rsg = df.groupby(['rating','score','gender'])

rsg.head()

# Correlation matrix of our main dataframe:
df.corr()

# Basic Correlation Heatmap based on our dataframe:

sns.heatmap(df.corr(), cmap="plasma")

"""Heatmap Settings"""

'''
Let's look at the overall data in a more detailed way.
By cutting it in half along the diagonal, we won't lose information.
'''

plt.figure(figsize=(18, 8))
# We define the mask to set the values in the upper triangle to 'True':
customMask = np.triu(np.ones_like(df.corr(), dtype=np.bool))
heatmap = sns.heatmap(df.corr(), mask = customMask, vmin=-1, vmax=1, annot=True, cmap='mako')
heatmap.set_title('animedb', fontdict={'fontsize':24}, pad=14);

"""Strength of the correlation between every independent variable in our database and the score."""

'''
We show the correlation of all features by ‘score’, sorted in a descending order.
'''
df.corr()[['score']].sort_values(by = 'score', ascending=False)

# Heatmap with the final results:

plt.figure(figsize=(8, 12))
map = sns.heatmap(df.corr()[['score']].sort_values(by='score', ascending=False), 
                                                 vmin=-1, vmax=1, annot=True, cmap='vlag')

map.set_title('Features Correlation with User Score', fontdict={'fontsize':24}, pad=15);