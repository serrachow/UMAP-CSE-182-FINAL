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
    parser_file.add_argument('input_dir', type=str, help='Path to the input .h5ad file')
    parser_file.add_argument('output_dir', type=str, help='Directory to save output files')
    parser_file.add_argument('-p', '--png_name', type=str, help='Optional UMAP plot png name')
    parser_file.add_argument('-c', '--csv_name', type=str, help='Optional UMAP results csv name')

    args = parser_file.parse_args()

    input_path = args.input_dir
    output_dir = args.output_dir
    png_name = 'UMAP_plot.png'
    csv_name = 'UMAP_results.csv'
    png_bool = False
    csv_bool = False

    if args.png_name:
        png_bool = True
        png_name = args.png_name
    if args.csv_name:
        csv_bool = True
        csv_name = args.csv_name


    print("Reading", input_path + " ...")
    print("Outputting", output_dir + " ...")
    adata = ad.read_h5ad(input_path)

    n_pcs = 50
    n_neighbors = 15
    min_dist = 0.1
    proceed = True

    while proceed:
        configurations_print(n_pcs, n_neighbors, min_dist, png_name, csv_name)
        input_config = input().split()
        if input_config[0] == "n_pcs":
            n_pcs = int(input_config[1])
        elif input_config[0] == "n_neighbors":
            n_neighbors = int(input_config[1])
        elif input_config[0] == "min_dist":
            min_dist = float(input_config[1])
        elif input_config[0] == "png_name":
            png_name = str(input_config[1])
        elif input_config[0] == "csv_name":
            csv_name = str(input_config[1])
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
    plot_umap(data_umap, output_dir, png_name)
    # print("UMAP plot saved to", output_dir + "/UMAP_plot.png")
    print("UMAP plot saved to", output_dir + "/" + png_name)

    print("Saving UMAP results to CSV...")
    # pd.DataFrame(data_umap, columns=['UMAP1', 'UMAP2']).to_csv(os.path.join(output_dir, 'umap_results.csv'), index=False)
    pd.DataFrame(data_umap, columns=['UMAP1', 'UMAP2']).to_csv(os.path.join(output_dir, csv_name), index=False)
    # print("UMAP results saved to", output_dir + "/UMAP_results.csv")
    print("UMAP results saved to", output_dir + "/" + csv_name)

def configurations_print(n_pcs, n_neighbors, min_dist, png_name, csv_name):
    print("*****")
    print("PCA Neighbors Configurations")
    print(f"Number of principal components to keep (int) [n_pcs]: {n_pcs}")
    print(f"Number of nearest neighbors to compute (int) [n_neighbors]: {n_neighbors}")
    print(f"Minimum distance between points in UMAP (float) [min_dist]: {min_dist}")
    print("PNG name (string) [png_name]:", png_name)
    print("CSV name (string) [csv_name]:", csv_name)
    print("*****")
    print("To configure, type ex: `n_pcs 45`.")
    print("If you want to proceed, type 'Done'.")

if __name__ == "__main__":
    main()
