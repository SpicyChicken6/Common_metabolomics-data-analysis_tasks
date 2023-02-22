import pandas as pd
import os
from pathlib import Path

#data reading
def read_data(filename="human_cachexia.csv"):
    """
    Read the data from the data folder and return a pandas dataframe

    Args:
        filename (str, optional): Name of the file to read. Defaults to "human_cachexia.csv".

    Returns:
        pandas.DataFrame: Dataframe containing the data
    """

    tool_directory=Path.cwd()
    project_directory=os.path.dirname(tool_directory)
    data_directory=os.path.join(project_directory,'resources','test_dataset',filename)
    input_data=pd.read_csv(data_directory)
    print("data read successfully, the shape of the dataframe is: ", input_data.shape)

    return input_data