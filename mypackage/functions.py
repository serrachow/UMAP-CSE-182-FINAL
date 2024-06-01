# mypackage/functions.py

import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import umap
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

def umap_transform(data_pca, n_neighbors=15, min_dist=0.1):
    """
    Perform UMAP dimensionality reduction on PCA-transformed data.
    
    Parameters:
    - data_pca: PCA-transformed data.
    - n_neighbors: Number of neighbors used in UMAP.
    - min_dist: Minimum distance between points in UMAP.
    
    Returns:
    - data_umap: UMAP-transformed data.
    """
    reducer = umap.UMAP(n_neighbors=n_neighbors, min_dist=min_dist)
    data_umap = reducer.fit_transform(data_pca)
    return data_umap

def plot_umap(data_umap, output_dir):
    """
    Plot UMAP results and save the plot.
    
    Parameters:
    - data_umap: UMAP-transformed data.
    - output_dir: Directory to save the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data_umap[:, 0], data_umap[:, 1], c='blue', label='Cells')
    plt.xlabel('UMAP Component 1')
    plt.ylabel('UMAP Component 2')
    plt.title('UMAP of Cells')
    plt.legend()
    plt.savefig(f"{output_dir}/UMAP_plot.png")
    plt.close()
