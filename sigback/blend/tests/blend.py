import numpy as np
import unittest
import os
import shutil
from skimage.io import imread
from skimage.transform import rescale
from skimage import img_as_float64

from sigback.blend import blend
from sigback.processing import transform


rand = str(np.random.randint(10000, 100000))
test_data_path = './sigback/blend/tests/data'
save_dir = '/tmp/' + rand + 'sigback_test_file'
tol = 5

class BlendTest(unittest.TestCase):

    def setUp(self):
        if not (os.path.exists(save_dir)):
            os.makedirs(save_dir)
        else:
            raise('directory already exists')

    def tearDown(self):
        if os.path.exists(save_dir):
            shutil.rmtree(save_dir)

    def test_blend(self):
        doc = img_as_float64(
            imread(test_data_path + '/test_doc.jpg', as_gray=True)
        )
        sig = img_as_float64(
            imread(test_data_path + '/test_sig_cropped.png', as_gray=True)
        )

        sig_barycenter = transform.barycenter(sig)
        actual = blend.blend(sig, sig_barycenter, doc, (1215, 1800))
        expected = img_as_float64(
            imread(test_data_path + '/blended.png', as_gray=True)
        )

        np.testing.assert_almost_equal(expected, actual, decimal=tol)

    def test_blend_keep_size(self):
        doc = img_as_float64(
            imread(test_data_path + '/test_doc.jpg', as_gray=True)
        )
        sig = img_as_float64(
            imread(test_data_path + '/test_sig_cropped.png', as_gray=True)
        )
        sig_barycenter = transform.barycenter(sig)
        actual = blend.blend(sig, sig_barycenter, doc, (1215, 1800), True)
        expected = img_as_float64(
            imread(test_data_path + '/blended_keep_size.png', as_gray=True)
        )

        np.testing.assert_almost_equal(expected, actual, decimal=tol)
    
    def test_blend_big_sig(self):
        doc = img_as_float64(
            imread(test_data_path + '/test_doc.jpg', as_gray=True)
        )
        sig = img_as_float64(
            imread(test_data_path + '/test_big_sig_cropped.png', as_gray=True)
        )

        sig_barycenter = transform.barycenter(sig)
        actual = blend.blend(sig, sig_barycenter, doc, (1215, 1800))
        expected = img_as_float64(
            imread(test_data_path + '/big_blended.png', as_gray=True)
        )

        np.testing.assert_almost_equal(expected, actual, decimal=tol)

    def test_blend_big_sig_keep_size(self):
        doc = img_as_float64(
            imread(test_data_path + '/test_doc.jpg', as_gray=True)
        )
        sig = img_as_float64(
            imread(test_data_path + '/test_big_sig_cropped.png', as_gray=True)
        )

        sig_barycenter = transform.barycenter(sig)
        actual = blend.blend(sig, sig_barycenter, doc, (1215, 1800), True)
        expected = img_as_float64(
            imread(test_data_path + '/big_blended_keep_size.png', as_gray=True)
        )

        np.testing.assert_almost_equal(expected, actual, decimal=tol)

    def test_blend_biggest_sig(self):
        doc = img_as_float64(
            imread(test_data_path + '/test_doc.jpg', as_gray=True)
        )
        sig = img_as_float64(
            imread(test_data_path + '/test_big_sig_cropped.png', as_gray=True)
        )
        sig = rescale(sig, 5)

        sig_barycenter = transform.barycenter(sig)
        actual = blend.blend(sig, sig_barycenter, doc, (1215, 1800))

        expected = img_as_float64(
            imread(test_data_path + '/biggest_sig_blended.png', as_gray=True)
        )

        np.testing.assert_almost_equal(expected, actual, decimal=tol)

    def test_blend_biggest_sig_keep_size(self):
        doc = img_as_float64(
            imread(test_data_path + '/test_doc.jpg', as_gray=True)
        )
        sig = img_as_float64(
            imread(test_data_path + '/test_big_sig_cropped.png', as_gray=True)
        )
        sig = rescale(sig, 5)

        sig_barycenter = transform.barycenter(sig)
        actual = blend.blend(sig, sig_barycenter, doc, (1215, 1800), True)

        expected = img_as_float64(
            imread(
                test_data_path + '/biggest_sig_blended_keep_size.png',
                as_gray=True
            )
        )

        np.testing.assert_almost_equal(expected, actual, decimal=tol)
    
    def test_blend_dirs(self):
        sigs_dir = os.path.join(test_data_path, 'sigs')
        docs_dir = os.path.join(test_data_path, 'docs')
        doc_centers = [(1215, 1800), (659, 2602)]

        blend.blend_dirs(sigs_dir, docs_dir, doc_centers, save_dir, False, 1)

        expecteds_path = os.path.join(test_data_path, 'blended')
        expected_files = [
            os.path.join(expecteds_path, path)
            for path in os.listdir(expecteds_path)
        ]
        expected_files.sort()

        actual_files = [
            os.path.join(save_dir, path)
            for path in os.listdir(save_dir)
        ]
        actual_files.sort()
    
        assert(len(actual_files) == len(expected_files))

        for expected_file, actual_file in zip(expected_files, actual_files):
            expected = img_as_float64(imread(expected_file, as_gray=True))
            actual = img_as_float64(imread(actual_file, as_gray=True))

            np.testing.assert_almost_equal(actual, expected, decimal=tol)

    def test_blend_dirs_keep_size(self):
        sigs_dir = os.path.join(test_data_path, 'sigs')
        docs_dir = os.path.join(test_data_path, 'docs')
        doc_centers = [(1215, 1800), (659, 2602)]

        blend.blend_dirs(sigs_dir, docs_dir, doc_centers, save_dir, True, 1)

        expecteds_path = os.path.join(test_data_path, 'ks_blended')
        expected_files = [
            os.path.join(expecteds_path, path)
            for path in os.listdir(expecteds_path)
        ]
        expected_files.sort()

        actual_files = [
            os.path.join(save_dir, path)
            for path in os.listdir(save_dir)
        ]
        actual_files.sort()
    
        assert(len(actual_files) == len(expected_files))

        for expected_file, actual_file in zip(expected_files, actual_files):
            expected = img_as_float64(imread(expected_file, as_gray=True))
            actual = img_as_float64(imread(actual_file, as_gray=True))

            np.testing.assert_almost_equal(actual, expected, decimal=tol)



if __name__ == "__main__":
    unittest.main()