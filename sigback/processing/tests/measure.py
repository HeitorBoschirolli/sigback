import unittest
import os
import numpy as np
from skimage.io import imread, imsave
from skimage import img_as_float64
from shutil import rmtree

from sigback.processing import measure


class MeasureTest(unittest.TestCase):
    test_data_path = './sigback/processing/tests/data'

    def setUp(self):
        test_dir = os.path.join(self.test_data_path, 'img_dir')
        empty_test_dir = os.path.join(self.test_data_path, 'empty_img_dir')

        if (not os.path.exists(test_dir)):
            os.mkdir(test_dir)
        if (not os.path.exists(empty_test_dir)):
            os.mkdir(empty_test_dir)

        img_names = ['first.png', 'second.png']
        imgs = [np.random.rand(100, 200), np.random.rand(150, 300)]

        for img, img_name in zip(imgs, img_names):
            full_path = os.path.join(test_dir, img_name)
            imsave(full_path, img)
    
    def tearDown(self):
        test_dir = os.path.join(self.test_data_path, 'img_dir')
        empty_test_dir = os.path.join(self.test_data_path, 'empty_img_dir')

        if (os.path.exists(test_dir)):
            rmtree(test_dir)
        if (os.path.exists(empty_test_dir)):
            rmtree(empty_test_dir)

    def test_minmax(self):
        test_dir = os.path.join(self.test_data_path, 'img_dir')

        actual = measure.minmax(test_dir)
        expected = (150, 300, 100, 200)

        self.assertEqual(expected, actual)

    def test_minmax_empty_dir(self):
        test_dir = os.path.join(self.test_data_path, 'empty_img_dir')

        actual = measure.minmax(test_dir)
        expected = (0, 0, -1, -1)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()