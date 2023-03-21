from sklearn.decomposition import PCA
import pandas as pd

def PCA_analysis(input_data, number_of_components=2):
    '''
    Perform PCA analysis on the data
    
    Args:
        input_data (pandas.DataFrame): Dataframe containing the data
        number_of_components (int, optional): Number of principal components to return. Defaults to 2.

    Returns:
        pandas.DataFrame: Dataframe containing the principal components
    '''

    # Load data into a Pandas DataFrame

    # Initialize PCA object with desired number of components
    pca = PCA(n_components=number_of_components)

    # Fit the PCA model to the data
    pca.fit(input_data)

    # Transform the data to the new coordinate system defined by the principal components
    data_pca = pca.transform(input_data)

    # Create a new DataFrame with the principal components
    df_pca = pd.DataFrame(data=data_pca, columns=['PC1', 'PC2'])

    return df_pca