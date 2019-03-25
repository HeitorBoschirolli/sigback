import unittest
import numpy as np
from skimage.io import imread
from skimage import img_as_float64

from sigback.processing import color


class ProcessingTest(unittest.TestCase):
    test_data_path = './sigback/processing/tests/data'

    def test_binarize(self):
        sig = img_as_float64(
            imread(self.test_data_path + '/test_sig.png', as_gray=True)
        )
        actual = color.binarize(sig)
        expected = img_as_float64(
            imread(self.test_data_path + '/test_sig_bw.png', as_gray=True)
        )
        np.testing.assert_almost_equal(expected, actual, 0.01)

    def test_remove_background(self):
        sig = img_as_float64(
            imread(self.test_data_path + '/test_sig.png', as_gray=True)
        )
        actual = color.remove_background(sig)
        expected = img_as_float64(
            imread(self.test_data_path + '/test_sig_no_bg.png')
        )
        np.testing.assert_almost_equal(expected, actual)
        

if __name__ == '__main__':
    unittest.main()