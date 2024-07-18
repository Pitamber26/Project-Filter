import pandas as pd
import numpy as np

def item_check(df_column, inputs):
    """
    Checks if all unique inputs are present in the specified DataFrame column.
    If yes, executes the fetch function; otherwise, returns an error message.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The column to check against.
        inputs (list): List of user-provided inputs.

    Returns:
        str: Either the result of the fetch function or an error message.
    """
    unique_inputs = set(inputs)
    unique_column_values = set(df_column.unique())
    
    if unique_inputs.issubset(unique_column_values):
        return 1
    else:
        return 0


