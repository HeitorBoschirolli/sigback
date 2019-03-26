import numpy as np
import unittest
from skimage.io import imread
from skimage import img_as_float

from sigback.blend import blend


class BlendTest(unittest.TestCase):
    test_data_path = './sigback/processing/tests/data'

    def test_blend(self):
        print('pru')


if __name__ == "__main__":
    unittest.main()