import numpy as np
import random
import os
from skimage import img_as_float64
from skimage.io import imread, imsave

from sigback.processing import color, transform


def blend(sig, sig_barycenter, doc, doc_center):
    n_rows_doc, n_cols_doc = doc.shape
    n_rows_sig, n_cols_sig = sig.shape

    sig_start_row = int(np.ceil(doc_center[0] - sig_barycenter[0]))
    sig_start_col = int(np.ceil(doc_center[1] - sig_barycenter[1]))

    if sig_start_row + n_rows_sig > n_rows_doc:
        sig_start_row = n_rows_doc - n_rows_sig
    if sig_start_col + n_cols_sig > n_cols_doc:
        sig_start_col = n_cols_doc - n_cols_sig
    
    sig_end_row = sig_start_row + n_rows_sig
    sig_end_col = sig_start_col + n_cols_sig

    signed_doc = np.copy(doc)
    signed_doc[
        sig_start_row:sig_end_row,
        sig_start_col:sig_end_col
    ] = doc[sig_start_row:sig_end_row, sig_start_col:sig_end_col] * sig

    return signed_doc

def blend_dirs(sigs_dir, docs_dir, doc_centers, save_dir, seed=None):
    sig_files = os.listdir(sigs_dir)
    doc_files = sorted(os.listdir(docs_dir))

    sig_files = [os.path.join(sigs_dir, sig_file) for sig_file in sig_files]
    doc_files = [os.path.join(docs_dir, doc_file) for doc_file in doc_files]

    n_sigs = len(sig_files)
    n_docs = len(doc_files)

    if n_docs > n_sigs:
        raise Exception(
            '''
            The number of signatures must be greater than or equal to the
            number of documents
            '''
        )
    
    random.seed(seed)
    combined = list(zip(doc_files, doc_centers))
    random.shuffle(combined)
    doc_files[:], doc_centers[:] = zip(*combined)

    for index, sig_file in enumerate(sig_files):
        doc_file = doc_files[index % n_docs]
        
        doc = img_as_float64(imread(doc_file, as_gray=True))
        sig = img_as_float64(imread(sig_file, as_gray=True))

        sig = color.binarize(sig)
        sig = color.remove_background(sig)
        sig = transform.remove_border(sig)
        sig_barycenter = transform.barycenter(sig)

        try:
            blended = blend(
                sig,
                sig_barycenter,
                doc,
                doc_centers[index % n_docs]
            )
        except Exception as inst:
            if sig.shape[0] > doc.shape[0] or sig.shape[1] > doc.shape[1]:
                raise Exception(
                    'The signature must be smaller than the document'
                ) 
            raise inst

        sig_name = os.path.split(sig_file)[-1]
        blended_file = os.path.join(save_dir, sig_name)

        imsave(blended_file, blended)