import numpy as np
from skimage.filters import threshold_otsu

def binarize(img, nl=3, method='posterization'):
    if method == 'posterization':
        post_img = np.round(img * nl) / nl
        return 1 - ((1 - post_img) > 0)
    elif method == 'otsu':
        pass
    else:
        raise(Exception("method not supported"))

