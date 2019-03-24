import numpy as np
import unittest
from sigback.processing import transform  

def remove_border():
    transform.remove_border(np.empty(5, 5))


def barycenter():
    transform.barycenter(np.empty(5, 5))