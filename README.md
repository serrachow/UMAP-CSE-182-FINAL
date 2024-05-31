# UMAP-CSE-182-FINAL

for **UC San Diego CSE 185 Spring 2024**

by Ignatius Jenie, Jiyuan Zhu, Serena Chuang

# UMAP Tool

## Public Dataset

The dataset included is from Open Problems' **NeurIPS 2021: Multimodal Single-Cell Data Integration** benchmarking dataset, which is collected from bone marrow mononuclear cells of 12 healthy human donors. This dataset offers a comprehensive set of cellular populations, making it ideal for showcasing the detailed and nuanced visualization capabilities of our custom UMAP tool.

## Getting Started
### Prerequisites
Ensure you have Python installed. Required libraries can be found in `requirements.txt`.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/serrachow/UMAP-TOOL-CSE-182-FINAL.git
   cd UMAP-TOOL-CSE-182-FINAL
   ```
 2. Install necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
### Running the UMAP Tool
To run the UMAP Tool, use the following command:
```bash
python umap-tool.py <dataset>
```
### Preprocessing Data
The preprocessing steps are detailed in the Jupyter Notebook:
```bash
jupyter notebook preprocess.ipynb
```
### Using Helper Functions
Functions for data processing and visualization are stored in functions.py. You can import and use them in your scripts as follows:
```bash
from functions import your_function_name

# Example usage
your_function_name(arguments)
```

## Repository Structure
- `functions.py`: Contains helper functions for data processing and visualization.
- `preprocess.ipynb`: Jupyter Notebook for data preprocessing steps.
- `umap-tool.py`: Main script to run the UMAP visualization.
- `README.md`: Project documentation.

## Contributors
This project was developed by Ignatius Jenie (A16923484), Serena Chuang (A17302920), Jiyuan Zhu (A16636193)

For any corrections or suggestions:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.



