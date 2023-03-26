**Metabolomics analysis tools**

*---Introduction: Tool development for bioinf576 class---*

The goal of this project is to implement a Python based pipeline or package related to metabolomics data analysis. I am currently working with targeted metabolomics data in my lab, and it will be helpful with my work to develop a package that contains some very common metabolomics data analysis tools, including:
* data transformation
* data normalization
* data scaling
* common statistical analyses including PCA, MA plot and Volcano plot. 

Even though there are lots of packages available for the functions mentioned above, implementing them myself will help me understand those functions better and help me do a better analysis job hopefully.  

![metabolomics analysis workflow](metabolomics_analysis_tools/resources/images/mwf.gif)

**Package user guide**

*---Package install---*

Steps:
1. Git clone or download the github folder;
2. Open the terminal, and go to this folder;
3. Enter 'pip install dist/metabolomics_analysis_tools-0.1.0.tar.gz' to install the package locally;


*---Sample data file---*

The sample data file "human_cachexia.csv" is located under the path "metabolomics_analysis_tools/metabolomics_analysis_tools/resources/test_dataset/". After the package is installed, to load the data with the "read_data_file" function included, it will use this sample data by default. The parameter "file_path" can be used to specity the user-defined data file location to load. However, the user-defined file should have similar data format as in the sample data, as shown below:
<img width="1157" alt="image" src="https://user-images.githubusercontent.com/72659448/227754357-40e8be65-129d-47c1-b3ac-dbd6f3202eaf.png">
<sub> (Column 1 is the patient id info,\
Column 2 is the group assigned for patients (note that this package focuses on single factor analysis, which means there should be only two groups in the data) ,\
Column 3 to the end will be the metabolite levels for different metabolites) </sub>


*---To Use functions---*

There are two groups of functions in this package, and there are multiple modules under each of these group:
* "data_preprocessing": \
  data_reading <sub>(functions include: read_data_file)</sub>\
  normalization <sub>(functions include: normalize_by_sum, normalize_by_median, normalize_by_reference_sample_PQN, )</sub>\
  scaling <sub>(functions include: data_scaling_mean_centered)</sub>\
  transformation <sub>(functions include: data_transformation_log)</sub>
  
* "stats_analyses": \
  analyses <sub>(functions include: PCA_analysis, ma_plot, volcano_plot)</sub>

To use a certain function, for example, to use read_data_file function to read file, you can do: \
'import metabolomics_analysis_tools.data_preprocessing as dp \
df=dp.data_reading.read_data_file()'





