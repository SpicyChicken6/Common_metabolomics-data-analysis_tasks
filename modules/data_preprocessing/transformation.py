import numpy as np
import pandas as pd

def data_transformation_log(input_data):
    '''
    Transform the data by taking the log10 of each value

    Args:
        input_data (pandas.DataFrame): Dataframe containing the data

    Returns:
        pandas.DataFrame: Transformed dataframe
    '''

    data_to_process=input_data.iloc[:,2:]
    data_log10 = data_to_process.apply(np.log10)
    transformed_data=input_data.copy
    transformed_data.iloc[:,2:]=data_log10
    
    return transformed_data