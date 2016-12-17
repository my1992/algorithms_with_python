from metrics.metrics import mse, logloss, mae, hinge, binary_cross_entropy

categorical_cross_entropy = logloss


def get_loss(name):
    """
    Return loss function by the name.
    :param name:
    :return:
    """
    try:
        return globals()[name]
    except:
        raise ValueError('Invalid metric function.')