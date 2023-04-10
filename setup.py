from setuptools import setup, find_packages

setup(
    name="metabolomics_analysis_tools",
    version="0.1.0",
    description="common metabolomics analysis tools",
    author="Zhijian Yu",
    author_email="yuzhijian@outlook.com",
    url="https://github.com/SpicyChicken6/metabolomics_analysis_tools.git",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "metabolomics_analysis_tools": ["resources/test_dataset/*"],
    },
)
