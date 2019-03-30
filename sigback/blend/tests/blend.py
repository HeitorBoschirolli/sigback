import numpy as np
import unittest
from skimage.io import imread
from skimage import img_as_float64

from sigback.blend import blend
from sigback.processing import transform


class BlendTest(unittest.TestCase):
    test_data_path = './sigback/blend/tests/data'

    def test_blend(self):
        doc = img_as_float64(
            imread(self.test_data_path + '/test_doc.jpg', as_gray=True)
        )
        sig = img_as_float64(
            imread(self.test_data_path + '/test_sig_cropped.png', as_gray=True)
        )

        sig_barycenter = transform.barycenter(sig)
        actual = blend.blend(sig, sig_barycenter, doc, (1215, 1800))
        expected = img_as_float64(
            imread(self.test_data_path + '/blended.png', as_gray=True)
        )

        np.testing.assert_almost_equal(expected, actual, 0.001)
    
    def test_blend_big_sig(self):
        doc = img_as_float64(
            imread(self.test_data_path + '/test_doc.jpg', as_gray=True)
        )
        sig = img_as_float64(
            imread(
                self.test_data_path + '/test_big_sig_cropped.png',
                as_gray=True
            )
        )

        sig_barycenter = transform.barycenter(sig)
        actual = blend.blend(sig, sig_barycenter, doc, (1215, 1800))
        expected = img_as_float64(
            imread(self.test_data_path + '/big_blended.png', as_gray=True)
        )

        np.testing.assert_almost_equal(expected, actual, 0.001)


if __name__ == "__main__":
    unittest.main()