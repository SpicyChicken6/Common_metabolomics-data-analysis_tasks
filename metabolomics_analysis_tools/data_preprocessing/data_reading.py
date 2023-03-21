import pkgutil
import csv
from io import StringIO
import pandas as pd

#read the test dataset from the package into a dataframe
def read_data_file(package_name='metabolomics_analysis_tools', file_path='resources/test_dataset/human_cachexia.csv'):
    data_bytes = pkgutil.get_data(package_name, file_path)
    if data_bytes is None:
        raise FileNotFoundError("Could not find data file")
        
    else:
        print("data read successfully")
        data_str = data_bytes.decode('utf-8')
        data_file = StringIO(data_str)
        csv_reader = csv.reader(data_file)
        rows = [row for row in csv_reader]
        df = pd.DataFrame(rows[1:], columns=rows[0])
        print("the shape of the dataframe is: ", df.shape)
        return df
    

