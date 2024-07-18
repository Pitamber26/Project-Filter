import pandas as pd
import numpy as np

def inputdata(imp_features):
    """ returns a dictionary having keys as important features and values as list of all the inputs we want to check in the feature

    params:
    imp_features : this is the list of important features we want to input as keys of dictionary 
    """
    y =  dict.fromkeys(imp_features, [])
    for x in imp_features:
        values = input(f'Enter {x} separated by " , "').split(" , ")
        y[x] = values

    return y