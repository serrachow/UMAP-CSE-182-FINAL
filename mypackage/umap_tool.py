# mypackage/umap_tool.py

import sys
import argparse
from mypackage.functions import pca_neighbors, umap_transform, plot_umap
import anndata as ad
import os
import pandas as pd

def main():
    print("Uniform Manifold Approximation and Projection Tool Configurations...")
    parser_file = argparse.ArgumentParser()
    parser_file.add_argument('h5ad_file', metavar='h5ad_file', type=str, help='Path to the input .h5ad file')
    parser_file.add_argument('--output_dir', type=str, default='output', help='Directory to save output files')

    args = parser_file.parse_args()

    h5ad_file = args.h5ad_file
    output_dir = args.output_dir

    print("Reading", h5ad_file + "...")
    adata = ad.read_h5ad(h5ad_file)

    n_pcs = 50
    n_neighbors = 15
    proceed = True

    while proceed:
        configurations_print(n_pcs, n_neighbors)
        input_config = input().split()
        if input_config[0] == "n_pcs":
            n_pcs = int(input_config[1])
        elif input_config[0] == "n_neighbors":
            n_neighbors = int(input_config[1])
        elif input_config[0] == "Done":
            proceed = False

    print("Running PCA Neighbors...")
    data_pca, distances, indices = pca_neighbors(adata, n_pcs, n_neighbors)
    print("PCA Neighbors complete.")

    print("Running UMAP transformation...")
    data_umap = umap_transform(data_pca, n_neighbors)
    print("UMAP transformation complete.")

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    print("Plotting UMAP results...")
    plot_umap(data_umap, output_dir)
    print("UMAP plot saved to", output_dir + "/UMAP_plot.png")

    print("Saving UMAP results to CSV...")
    pd.DataFrame(data_umap, columns=['UMAP1', 'UMAP2']).to_csv(os.path.join(output_dir, 'umap_results.csv'), index=False)
    print("UMAP results saved to", output_dir + "/umap_results.csv")

def configurations_print(n_pcs, n_neighbors):
    print("*****")
    print("PCA Neighbors Configurations")
    print(f"Number of principal components to keep (int) [n_pcs]: {n_pcs}")
    print(f"Number of nearest neighbors to compute (int) [n_neighbors]: {n_neighbors}")
    print("*****")
    print("To configure, type ex: `n_pcs 45`.")
    print("If you want to proceed, type 'Done'.")

if __name__ == "__main__":
    main()
