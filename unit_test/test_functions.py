import code_folder.normalization as nm
import code_folder.transformation as tf

def test_normalization_sum():
    assert nm.normalize_by_sum() == 3, f"function passed the test"

def test_normalization_median():
    assert nm.normalize_by_median() == 3, f"function passed the test"

def test_normalization_PQN():
    assert nm.normalize_by_reference_sample_PQN() == 3, f"function passed the test"

def test_log_transform():
    assert tf.data_transformation_log() == 3, f"function passed the test"