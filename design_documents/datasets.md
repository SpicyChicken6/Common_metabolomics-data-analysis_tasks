# Brief description of the datasets to use for this project

1. Targeted metabolomics data
Retrieve metabolites concentration data from 
https://www.metaboanalyst.ca/MetaboAnalyst/upload/StatUploadView.xhtml
  or from
https://www.ebi.ac.uk/metabolights/search? (Metabolights)


2. A data file with metabolites concentration profile
It will contain a matrix with metabolites names and metabolites concentrations on each row for each sample. This file will be provided by the user, I will have data for testing


3. **Real dataset for answering a biological question using the tool** \
  - Description of this dataset: "Metabolite concentrations of 39 rumen samples measured by proton NMR from dairy cows fed with different proportions of barley grain (Ametaj BN, et al.). Group label - 0, 15, 30, or 45 - indicating the percentage of grain in diet." [Real dataset](metabolomics_analysis_tools/resources/test_dataset/cow_diet.csv) 
  - Why use this dataset: This will be a good dataset to use as it contains more than two different groups of subjects, which makes it a good example to test for the clustering with PCA plot, as we already had a good example with our functions for differential expression of metabolites in the tutorial.
  - Biological questions to aks: Can we see the pattern of clustering based on different proportions of barley grain fed in the cows?
  - Expected results: As the data for cows was from different groups, if everything works perfectly, ideally we would like to see the PCA plot can cluster different groups of cows based on their feeding group.
