# Example PyPI (Python Package Index) Package
import unittest
from astropy.io import fits
import astropy.io
import numpy as np
import matplotlib
from astropy.table import Table
import astropy.io
from scipy import stats
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from astroML.stats import fit_bivariate_normal
from astroML.stats.random import bivariate_normal
import numpy as np
import pandas as pd
import pkg_resources
class test_num(object):

    def __init__(self, n):
        self.value = n

    def square(self):
        a = self.value
        return a * a
    def load_example():
        stream = pkg_resources.resource_stream(__name__, 'data/example.csv')
        return pd.read_csv(stream)
    a = load_example()
    print(a)
    
        

