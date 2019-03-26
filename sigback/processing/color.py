import numpy as np
from skimage.filters import threshold_otsu


def binarize(img, nl=3, method='posterization'):
    if method == 'posterization':
        post_img = np.round(img * nl) / nl
        return 1 - ((1 - post_img) > 0)
    elif method == 'otsu':
        pass
    else:
        raise(Exception('method not supported'))


def remove_background(img, nl=3, method='posterization'):
    if len(img.shape) != 2:
        raise(Exception('image must be in grayscale'))
    
    bin_img = binarize(img, nl, method)
    no_bg_img = img
    no_bg_img[bin_img==1] = 1
    return no_bg_img
