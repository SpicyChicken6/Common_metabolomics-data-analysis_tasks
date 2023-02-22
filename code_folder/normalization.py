import numpy as np
import pandas as pd


def test_function_sum(x,y):
    sum=x+y
    return sum

##normalization methods
def normalize_by_sum(input_data):
    '''
    Normalize the data by dividing each column by the sum of the row

    Args:
        input_data (pandas.DataFrame): Dataframe containing the data

    Returns:
        pandas.DataFrame: Normalized dataframe
    '''
    data_to_process=input_data.iloc[:,2:]
    normalized_data=data_to_process.div(data_to_process.sum(axis=0), axis=1)
    normed_data=input_data.copy
    normed_data.iloc[:,2:]=normalized_data
    
    return normed_data



def normalize_by_median(input_data):
    '''
    Normalize the data by dividing each column by the median of the row

    Args:
        input_data (pandas.DataFrame): Dataframe containing the data

    Returns:
        pandas.DataFrame: Normalized dataframe
    '''

    data_to_process=input_data.iloc[:,2:]
    normalized_data=data_to_process.div(data_to_process.median(axis=0), axis=1)
    normed_data=input_data.copy
    normed_data.iloc[:,2:]=normalized_data

    return normed_data


def normalize_by_reference_sample_PQN(input_data):
    '''
    Normalize the data by dividing each column by the PQN of the reference sample. 
    PQN has been shown to be effective at normalizing data from different platforms and technologies, 
    and can reduce batch effects and other systematic variations in data. However, 
    PQN assumes that most genes or proteins are not differentially expressed, which may not be true in all cases. 
    Additionally, PQN may not be appropriate for all types of data, 
    and other normalization methods may be more appropriate 
    depending on the specific research question and experimental design.

    Args:
        input_data (pandas.DataFrame): Dataframe containing the data

    Returns:
        pandas.DataFrame: Normalized dataframe

    '''
    data_to_process=input_data.iloc[:,2:]
    sample_medians = data_to_process.median(axis=0)
    data_norm = data_to_process.div(sample_medians, axis=1)
    metabolite_means = np.exp(np.log(data_norm).mean(axis=1))
    data_norm = data_norm.div(metabolite_means, axis=0)
    col_medians = data_norm.median(axis=0)
    data_norm = data_norm.div(col_medians, axis=1)
    normed_data=input_data.copy
    normed_data.iloc[:,2:]=data_norm

    return normed_data
    


