**Metabolomics analysis tools**

*Introduction: Tool development for bioinf576 class*

The goal of this project is to implement a Python based pipeline or package related to metabolomics data analysis. I am currently working with targeted metabolomics data in my lab, and it will be helpful with my work to develop a package that contains some very common metabolomics data analysis tools, including:
* data transformation
* data normalization
* data scaling
* common statistical analyses that contains PCA and MA plot. 

Even though there are lots of packages available for the functions mentioned above, implementing them myself will help me understand those functions better and help me do a better analysis job hopefully.  

![metabolomics analysis workflow](resources/images/mwf.gif)

**Package user guide**

*How to use the sample data*

The sample data file "human_cachexia.csv" is located under the path "metabolomics_analysis_tools/metabolomics_analysis_tools/resources/test_dataset/". After the package is installed, to load the data with the "read_data_file" function included, it will use this sample data by default. The parameter "file_path" can be used to specity the user-defined data file location to load. However, the user-defined file should have similar data format as in the sample data, in which the data can be separated into two groups: cachexic and control.
