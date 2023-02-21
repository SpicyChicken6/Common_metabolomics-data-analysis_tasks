Software requirement specification

V.0.1\
For: metabolomics_analysis_tools
\
By: Zhijian Yu


1.	Introduction

	A set of tools to perform common targeted metabolomics data analysis tasks including data transformation, scaling and normalization, and common statistical analyses -- PCA analysis and MA plot, and visualization.

2.	Overall description 
	
	Input: Metabolites concentration profile of a list of targeted metabolites for different samples\
	Output: The processed data that is suitable for doing downstream analysis, and also the results from PCA analysis and MA plot.
	
3.	Requirements

	Input data format for targeted metabolites concentrations: csv file with columns that contain metabolites concentration values for targeted metabolites; each row represents each sample
