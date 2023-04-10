from sklearn.decomposition import PCA
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
import matplotlib.pyplot as plt
import numpy as np


def PCA_analysis(normalized_data, number_of_components=2):
    """
    Perform PCA analysis on the data

    Args:
        input_data (pandas.DataFrame): Dataframe containing the data
        number_of_components (int, optional): Number of principal components to return. Defaults to 2.

    Returns:
        pandas.DataFrame: Dataframe containing the principal components
    """
    normalized_data = normalized_data.iloc[:, 2:]
    # Initialize PCA object with desired number of components
    pca = PCA(n_components=number_of_components)

    # Fit the PCA model to the data
    pca.fit(normalized_data)

    # perform PCA on the DataFrame
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(normalized_data)

    # get the percentage of variance explained by each principal component
    variance_explained = pca.explained_variance_ratio_

    # create a new DataFrame with the principal components
    principal_df = pd.DataFrame(data=principal_components, columns=["PC1", "PC2"])

    # create a scatter plot of the principal components with annotations
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel(
        "Principal Component 1\nVariance explained: {:.2f}%".format(
            variance_explained[0] * 100
        ),
        fontsize=15,
    )
    ax.set_ylabel(
        "Principal Component 2\nVariance explained: {:.2f}%".format(
            variance_explained[1] * 100
        ),
        fontsize=15,
    )
    ax.set_title("2 Component PCA", fontsize=20)

    ax.scatter(principal_df["PC1"], principal_df["PC2"], s=50)

    return principal_df


def volcano_plot(
    grouped_data,
    sig_threshold=0.05,
    fold_change_threshold=1.5,
    group_name="Muscle loss",
    group_A_name="control",
    group_B_name="cachexic",
):
    """
    Perform a two-sample t-test on each feature and plot the results as a volcano plot
    """

    # convert the data to float
    grouped_data = grouped_data.iloc[:, 1:]
    grouped_data.iloc[:, 1:] = grouped_data.iloc[:, 1:].astype(float)
    # set significance threshold and fold change threshold
    sig_threshold = 0.05
    fold_change_threshold = 1.5

    # create a new DataFrame to store the results
    result_grouped_data = pd.DataFrame(
        columns=["Metabolite", "Fold Change", "P-value", "FDR"]
    )

    # iterate over each feature
    for col in grouped_data.iloc[:, 1:]:
        group_A = grouped_data[grouped_data[group_name] == group_A_name][col]
        group_B = grouped_data[grouped_data[group_name] == group_B_name][col]

        # perform a two-sample t-test for each feature
        t_stat, p_val = stats.ttest_ind(group_A, group_B)

        # calculate the fold change
        mean_A = group_A.mean()
        mean_B = group_B.mean()
        fold_change = mean_B / mean_A

        # correct the p-value for multiple testing using Benjamini-Hochberg procedure
        p_vals = [p_val]
        corrected_p_vals = multipletests(p_vals, method="fdr_bh")[1][0]

        # add the results to the result DataFrame
        result_grouped_data = result_grouped_data.append(
            {
                "Metabolite": col,
                "Fold Change": fold_change,
                "P-value": p_val,
                "FDR": corrected_p_vals,
            },
            ignore_index=True,
        )

    # filter significant features based on FDR and fold change threshold
    sig_features = result_grouped_data[
        (result_grouped_data["FDR"] < sig_threshold)
        & (abs(result_grouped_data["Fold Change"]) > fold_change_threshold)
    ]

    # plot volcano plot
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(
        result_grouped_data["Fold Change"],
        -1 * np.log10(result_grouped_data["P-value"]),
        alpha=0.5,
    )
    ax.scatter(
        sig_features["Fold Change"],
        -1 * np.log10(sig_features["P-value"]),
        color="red",
        alpha=0.5,
    )
    ax.axvline(x=1, color="black", linestyle="--")
    ax.axvline(x=-1, color="black", linestyle="--")
    ax.axhline(y=-np.log10(sig_threshold), color="black", linestyle="--")
    ax.set_xlabel("Fold Change")
    ax.set_ylabel("-Log10 P-value")
    ax.set_title("Volcano Plot")
    plt.show()

    return result_grouped_data


def ma_plot(
    grouped_data,
    group_name="Muscle loss",
    group_A_name="control",
    group_B_name="cachexic",
):
    """
    Create an MA plot
    """
    # Calculate the log-fold change and mean expression
    cachexic_mean = (
        grouped_data[grouped_data[group_name] == group_B_name].iloc[:, 1:].mean()
    )
    control_mean = (
        grouped_data[grouped_data[group_name] == group_A_name].iloc[:, 1:].mean()
    )
    logFC = np.log2(cachexic_mean / control_mean)
    data_mean = np.log2(grouped_data.iloc[:, 1:].mean(axis=0))
    # Create the MA plot
    plt.scatter(data_mean, logFC, s=10, alpha=0.5, color="black")
    plt.axhline(y=0, color="gray", linestyle="--")
    plt.xlabel("Mean Expression (log2)")
    plt.ylabel("Log-Fold Change (log2)")
    plt.title("MA Plot")
    plt.show()

    return (logFC, data_mean)
