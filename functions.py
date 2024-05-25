# functions.py

import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import anndata

def pca_neighbors(adata: anndata.AnnData, n_pcs: int = 50, n_neighbors: int = 15):
    """
    Perform PCA and compute nearest neighbors on an AnnData object.
    
    Parameters:
    - adata: AnnData object with cells as rows and genes as columns.
    - n_pcs: Number of principal components to keep.
    - n_neighbors: Number of nearest neighbors to compute.
    
    Returns:
    - data_pca: PCA-transformed data.
    - distances: Distances to nearest neighbors.
    - indices: Indices of nearest neighbors.
    """
    # Ensure data is in the right format
    data = adata.X if isinstance(adata.X, np.ndarray) else adata.X.toarray()
    
    # Perform PCA
    pca = PCA(n_components=n_pcs)
    data_pca = pca.fit_transform(data)
    
    # Compute Nearest Neighbors
    neighbors = NearestNeighbors(n_neighbors=n_neighbors)
    neighbors.fit(data_pca)
    distances, indices = neighbors.kneighbors(data_pca)
    
    return data_pca, distances, indices

def plot_pca_neighbors(data_pca, indices):
    """
    Plot PCA results and nearest neighbors.
    
    Parameters:
    - data_pca: PCA-transformed data.
    - indices: Indices of nearest neighbors.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data_pca[:, 0], data_pca[:, 1], c='blue', label='Cells')
    
    # Plot the neighbors
    for i in range(data_pca.shape[0]):
        for j in indices[i]:
            plt.plot([data_pca[i, 0], data_pca[j, 0]], [data_pca[i, 1], data_pca[j, 1]], 'k-', alpha=0.2)
    
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.title('PCA of Cells with Nearest Neighbors')
    plt.legend()
    plt.savefig("PCA_plot.png")
    plt.show()
