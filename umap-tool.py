import sys
import argparse
from functions import pca_neighbors
from functions import plot_pca_neighbors
import anndata as ad
import scanpy as sc

def main():
    print("Uniform Manifold Approximation and Projection Tool Configurations...")
    parser_file = argparse.ArgumentParser()
    parser_file.add_argument('h5ad_file', metavar='h5ad_file', type=str)

    args = parser_file.parse_args()

    h5ad_file = args.h5ad_file

    print("Reading", h5ad_file + "...")
    adata = sc.read_h5ad(h5ad_file)

    n_pcs = 50
    n_neighbors = 15
    proceed = True

    while(proceed):
        configurations_print(n_pcs, n_neighbors)
        input_config = input().split()
        if (input_config[0] == "n_pcs"):
            n_pcs = input_config[1]
        elif (input_config[0] == "n_neighbors"):
            n_neighbors = input_config[1]
        elif (input_config[0] == "Done"):
            proceed = False

    print("Running PCA Neighbors...")
    data_pca, distances, indices = pca_neighbors(adata, n_pcs, n_neighbors)
    print("Plotting PCA Neighbors...")
    plot_pca_neighbors(data_pca, indices)


def configurations_print(n_pcs, n_neighbors):
    print("*****")
    print("PCA Neighbors Configurations")
    print("Number of principal components to keep (int) [n_pcs]", n_pcs)
    print("Number of nearest neighbors to compute (int) [n_neighbors]", n_neighbors)
    print("*****")
    print("To configure, type ex: `n_pcs 45`.")
    print("If you want to proceed, type 'Done'.")


if __name__ == "__main__":
    main()