import numpy as np


class BaseEstimiator(object):
    X = None
    y = None
    y_required = True

    def _setup_input(self, X, y=None):
        pass