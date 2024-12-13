import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

np.random.seed(42)
X=np.random.randn(200,2)*0.5


kmeans=KMeans(n_clusters=3,random_state=0).fit(X)

y_kmeans=kmeans.predict(X)

plt.scatter(X[:,0],X[:,1],c=y_kmeans,s=50, cmap="viridis")

centers=kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c="black",s=200,alpha=0.5)
plt.show()