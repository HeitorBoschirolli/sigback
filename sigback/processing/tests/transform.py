import numpy as np
import unittest
from skimage.io import imread
from skimage import img_as_float64

from sigback.processing import transform  


class ProcessingTest(unittest.TestCase):
    test_data_path = './sigback/processing/tests/data'

    def test_remove_border(self):
        sig = img_as_float64(
            imread(self.test_data_path + '/test_sig_no_bg.png')
        )
        actual = transform.remove_border(sig)
        expected = img_as_float64(
            imread(self.test_data_path + '/test_sig_cropped.png')
        )
        np.testing.assert_almost_equal(expected, actual, 0.01)


    def test_barycenter(self):
        sig = img_as_float64(
            imread(self.test_data_path + '/test_sig_cropped.png')
        )
        actual = transform.barycenter(sig)
        expected = (155.0, 192.0)
        self.assertAlmostEquals(actual[0], expected[0], 0.001)
        self.assertAlmostEquals(actual[1], expected[1], 0.001)


if __name__ == "__main__":
    unittest.main()