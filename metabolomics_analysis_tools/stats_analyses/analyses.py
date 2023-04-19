from sklearn.decomposition import PCA
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def PCA_analysis(normalized_data, number_of_components=2):
    data_to_process = normalized_data.iloc[:, 2:]
    pca = PCA(n_components=number_of_components)
    principal_components = pca.fit_transform(data_to_process)
    principal_df = pd.DataFrame(
        data=principal_components, columns=[f"PC {i+1}" for i in range(number_of_components)]
    )
    groups = normalized_data.iloc[:, 1]

    # Create a LabelEncoder to encode the groups as integers
    le = LabelEncoder()
    groups_encoded = le.fit_transform(groups)

    # Create a colormap based on the number of unique groups
    cmap = plt.cm.get_cmap('viridis', len(np.unique(groups_encoded)))

    fig, ax = plt.subplots()
    scatter = ax.scatter(
        principal_df["PC 1"], principal_df["PC 2"], c=groups_encoded, cmap=cmap
    )

    # Create a legend with the group labels
    legend_elements = [plt.Line2D([0], [0], marker='o', color=cmap(i), label=label, markersize=7, linestyle='')
                       for i, label in enumerate(le.classes_)]
    legend1 = ax.legend(handles=legend_elements, title="Groups")
    ax.add_artist(legend1)
    ax.set_xlabel("PC 1")
    ax.set_ylabel("PC 2")
    ax.set_title("PCA of Metabolomic Data")

    return fig



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

    return fig



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
    fig, ax = plt.subplots()
    ax.scatter(data_mean, logFC, s=10, alpha=0.5, color="black")
    ax.axhline(y=0, color="gray", linestyle="--")
    ax.set_xlabel("Mean Expression (log2)")
    ax.set_ylabel("Log-Fold Change (log2)")
    ax.set_title("MA Plot")

    return fig