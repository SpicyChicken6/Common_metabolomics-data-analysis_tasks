import modules.test_module as tm
import modules.data_preprocessing.normalization as nm
import modules.data_preprocessing.transformation as tf
import modules.data_preprocessing.data_reading as dp

## a simple test function to see if unit testing is working
def test_xy_sum():
    assert tm.x_y_sum(1, 2) == 3, f"test function passed the test, unit testing is working"

# test functions for each module
## file processsing
sub_dir1="resources"
sub_dir2="test_dataset"
filename="human_cachexia.csv"
file_to_process=dp.get_file_path(sub_dir1,sub_dir2,filename)

def test_read_file():
    assert dp.read_data(file_to_process).shape == (77,65), f"function passed the test, file read successfully"


filename="human_cachexia.csv"
def test_read_file_edge1():
    '''
    edge cases when file format is wrong
    '''
    assert dp.get_file_path(sub_dir1,sub_dir2,filename).endswith('csv'), f"function passed the test"

def test_read_file_edge2():
    '''
    edge case when the file name is not in string
    '''
    assert type(file_to_process)==str, f"correct fi;e name format, please check the input"

    
##
## normalization
after_norm=nm.normalize_by_sum(dp.read_data(file_to_process)).iloc[:,2:].sum(axis=0)

def test_normalization_sum():
    assert after_norm[0:].sum(axis=0)==len(after_norm), f"function passed the test, normalization by sum is working"

# ##
# def test_normalization_sum_edge1():
#     assert nm.normalize_by_sum() == 3, f"function passed the test"

# ##
# def test_log_transform():
#     assert tf.data_transformation_log() == 3, f"function passed the test"

# ##