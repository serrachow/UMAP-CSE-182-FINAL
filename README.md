
# UMAP Tool

For **UC San Diego CSE 185 Spring 2024**

by Ignatius Jenie, Jiyuan Zhu, Serena Chuang

## Description

This package performs PCA and UMAP dimensionality reduction on single-cell RNA-seq data stored in `.h5ad` files and saves the results to a specified directory.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/serrachow/UMAP-TOOL-CSE-182-FINAL.git
   cd UMAP-TOOL-CSE-182-FINAL
   ```

2. Install the package:
   ```bash
   python setup.py install --user
   ```

3. Add to path: replace <user> with your username
   ```bash
   export PATH=$PATH:/home/<user>/.local/bin
   ```

4. Install requirements:
   ```bash
   pip install --user -r requirements.txt
   ```


## Usage

To use the tool, run the following command:
```bash
umap-tool --output_dir <output directory> <.h5ad file>
```

Install example data from [Data File 2](https://drive.google.com/file/d/1BzPd3DBIzZa3T0PpaU236cautzjMbC7i/view?usp=sharing):
```bash
curl -L -o 500_genes.h5ad 'https://drive.google.com/uc?export=download&id=1BzPd3DBIzZa3T0PpaU236cautzjMbC7i'
```

You will be prompted to configure the number of principal components and nearest neighbors interactively.

## Example

```bash
umap-tool --output_dir ./out 500_genes.h5ad
```

This command will process the input `.h5ad` file, perform PCA and UMAP transformations, and save the results (both plot and CSV) in the specified output directory.

## Data

The data used for this tool was generated using the `preprocess.ipynb` notebook or can be downloaded directly from the following links:
- [Data File 1](https://drive.google.com/file/d/18H1GYi7swykG-7rd3bKtUUP_e7EZJBTO/view?usp=sharing)
- [Data File 2](https://drive.google.com/file/d/1BzPd3DBIzZa3T0PpaU236cautzjMbC7i/view?usp=sharing)

## Repository Structure
- `mypackage/`: Contains the package modules.
   - `__init__.py`: Initializes the package.
   - `functions.py`: Contains helper functions for data processing and visualization.
   - `umap_tool.py`: Script for running the tool from the command line.
- `setup.py`: Script for setting up the package.
- `README.md`: Project documentation.
- `requirements.txt`: Required libraries.

## Contributors

This project was developed by Ignatius Jenie (A16923484), Serena Chuang (A17302920), Jiyuan Zhu (A16636193). The dataset is sourced from the NeurIPS 2021 Multimodal Single-Cell Data Integration benchmarking dataset.

For any corrections or suggestions:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
