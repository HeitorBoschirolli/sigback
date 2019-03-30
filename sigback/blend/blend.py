import numpy as np

from sigback import processing


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