
"""
Prediction module.

Responsible for loading the trained model
and generating loan approval predictions.
"""

import joblib


def load_model(model_path):
    """
    Load a trained Machine Learning model.

    Parameters
    ----------
    model_path : str
        Path to the saved model.

    Returns
    -------
    object
        Loaded model.
    """
    return joblib.load(model_path)
