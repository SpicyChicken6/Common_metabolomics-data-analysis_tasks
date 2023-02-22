import pandas as pd

def data_scaling_mean_centered(input_data):
    '''
    Scale the data by subtracting the mean of each column from each value in the column

    Args:
        input_data (pandas.DataFrame): Dataframe containing the data

    Returns:    
        pandas.DataFrame: Scaled dataframe
    '''

    data_scaled = input_data.subtract(input_data.mean(axis=0), axis=1)
    scaled_data=input_data.copy
    scaled_data.iloc[:,2:]=data_scaled

    return scaled_data