import pandas as pd
import os
from pathlib import Path

def get_file_path(sub_dir1,sub_dir2,filename):
    tool_directory=Path.cwd()
    #project_directory=os.path.dirname(tool_directory)
    data_directory=os.path.join(tool_directory,sub_dir1,sub_dir2,filename)
    return data_directory

def read_data(filename):
    """
    Read the data from the data folder and return a pandas dataframe

    Args:
        filename (str, optional): Name of the file to read. Defaults to "human_cachexia.csv".

    Returns:
        pandas.DataFrame: Dataframe containing the data
    """
    input_data=pd.read_csv(filename)
    print("data read successfully, the shape of the dataframe is: ", input_data.shape)

    return input_data