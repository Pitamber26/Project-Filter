import pandas as pd
import numpy as np

def find_projects_by_input(df,column,inputs):
    """
    Find project names that have all the given material values.

    Parameters:
    df (pd.DataFrame): DataFrame with columns 'Name' and 'Device Description'.
    inputs (list): List of inputs to search for.
    column : name of the column in which the inputs are present

    Returns:
    list: List of project names that have all the given input values.
    """
    filtered_df = df[df[column].isin(inputs)]
    grouped = filtered_df.groupby('Name')[column].apply(set).reset_index()
    required_materials = set(inputs)
    result = grouped[grouped[column].apply(lambda x: required_materials.issubset(x))]
    return result['Name'].tolist()
    
    