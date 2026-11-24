
"""
Data preprocessing module.

This module contains reusable functions for:
- Handling missing values
- Encoding categorical variables
- Preparing data for Machine Learning
"""

import pandas as pd


def load_data(file_path):
    """
    Load a CSV dataset.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.
    """
    return pd.read_csv(file_path)
