# setup.py

from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'matplotlib',
        'anndata',
        'umap-learn',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'umap-tool=mypackage.umap_tool:main',
        ],
    },
    author='Ignatius Jenie, Jiyuan Zhu, Serena Chuang',
    author_email='ijenie@ucsd.edu',
    description='A package for performing PCA and UMAP on single-cell RNA-seq data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/serrachow/UMAP-TOOL-CSE-182-FINAL',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
