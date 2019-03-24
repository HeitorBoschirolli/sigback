import numpy as np


def remove_border(img):
    neg_img = 1 - img
    
    pixels_on_col = np.sum(neg_img, axis=0)
    cols = np.nonzero(pixels_on_col > 0)[0]
    
    pixels_on_row = np.sum(neg_img, axis=1)
    rows = np.nonzero(pixels_on_row)[0]

    no_borders_img = img[rows[0]:rows[1]][cols[0]:cols[1]]
    return no_borders_img


def barycenter(img):
    (num_rows, num_cols) = img.shape

    bc_col = np.round(
        np.sum(
            np.array(range(num_cols)) * np.sum(img, axis=0),
            axis=0
        ) / np.sum(img)
    )
    bc_row = np.round(
        np.sum(
            np.array(range(num_rows)) * np.sum(img, axis=1),
            axis=0
        ) / np.sum(img)
    )

    return (bc_row, bc_col)