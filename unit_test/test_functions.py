import modules.test_module as tm
import modules.normalization as nm
import modules.transformation as tf
import modules.data_processing as dp

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

filename="human_cachexia.txt"
def test_data_processing_edge1():
    '''
    test if the function can handle a file with a different extension
    '''
    assert dp.get_file_path(sub_dir1,sub_dir2,filename).endswith('csv'), f"function passed the test"
    assert dp.get_file_path(sub_dir1,sub_dir2,filename).endswith('txt'), f"wrong file formate, please check the file extension"
    assert dp.get_file_path(sub_dir1,sub_dir2,filename).endswith('xlsx'), f"wrong file formate, please check the file extension"
##


def test_normalization_sum():
    assert nm.normalize_by_sum() == 3, f"function passed the test"

##
def test_normalization_sum_edge1():
    assert nm.normalize_by_sum() == 3, f"function passed the test"

##
def test_log_transform():
    assert tf.data_transformation_log() == 3, f"function passed the test"

##