import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import datasets
iris = datasets.load_iris()
data = iris.data


def fun_denclude(data, eps=0.3, min_samples=10):
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(data)
    core_sample_mask = np.zeros_like(db.labels_, dtype=bool)
    core_sample_mask[db.core_sample_indices_] = True
    cluster_labels = iris.target
    unique_cluster_labels = set(cluster_labels)
    colors = ['green', 'red', 'blue', 'black', 'gray', '#ff00ff', '#ffff00']
    markers = ['o', '^', 'v', '*', 'x', 'h', 'd']
    for i, cluster in enumerate(unique_cluster_labels):
        cluster_index = (cluster_labels == cluster)
        core_samples = data[cluster_index & core_sample_mask]
        plt.scatter(core_samples[:, 0] + core_samples[:, 1], core_samples[:, 2] + core_samples[:, 3],c=colors[i],
                    marker=markers[i], s=80)
        noise_samples = data[cluster_index & ~core_sample_mask]
        plt.scatter(noise_samples[:, 0] + noise_samples[:, 1],noise_samples[:, 2] + noise_samples[:, 3], c=colors[i],
                    marker=markers[i], s=26)
    plt.show()


if __name__ == '__main__':
    fun_denclude(data, 10, 10)



